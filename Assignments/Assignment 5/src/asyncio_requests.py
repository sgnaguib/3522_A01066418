import aiohttp
import asyncio
from poke_objects import *


class RequestHandler:
    """
    Sends requests to the PokeAPI for detailed information
    about either a move, pokemon or ability.
    """

    def __init__(self, mode):
        self.mode = mode
        self.url = 'http://pokeapi.co/api/v2/{}/{}'

    async def get_data(
            self, query, url: str, session: aiohttp.ClientSession):
        """
        (Comment written by Rahul. Has been slightly modified.):
        An async coroutine that executes GET http request to the
        PokeAPI.
        The response is converted to a json.
        The HTTP request and the json conversion are
        asynchronous processes that need to be awaited.
        :param query: an int or a string
        :param url: a string, the unformatted url (missing parameters)
        :param session: a HTTP session
        :return: a dict, json representation of response.
        """
        target_url = url.format(self.mode, query)

        response = await session.request(method="GET", url=target_url)
        try:
            if query == '?':
                raise Exception
            json_dict = await response.json()
        except Exception:
            return f"Error. No data exists for " \
                            f"the query: {query}"
        else:
            return json_dict

    async def process_single_request(self, query, expanded):
        """
        (Comment written by Rahul)
        Gets response from PokeAPI and tries to create a poke_object
        with the response.
        :param query: an int
        :param expanded: boolean
        :return: dict, json response
        """
        async with aiohttp.ClientSession() as session:
            response = await self.get_data(query, self.url, session)
            # either pokemon, move, or ability
            try:
                poke_object = \
                    await self.create_poke_object(response, expanded)
            except Exception:
                return response
            return poke_object

    async def process_multiple_requests(self, requests: list, expanded)\
            -> list:
        """
        Get multiple responses from the PokeAPI and tries to create
        a list of corresponding poke_objects.
        :param expanded: boolean
        :param requests: a list of int's
        :return: list of dict, collection of response data from the
         endpoint.
        """
        async with aiohttp.ClientSession() as session:
            async_coroutines = [self.get_data(query, self.url, session)
                                for query in requests]
            responses = await asyncio.gather(*async_coroutines)
            poke_objects = []
            for response in responses:
                try:
                    poke_object = await \
                        self.create_poke_object(response, expanded)
                except Exception:
                    poke_objects.append(response)
                else:
                    poke_objects.append(poke_object)
            return poke_objects

    async def create_poke_object(self, response, expanded):
        """
        Determines what kind of poke_object to create with the
        response.
        :param response: HTTP response from PokeAPI
        :param expanded: boolean
        :return:
        """
        url_dict = {'ability': self.create_ability,
                    'move': self.create_move}
        if self.mode == 'pokemon':
            return await self.create_pokemon(response, expanded)
        else:
            return url_dict[self.mode](response)

    def create_move(self, response):
        """
        Uses the PokeAPI response to create a Move object.
        :param response:
        :return: Move
        """
        move = Move(response['name'],
                    response['id'],
                    response['generation']['name'],
                    response['accuracy'],
                    response['pp'],
                    response['power'],
                    response['type']['name'],
                    response['damage_class']['name'],
                    response['effect_entries'][0]['short_effect'])
        return move

    async def create_pokemon(self, response, expanded):
        """
         Uses the PokeAPI response to create a Pokemon object.
          :param response:
          :param expanded: boolean
          :return: Pokemon
        """

        moves_list = await \
            self.create_moves_list(response['moves'], expanded)

        abilities_list = await \
            self.create_ability_list(response['abilities'], expanded)

        types_list = \
            [element['type']['name'] for element in
             response['types']]

        stats_list = await \
            self.create_stat_list(response['stats'], expanded)

        pokemon = Pokemon(response['name'],
                          response['id'],
                          response['height'],
                          response['weight'],
                          stats_list,
                          types_list,
                          abilities_list,
                          moves_list)
        return pokemon

    def create_ability(self, response):
        """
         Uses the PokeAPI response to create an Ability object.
        :param response:
        :return: Ability
        """

        pokemon_list =\
            [element['pokemon']['name'] for element in response['pokemon']]

        ability = Ability(response['name'],
                          response['id'],
                          response['generation']['name'],
                          response['effect_entries'][0]['effect'],
                          response['effect_entries'][0]['short_effect'],
                          pokemon_list)
        return ability

    async def create_stat_list(self, stats, expanded):
        """ Uses the PokeAPI stats response to create a list
            Stat object.
          :param stats:
          :param expanded: boolean
          :return: List of Stat objects
          """

        stat_list = []
        for stat in stats:
            if expanded:
                sub_url = stat['stat']['url']
                expanded_dict = await self.expanded_request(sub_url)
                stat_obj = Stat(stat['stat']['name'],
                                stat['base_stat'],
                                expanded,
                                expanded_dict['id'],
                                expanded_dict['is_battle_only'])
            else:
                stat_obj = Stat(stat['stat']['name'],
                                stat['base_stat'],
                                expanded)

            stat_list.append(stat_obj)

        return stat_list

    async def create_ability_list(self, abilities, expanded):
        """ Uses the PokeAPI abilities response to create a list
            Ability object.
          :param abilities: list of abilities
          :param expanded: boolean
          :return: List of Stat objects
          """

        ability_list = []

        for ability in abilities:
            if expanded:
                sub_url = ability['ability']['url']
                expanded_dict = await self.expanded_request(sub_url)
                ability_exp = self.create_ability(expanded_dict)
                ability_list.append(ability_exp)
            else:
                ability_list.append(ability['ability']['name'])

        return ability_list

    async def create_moves_list(self, moves, expanded):
        """ Uses the PokeAPI moves response to create a list
            Move object.
          :param moves:
          :param expanded: boolean
          :return: List of Stat objects
          """
        moves_list = []

        for move in moves:
            if expanded:
                sub_url = move['move']['url']
                expanded_dict = await self.expanded_request(sub_url)
                move_exp = self.create_move(expanded_dict)
                moves_list.append(move_exp)
            else:
                name = move['move']['name']
                level = \
                    move['version_group_details'][0]['level_learned_at']
                moves_list.append(f'{name}, acquired at level: '
                                  f'{level}')
        return moves_list

    async def expanded_request(self, target_url):
        """Send an HTTP request to the PokeAPI to retrieve
        more information for the Pokemon object"""
        async with aiohttp.ClientSession() as session:
            response = \
                await session.request(method="GET", url=target_url)
            json_dict = await response.json()
            return json_dict


