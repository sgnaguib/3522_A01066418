This program allows a user to build a custom pizza.

A user starts off with a plain pizza. This pizza has a cost (4.99) and a 
list of one ingredient (Signature Crust). When the user opts to 
add a cheese, a kind of cheese pizza is a wrapped around the plain pizza.
This cheese pizza takes the a pizza as its parameter. Its cost 
is the pizza argument's cost plus its own price. Similarly, its 
ingredients list is the cheese (i.e. Vegan cheese ) 
appended to the argument's ingredients list. An analogus process 
occurs when a user opts to add a topping.

When the user opts to checkout, a list is printed of the ingredient
list of the resulting pizza, alongside the price of each ingredient,
which is fetched from class corresponding to that ingredient.

This program uses two external modules: pretty table and menu.

In the run configuration, 
TERM variable TERM needs to be added and set to xterm-color 
to remove TERM variable error message.

As far as I know, all the required functionalities work properly.