import aiohttp
import asyncio


class Move:

    def __init__(self, name, id, generation, accuracy, pp,
                 power, type, damage_class, effect_entries):

        self.name = name
        self.id = id
        self.generation = generation
        self.accuracy = accuracy
        self.pp = pp
        self.power = power
        self.type = type
        self.damage_class = damage_class
        self.effect = effect_entries

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Id: {self.id}\n" \
               f"Generation: {self.generation}\n" \
               f"Accuracy: {self.accuracy}\n" \
               f"PP: {self.pp}\n" \
               f"Power: {self.power}\n" \
               f"Type: {self.type}\n" \
               f"Damage Class: {self.damage_class}\n" \
               f"Effect: {self.effect}\n"


class Ability:

    def __init__(self, name, id, generation, effect, effect_short,
                 pokemon):

        self.name = name
        self.id = id
        self.generation = generation
        self.effect = effect
        self.effect_short = effect_short
        self.pokemon = pokemon

    def __str__(self):
        to_string = f"Name: {self.name}\n" \
               f"Id: {self.id}\n" \
               f"Generation: {self.generation}\n" \
               f"Effect: {self.effect}\n" \
               f"Effect Short: {self.effect_short}\n" \
               f"Pokemon: {', '.join(self.pokemon)}\n"

        return to_string


class Pokemon:

    def __init__(self, name, id, height, weight,
                 stats, types, abilities, moves):

        self.name = name
        self.id = id
        self.height = height
        self.weight = weight
        self.stats = stats
        self.types = types
        self.abilities = abilities
        self.moves = moves

    def __str__(self):
        to_string =  f"Name: {self.name}\n" \
               f"Id: {self.id}\n" \
               f"Height: {self.height} decimeters\n" \
               f"Weight: {self.weight} hectograms\n" \
               f"Stats:"

        for stat in self.stats:
            to_string += f'\n~ {stat}'

        to_string += f"\nTypes: {', '.join(self.types)}"

        to_string += '\nAbilities:'

        for ability in self.abilities:
            to_string += f'\n~ {ability}'

        to_string += '\nMoves:'

        for move in self.moves:
            to_string += f'\n~ {move}'

        return to_string



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
            if query == '?': raise Exception
            json_dict = await response.json()
        except Exception:
            return f"Error. No data exists for " \
                            f"the query: {query}"
        else:
            return json_dict

    async def process_single_request(self, query) -> Move:
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
                poke_object = self.create_poke_object(response)
            except Exception:
                return response
            return poke_object

    async def process_multiple_requests(self, requests: list) -> list:
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
                    poke_object = self.create_poke_object(response)
                except Exception:
                    poke_objects.append(response)
                else:
                    poke_objects.append(poke_object)
            return poke_objects

    def create_poke_object(self, response):
        url_dict = {'pokemon': self.create_pokemon,
                    'ability': self.create_ability,
                    'move': self.create_move}
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

    def create_pokemon(self, response):

        moves_list = \
            [element['move']['name'] for element in
             response['moves']]

        abilities_list = \
            [element['ability']['name'] for element in
             response['abilities']]

        types_list = \
            [element['type']['name'] for element in
             response['types']]

        stats_list = \
            [element['stat']['name'] for element in
             response['stats']]

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


def main():
    pass


if __name__ == '__main__':
    main()

