"""
This module contains all the poke_objects
"""


class Move:
    """Represents a pokemon move."""

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
        return f"Move: {self.name}, " \
               f"Id: {self.id}, " \
               f"Generation: {self.generation}, " \
               f"Accuracy: {self.accuracy}, " \
               f"PP: {self.pp}, " \
               f"Power: {self.power}, " \
               f"Type: {self.type}, " \
               f"Damage Class: {self.damage_class}\n" \
               f"Effect: {self.effect}\n"


class Ability:
    """
    Represents a pokemon ability.
    """
    def __init__(self, name, id, generation, effect, effect_short,
                 pokemon):

        self.name = name
        self.id = id
        self.generation = generation
        self.effect = effect
        self.effect_short = effect_short
        self.pokemon = pokemon

    def __str__(self):
        to_string = f"Ability: {self.name}, " \
               f"Id: {self.id}, " \
               f"Generation: {self.generation}\n" \
               f"Effect: {self.effect}\n" \
               f"Effect Short: {self.effect_short}\n" \
               f"Pokemon: {', '.join(self.pokemon)}\n"

        return to_string


class Pokemon:
    """
    Represents a pokemon.
    """

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


class Stat:
    """
    Represents the statistics of a pokemon
    """

    def __init__(self, name, base_value, expanded,
                 _id=None, is_battle_only=None):
        self.name = name
        self._id = _id
        self.base_value = base_value
        self.is_battle_only = is_battle_only
        self.expanded = expanded

    def __str__(self):
        if self.expanded:
            return f'Stat: {self.name}, ID: {self._id}, ' \
                   f'Base Value: {self.base_value}, ' \
                   f'Battle Only: {self.is_battle_only}'
        else:
            return f'Stat: {self.name}, Base Value: {self.base_value}'
