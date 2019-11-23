This program takes in an excel spreadsheet specified by the user, and 
"creates" garments based on the order specifications outlined in the 
excel spreadsheet. 

This program is divided in two modules: 

1) GarmentFactory.py which implements
the abstract factory pattern to create different brands of garments

2) BusinessLogic.py which handles extracting the necessary information 
from the excel spreadsheet to pass on the the garment factories so they
can create the garments.

On the business Logic side, the Order class
packages all the information in one 
row of the excel spreadsheet as an Order object.

The OrderProcessor class is responsible
for opening the excel file and creating Orders objects based on the
excel rows.

The GarmentMaker class is responsible for getting the orders from the
OrderProcessors and passing the order details to the appropriate
BrandFactory. Each order has an attribute "kw_details". These details
get passed to the factory and using those kwargs, the factory creates
the appropriate garment. For example, a if the kw_args indicate that
the garment is a lululime's men's shirt, the GarmentMaker class calls
the LuluLimeFactory class, which calls its create luluLimeMenShirt method.

Q1: To add a fourth brand, Goosie, with shirts and socks, I would just
need add the following to the GarmentFactory module:

add a GoosieFactory() class that implements the BrandFactoryClass

add ShirtMenGoosie, ShirtWomenGoosie, SocksPairUnisexGoose classes
that implement from ShirtMen, ShirtWomen and SocksPairUnisex respectively
and add any necessary attributes to them as specified by the manufacturer.

Q2:
To add a women's activewear garment to each of the three brands,
all I would have to do is create a ActiveWearWomen base class and then
create child classes for each Brand, ex. ActiveWearWomenNika. The
BrandFactory interface and its implementations
would all also need an extra method, create_activewear_women().


