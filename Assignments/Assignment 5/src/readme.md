This program runs through the command line. 

A user may use this program to query the PokeAPI for Pokemon,
Abilities or Moves.

The Pokedex object is the 'controller' of the program. It has an 
inputHandler object that parses the user's commandline input. When
the Pokedex creates a RequestHandler, it passes the mode of 
the request is: Pokemon, Ability or move.

The Pokedex takes the input from the InputHandler and passes it as a query 
to the a RequestHandler function. 
The RequestHandler function makes a request to the PokeAPI
based on the that query. 

The pokedex determines whether the input
is a single string or a list of strings and calls the RequestHandler's 
process_single_request or process_mulitple_requests accordingly. The 
Pokedex also tells the RequestHandler's function 
whether the user wants an expanded query or not. 

The requestHandler makes an HTTP request based on the query and
tries to create a poke_object according to the mode the user initially 
specified. It does so by parsing the response for attributes necessary to 
create the poke_object.

If the RequestHandler is creating a pokemon object and the 
request is in expanded mode, it parses the url from the 
initial query and sends a new request to the PokeAPI with that url.

The Pokemon object has an attribute expanded and its __str__() function
returns different results based on the value of that attribute.

If the initial query was invalid, the poke_object will not be made and the requestHandler
will return that the query as invalid.

If the creation of the poke_object(s) was successful, the requestHandler
returns the poke_object(s) to the Pokedex. 

The Pokedex prints the result either to the console or a .txt file 
based on the output attribute of its InputHandler.