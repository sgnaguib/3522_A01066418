First off, I imported a module from pip called menu that help's
generate a text-based UI. There are 6 main menu options, View Cards,
Add Card, Search Card, Delete Card, Export Cards and Exit program.

When a user choose to add a card, the ui goes through the cardEnum
class to get the list of available card types. When the user
selects what type of card he or she wants, the ui asks the
card manager to return a dummy card of that type. The ui goes
through that dummy card, gets its attributes as a dictionary
and then prompts the user to input information for each attribute.

When the user selects the option to view the cards, the UI goes through
all the cards stored in the cardmanager and creates a menu option for
each card. When a user selects a card, the cards information is printed.

The search and delete functions work very similarly to each other.
The user inputs the name of card, and the ui asks the card manager
to find the card, if it is found, it is either returned and printed or
deleted.

When the user chooses to export a card, the cards are exported as a .txt
file, one line per card, with a filename as specified in the
assignment outline.

As far as I know, there are no basic functionalities that are missing
from this submission. I should point out though that I did not use
multiple inheritance.