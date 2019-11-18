"""
This module depicts the use of the Abstract Factory Pattern for a game
that needs groups of characters for different worlds.
"""
import abc
import random
import enum


class BrandEnum(enum.Enum):
    pass

class MenSizeEnum(enum.Enum):
    S = 0
    M = 1
    L = 2
    XL = 3
    XXL = 4

class WomenSizeEnum(enum.Enum):
    XS = 0
    S = 1
    M = 2
    L = 3
    XL = 4
    XXL = 5

class UnisexSocksEnum(enum.Enum):
    S = 0
    M = 1
    L = 2


class ShirtMen(abc.ABC):
    """
    Friendly defines the interface for one of the products that the
    abstract factory pattern is responsible to create.
    """
    @abc.abstractmethod
    def __init__(self, style, size, colour, textile):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile


class ShirtMenLuluLime(ShirtMen):
    """
    MerPerson is a type of Friendly usually found in the Aquatica World.
    """

    def __init__(self, design, number_pockets, **kwargs):
        super().__init__(**kwargs)
        self.design = design
        self.number_pockets = number_pockets


class ShirtMenPineappleRepublic(ShirtMen):
    """
    FireSprite is a type of Friendly usually found in the Firelands
    World.
    """

    def __init__(self, requires_iron, number_buttons, **kwargs):
        super().__init__(**kwargs)
        self.requires_iron = requires_iron
        self.number_buttons = number_buttons


class ShirtMenNika(ShirtMen):
    """
    FireSprite is a type of Friendly usually found in the Firelands
    World.
    """

    def __init__(self, indoor_outdoor_type, **kwargs):
        super().__init__(**kwargs)
        self.indoor_outdoor_type = indoor_outdoor_type


class ShirtWomen(abc.ABC):
    """
    Enemy defines the interface for one of the products that the
    abstract factory pattern is responsible to create.
    """

    @abc.abstractmethod
    def __init__(self, style, size, colour, textile):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile


class ShirtWomenLuluLime(ShirtWomen):
    """
    MerPerson is a type of Friendly usually found in the Aquatica World.
    """

    def __init__(self, design, number_pockets, **kwargs):
        super().__init__(**kwargs)
        self.design = design
        self.number_pockets = number_pockets


class ShirtWomenPineappleRepublic(ShirtWomen):
    """
    FireSprite is a type of Friendly usually found in the Firelands
    World.
    """

    def __init__(self, requires_iron, number_buttons, **kwargs):
        super().__init__(**kwargs)
        self.requires_iron = requires_iron
        self.number_buttons = number_buttons


class ShirtWomenNika(ShirtWomen):
    """
    FireSprite is a type of Friendly usually found in the Firelands
    World.
    """

    def __init__(self, indoor_outdoor_type, **kwargs):
        super().__init__(**kwargs)
        self.indoor_outdoor_type = indoor_outdoor_type


class SockPairUnisex(abc.ABC):
    """
    Animal defines the interface for one of the products that the
    abstract factory is responsible to create
    """

    @abc.abstractmethod
    def __init__(self, style, size, colour, textile):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile


class SockPairUnisexLuluLime(SockPairUnisex):
    """
    MerPerson is a type of Friendly usually found in the Aquatica World.
    """

    def __init__(self, contains_silver, contrast_colour, **kwargs):
        super().__init__(**kwargs)
        self.contains_silver = contains_silver
        self.contrast_colour = contrast_colour


class SockPairUnisexPineappleRepublic(SockPairUnisex):
    """
    FireSprite is a type of Friendly usually found in the Firelands
    World.
    """

    def __init__(self, requires_dry_cleaning, **kwargs):
        super().__init__(**kwargs)
        self.requires_dry_cleaning = requires_dry_cleaning

class SockPairUnisexNika(SockPairUnisex):
    """
    FireSprite is a type of Friendly usually found in the Firelands
    World.
    """

    def __init__(self, is_articulated, length, **kwargs):
        super().__init__(**kwargs)
        self.is_articulated = is_articulated
        self.length = length


