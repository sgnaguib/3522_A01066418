"""
This module makes use of the Abstract Factory Pattern for a factory
that needs to make different types of garments for specific brands.
"""
import abc
import random
import enum


class ShirtMen(abc.ABC):
    """
    ShirtMen defines the interface for one of the garments that the
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

    def __init__(self, sport, number_pockets, **kwargs):
        super().__init__(**kwargs)
        self.sport = sport
        self.number_pockets = number_pockets


class ShirtMenPineappleRepublic(ShirtMen):

    def __init__(self, requires_iron, number_buttons, **kwargs):
        super().__init__(**kwargs)
        self.requires_iron = requires_iron
        self.number_buttons = number_buttons


class ShirtMenNika(ShirtMen):

    def __init__(self, indoor_outdoor_type, **kwargs):
        super().__init__(**kwargs)
        self.indoor_outdoor_type = indoor_outdoor_type


class ShirtWomen(abc.ABC):
    """
    ShirtWomen defines the interface for one of the garments that the
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

    def __init__(self, sport, number_pockets, **kwargs):
        super().__init__(**kwargs)
        self.sport = sport
        self.number_pockets = number_pockets


class ShirtWomenPineappleRepublic(ShirtWomen):

    def __init__(self, requires_iron, number_buttons, **kwargs):
        super().__init__(**kwargs)
        self.requires_iron = requires_iron
        self.number_buttons = number_buttons


class ShirtWomenNika(ShirtWomen):

    def __init__(self, indoor_outdoor_type, **kwargs):
        super().__init__(**kwargs)
        self.indoor_outdoor_type = indoor_outdoor_type


class SockPairUnisex(abc.ABC):
    """
    SockPairUnisex defines the interface for one of the garments that
    the abstract factory pattern is responsible to create.
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

    def __init__(self, contains_silver, contrast_colour, **kwargs):
        super().__init__(**kwargs)
        self.contains_silver = contains_silver
        self.contrast_colour = contrast_colour


class SockPairUnisexPineappleRepublic(SockPairUnisex):

    def __init__(self, requires_dry_cleaning, **kwargs):
        super().__init__(**kwargs)
        self.requires_dry_cleaning = requires_dry_cleaning


class SockPairUnisexNika(SockPairUnisex):

    def __init__(self, is_articulated, length, **kwargs):
        super().__init__(**kwargs)
        self.is_articulated = is_articulated
        self.length = length


class BrandFactory(abc.ABC):
    """
    The base factory class. All specific brand factories expect this
    factory class. The BrandFactory class defines an interface
    to create the a Product family consisting of men's
    shirts, women's shirts and unisex socks . These vary by brand.
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
    This LuluLimeFacotry class implements the BrandFactory Interface.
    It returns garments of made according to the specifics of LuluLime.
    """

    def create_shirt_men(self, **kwargs) -> ShirtMen:
        return ShirtMenLuluLime(**kwargs)

    def create_shirt_women(self, **kwargs) -> ShirtWomen:
        return ShirtWomenLuluLime(**kwargs)

    def create_socks_unisex(self, **kwargs) -> SockPairUnisex:
        return SockPairUnisexLuluLime(**kwargs)


class PineappleRepublicFactory(BrandFactory):
    """
    This PineappleRepublicFactory class implements the BrandFactory
    Interface.It returns garments of made according to the specifics of
    PineappleRepublic
    """

    def create_shirt_men(self, **kwargs) -> ShirtMen:
        return ShirtMenPineappleRepublic(**kwargs)

    def create_shirt_women(self, **kwargs) -> ShirtWomen:
        return ShirtWomenPineappleRepublic(**kwargs)

    def create_socks_unisex(self, **kwargs) -> SockPairUnisex:
        return SockPairUnisexPineappleRepublic(**kwargs)


class NikaFactory(BrandFactory):
    """
    This NikaFactory class implements the BrandFactory Interface.
    It returns garments of made according to the specifics of Nika.
    """

    def create_shirt_men(self, **kwargs) -> ShirtMen:
        return ShirtMenNika(**kwargs)

    def create_shirt_women(self, **kwargs) -> ShirtWomen:
        return ShirtWomenNika(**kwargs)

    def create_socks_unisex(self, **kwargs) -> SockPairUnisex:
        return SockPairUnisexNika(**kwargs)








