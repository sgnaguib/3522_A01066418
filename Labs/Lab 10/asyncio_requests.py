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
               f"Generation: {self.id}\n" \
               f"Accuracy: {self.accuracy}\n" \
               f"PP: {self.pp}\n" \
               f"Power: {self.power}\n" \
               f"Type: {self.type}\n" \
               f"Damage Class: {self.damage_class}\n" \
               f"Effect: {self.effect}\n"





class RequestHandler:

    def __init__(self):
        self.url = "http://pokeapi.co/api/v2/move/{}/"

    async def get_moves_data(
            self, query, url: str, session: aiohttp.ClientSession) -> dict:
        """
        An async coroutine that executes GET http request. The response is
        converted to a json. The HTTP request and the json conversion are
        asynchronous processes that need to be awaited.
        :param id_: an int
        :param url: a string, the unformatted url (missing parameters)
        :param session: a HTTP session
        :return: a dict, json representation of response.
        """
        target_url = url.format(query)
        response = await session.request(method="GET", url=target_url)
        # print("Response object from aiohttep:\n", response)
        # print("Response object type:\n", type(response))
        json_dict = await response.json()
        return json_dict

    async def create_move(self):
        pass

    async def process_single_request(self, query) -> Move:
        """
        Thsi function depicts the use of await to showcase how one async
        coroutine can await another async coroutine
        :param id_: an int
        :return: dict, json response
        """
        async with aiohttp.ClientSession() as session:
            response = await self.get_moves_data(query, self.url, session)
            move = Move(response['name'],
                        response['id'],
                        response['generation'],
                        response['accuracy'],
                        response['pp'],
                        response['power'],
                        response['type']['name'],
                        response['damage_class']['name'],
                        response['effect_entries'][0]['short_effect'])

            return move


    async def process_requests(self, requests: list) -> list:
        """
        This function depicts the use of asyncio.gather to run multiple
        async coroutines concurrently.
        :param requests: a list of int's
        :return: list of dict, collection of response data from the endpoint.
        """
        async with aiohttp.ClientSession() as session:
            async_coroutines = [self.get_moves_data(query, self.url, session)
                                for query in requests]
            responses = await asyncio.gather(*async_coroutines)
            moves = []
            for response in responses:
                move = Move(response['name'],
                            response['id'],
                            response['generation'],
                            response['accuracy'],
                            response['pp'],
                            response['power'],
                            response['type']['name'],
                            response['damage_class']['name'],
                            response['effect_entries'][0][
                                'short_effect'])
                moves.append(move)
            return moves


def main():
    requests = [1, 2, 3]
    handler = RequestHandler()
    moves = asyncio.run(handler.process_requests(requests))
    for move in moves:
        print(move)
    print("-"*80)
    #response2 = asyncio.run(handler.process_single_request(1))
    #print(response2)


if __name__ == '__main__':
    main()

