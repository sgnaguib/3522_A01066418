import aiohttp
import asyncio
from poke_objects import *


class RequestHandler:

    def __init__(self, mode):
        self.mode = mode
        self.url = 'http://pokeapi.co/api/v2/{}/{}'

    async def get_data(
            self, query, url: str, session: aiohttp.ClientSession):
        """
        An async coroutine that executes GET http request. The response is
        converted to a json. The HTTP request and the json conversion are
        asynchronous processes that need to be awaited.
        :param query: an int or string
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
        This function depicts the use of await to showcase how one async
        coroutine can await another async coroutine
        :param query: an int
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
        This function depicts the use of asyncio.gather to run multiple
        async coroutines concurrently.
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
        url_dict = {'ability': self.create_ability,
                    'move': self.create_move}
        if self.mode == 'pokemon':
            return await self.create_pokemon(response, expanded)
        else:
            return url_dict[self.mode](response)

    def create_move(self, response):
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
        async with aiohttp.ClientSession() as session:
            response = \
                await session.request(method="GET", url=target_url)
            json_dict = await response.json()
            return json_dict


