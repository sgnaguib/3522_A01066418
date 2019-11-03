from pizza import *

cheese_dict = {'Parmigiano Reggiano': ParmigianoPizza,
               'Fresh Mozzarella': MozzarellaPizza,
               'Vegan Cheese': VeganCheesePizza}

for element in cheese_dict.items():
    print(element.key)