class BrandFactory(abc.ABC):
    """
    The baase factory class. All worlds expect this factory class to
    populate the world. The CharacterFactory class defines an interface
    to create the a Product family consisting of Friendlies, Enemies,
    and Animals. These vary by world.
    """

    @abc.abstractmethod
    def create_shirt_men(self) -> ShirtMen:
        pass

    @abc.abstractmethod
    def create_shirt_women(self) -> ShirtWomen:
        pass

    @abc.abstractmethod
    def create_socks_unisex(self) -> SockPairUnisex:
        pass


class LuluLimeFactory(BrandFactory):
    """
    This factory class implements the CharacterFactory Interface. It
    returns a product family consisting of MerPersons, Krakens, and
    Jellyfish.
    """

    def create_shirt_men(self) -> ShirtMen:
        return ShirtMenLuluLime()

    def create_shirt_women(self) -> ShirtWomen:
        return ShirtWomenLuluLime()

    def create_socks_unisex(self) -> SockPairUnisex:
        return SockPairUnisexLuluLime()


class PineappleRepublicFactory(BrandFactory):
    """
    This factory class implements the CharacterFactory Interface. It
    returns a product family consisting of FireSprites, Imps and
    Fireflies
    """

    def create_shirt_men(self) -> ShirtMen:
        return ShirtMenPineappleRepublic()

    def create_shirt_women(self) -> ShirtWomen:
        return ShirtWomenPineappleRepublic()

    def create_socks_unisex(self) -> SockPairUnisex:
        return SockPairUnisexPineappleRepublic()


class NikaFactory(BrandFactory):
    """
    This factory class implements the CharacterFactory Interface. It
    returns a product family consisting of FireSprites, Imps and
    Fireflies
    """

    def create_shirt_men(self) -> ShirtMen:
        return ShirtMenNika()

    def create_shirt_women(self) -> ShirtWomen:
        return ShirtWomenNika()

    def create_socks_unisex(self) -> SockPairUnisex:
        return SockPairUnisexNika()


class WorldPopulator:
    """
    Maintains a mapping of world -> CharacterFactory. The WorldPopulator
    is responsible for retrieving the right factory for the specified
    world.
    """

    # Maps world types to their respective factories
    world_factory_mapper = {
        WorldEnum.AQUATICA : AquaticaCharacterFactory,
        WorldEnum.FIRELANDS : FirelandsCharacterFactory
    }

    def get_factory(self, world_type: WorldEnum) -> CharacterFactory:
        """
        Retrieves the associated factory for the specified WorldEnum
        :param world_type: WorldEnum
        :return: a CharacterFactory if found, None otherwise
        """
        factory_class = self.world_factory_mapper.get(world_type, None)
        return factory_class()


class World:
    """
    Defines a world that consists of fFriendlies, Enemies and Animals.
    Each world has a theme/variety.
    """

    def __init__(self, char_factory: CharacterFactory):
        """
        Instantiates a world with the specified character factory. The
        Character Factory specifies which type of characters inhabit
        this world.
        :param char_factory: a Character Factory
        """
        self.friendlies = []
        self.enemies = []
        self.animals = []
        self.world_populator_factory = char_factory

        for i in range(5):
            self.friendlies.append(self.world_populator_factory.create_friendly())

        for i in range(5):
            self.enemies.append(self.world_populator_factory.create_enemy())

        for i in range(5):
            self.animals.append(self.world_populator_factory.create_animal())

    def simulate(self):
        """
        Simulates behaviour of all the characters in this world.
        :return:
        """
        for friendly in self.friendlies:
            friendly.talk()

        for enemy in self.enemies:
            print(f"{enemy.name} tried to defend! Success: "
                  f"{enemy.defend()}")

        for animal in self.animals:
            animal.move()


def main():
    populator = WorldPopulator()
    aquatica_factory = populator.get_factory(WorldEnum.AQUATICA)
    aquatica = World(aquatica_factory)
    aquatica.simulate()


if __name__ == '__main__':
    main()





