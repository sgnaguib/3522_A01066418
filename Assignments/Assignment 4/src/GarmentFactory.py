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
    def __init__(self, style, size, colour, textile, garment_type,
                 **kwargs):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile
        self.garment_type = garment_type

    def __str__(self):
        return f"Size: {self.size}, Colour: {self.colour}, " \
               f"Textile: {self.textile}, Serial #: {id(self)}"


class ShirtMenLuluLime(ShirtMen):
    """
    MerPerson is a type of Friendly usually found in the Aquatica World.
    """

    def __init__(self, sport, number_pockets, **kwargs):
        super().__init__(**kwargs)
        self.sport = sport
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
    def __init__(self, style, size, colour, textile, garment_type,
                 **kwargs):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile
        self.garment_type = garment_type

    def __str__(self):
        return f"Size: {self.size}, Colour: {self.colour}, " \
               f"Textile: {self.textile}, Serial #: {id(self)}"


class ShirtWomenLuluLime(ShirtWomen):
    """
    MerPerson is a type of Friendly usually found in the Aquatica World.
    """

    def __init__(self, sport, number_pockets, **kwargs):
        super().__init__(**kwargs)
        self.sport = sport
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
    def __init__(self, style, size, colour, textile, garment_type,
                 **kwargs):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile
        self.garment_type = garment_type

    def __str__(self):
        return f"Size: {self.size}, Colour: {self.colour}, " \
               f"Textile: {self.textile}, Serial #: {id(self)}"


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
    def create_shirt_men(self, **kwargs) -> ShirtMen:
        pass

    @abc.abstractmethod
    def create_shirt_women(self, **kwargs) -> ShirtWomen:
        pass

    @abc.abstractmethod
    def create_socks_unisex(self, **kwargs) -> SockPairUnisex:
        pass


class LuluLimeFactory(BrandFactory):
    """
    This factory class implements the CharacterFactory Interface. It
    returns a product family consisting of MerPersons, Krakens, and
    Jellyfish.
    """

    def create_shirt_men(self, **kwargs) -> ShirtMen:
        return ShirtMenLuluLime(**kwargs)

    def create_shirt_women(self, **kwargs) -> ShirtWomen:
        return ShirtWomenLuluLime(**kwargs)

    def create_socks_unisex(self, **kwargs) -> SockPairUnisex:
        return SockPairUnisexLuluLime(**kwargs)


class PineappleRepublicFactory(BrandFactory):
    """
    This factory class implements the CharacterFactory Interface. It
    returns a product family consisting of FireSprites, Imps and
    Fireflies
    """

    def create_shirt_men(self, **kwargs) -> ShirtMen:
        return ShirtMenPineappleRepublic(**kwargs)

    def create_shirt_women(self, **kwargs) -> ShirtWomen:
        return ShirtWomenPineappleRepublic(**kwargs)

    def create_socks_unisex(self, **kwargs) -> SockPairUnisex:
        return SockPairUnisexPineappleRepublic(**kwargs)


class NikaFactory(BrandFactory):
    """
    This factory class implements the CharacterFactory Interface. It
    returns a product family consisting of FireSprites, Imps and
    Fireflies
    """

    def create_shirt_men(self, **kwargs) -> ShirtMen:
        return ShirtMenNika(**kwargs)

    def create_shirt_women(self, **kwargs) -> ShirtWomen:
        return ShirtWomenNika(**kwargs)

    def create_socks_unisex(self, **kwargs) -> SockPairUnisex:
        return SockPairUnisexNika(**kwargs)








