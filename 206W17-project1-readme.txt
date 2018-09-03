206 Project 1 - Code for playing cards

README



Your name:
 Tahmeed Tureen
Section: Fri 1-2PM with Mauli Pandey
Anyone you worked with: None



----- Add your README file content for the Project 1 code.



206W17-project1.py is a file that holds a collection of code that can be used to create a simulation of a card game with the traditional deck of cards
including four suits and 13 different ranks. The code is divided into three different classes: Card, Deck & Hand. The code also includes one function 
play_war_game which calls some of the methods & instances of the beforementioned classes to run the simulation of the war card game. The three classes 
can be used to create cards, decks, and hands which can be applied to different code for different card games. If you follow the simulation of the 
play_war_game you will get an example of how the different classes can be applied to create your own card game. Feel free to use the classes in any 
unique you may please! Have fun! 

Descriptions of each Class & Function are below:

1) Card()

The first class in the code is the Card class. The overall purpose of the Card class is to construct any single card from a traditional deck of 
cards. For example, "Queen of Hearts" , "Ace of Spades", "7 of Diamonds" etc.

An instance of the card class would be something like: x = Card(0,2) which is the card "2 of Diamonds"

	i) Three separate variables were defined before the constructor was defined.
		a) suit_names is a list with all of the names of the suits a traditional deck of cards has. ex: "Clubs", "Hearts"
		b) rank_levels is a list of integers ranging from 1 to 13, they represent the rank of the cards. ex: "1", "2", "7"
		c) faces is a dictionary that assigns the four specific ranks to the face cards of a traditional deck of cards. ex: "1 is Ace", "11 is Jack"

	ii) def __init__(self, suit=0,rank=2):
		The constructor of the Card class takes the default parameters of suit=0 and rank=2. The number 0 represents "Diamonds" and 2 represents
		2. These numbers are the indexes of the list variables suit_names & rank_levels. The constructor then systematically assigns the suit and
		rank to the newly generated card.
		For example: Card(1,12) will create the card "Queen of Clubs" and Card(0,2) will create the card "2 of Diamonds"
	
	iii) def __str__(self):
		This method simply returns a string the card constructed by the the Card class in the format of "Rank of Suit"
		For example: "Queen of Clubs"

2) Deck()

The second class in the code is the Deck class. The overall purpose of the Deck class is to construct a deck of 52 cards. The deck will have no repetition of
cards and will portray a traditional deck of cards with the four suits and 13 cards of varying rank for each suit.

An instance of the Deck class would be something like: y = Deck() which is a deck with all 52 cards sorted in an order unique to this code.
	
	i) def __init__(self):
		The constructor for the Deck class does not take any input. The constructor will create a list of all of the cards in a traditional card
		deck. The list is appended one card at a time in a sorted way. Here, the Card class is called to construct all of the cards which are to 
		be added to the list the constructor creates. The way the list is sorted is unique to this code and is not universal to card decks. If you
		wish to see the order, simply use this code print(Deck()).
	
	ii) def __str__(self): 
		This method returns a multi-line string of a deck. The code was written so that any deck could be printed with one card in one line instead
		of multiple cards in one line. For example:
		"King of Spades"
		"Queen of Spades"
		"Jack of Spades" and so on.

	iii) def pop_card(self, i=-1):
		This method takes integer inputs such as -1,0,1,2 etc. The inputted number is the index number of the list which the Deck constructor creates.
		The card at that particular index will be taken out of the deck and returned in this method. The default is the last card in the Deck. 

	iv) def shuffle(self):
		This method simply shuffles any Deck the method is invoked onto. The method does not require any input.

	v) def replace_card(self, card):
		This method requires an input of a Card variable. This method goes through a deck searching for the specific Card that was inputed and will 
		append it to the deck if that Card is not in the deck already. If the card is already in the deck, then the method will not add the card into
		the deck. 
		
	vi) def sort_cards(self):
		This method does not require any input. The method will sort any deck in the unique order which this code prefers. The decks on which this
		method is invoked should not contain more than 52 cards. This method actually remakes a new deck by first creating an empty list and appending
		the cards in a sorted manner. This method is useful if a deck was shuffled and needed to be sorted later. 


3) Hand()

The third class in the code is the Hand class. The overall purpose of the Hand class is to create a hand of cards like in a game of Poker or any other card
game. The hand can be created from a specific deck and can have any number of cards depending on how big the deck is. 

An instance of the Hand class would be something like: z = Hand(Deck(),5) which is a hand with 5 random cards. 

	i) def __init__(self,deck_to_use,num_cards=5):
		The constructor of the Hand class creates a list of cards which represents a hand of cards. The constructer requires inputs of a Deck and an
		integer number. The input Deck is the deck from which the hand will be created, the number represents how many cards the hand will hold. The
		number can not be less than 0 nor can it exceed the number of cards in the deck that is inputted. The default is set to 5. Since the pop_card
		method is invoked on the inputted Deck, the Deck size decreases with the number of cards in the hand. For example, if a hand was created with
		52 cards, then the inputted deck will 0 cards left. 
	
	ii) def place_card(self,i=0):
		This method returns a specific card from a hand. The method requires an input of an integer number. The number is the index of the list in
		a Hand variable, so the card at that particular index will be taken out of the hand since the pop_card method is invoked. The default number
		is 0, the initial card in the list of the Hand variable.

	iii) def get_suits_available(self)
		This metod returns a list of all the suits that are in the hand. For example, if a hand has 5 cards with only the Hearts suit then this method
		will return the list ["Hearts"]. If a hand has two suits, then it will return a list with two elements. The returned list will not exceed the length
		of four since there are only four distinct suits. The method iterates through the list in a Hand variable assessing what suits the hand has & then
		appends it to an empty list, which is then returned. The method does not require any input. If a hand has all four suits, it will return a list
		with this unique order: ['Spades', 'Hearts', 'Clubs', 'Diamonds']
	
	iv) def get_ranks_available(self):
		This method returns a list of all of the ranks that are in the hand. For example, if a hand has 3 cards with ranks 13,2,1 then this method will
		return the list ["King", 2, "Ace"]. If a rank has all of the ranks, then it will return the list ['King', 'Queen', 'Jack', 10, 9, 8, 7, 6, 5, 4, 3, 2, 'Ace']
		This method works in a similar manner as the get_suits_available method. Please, refer to that method's description for specifics. The method
		does not require any input.

	v) def specific_card(self,suit,rank):
		This method requires two inputs suit and rank. The input must be in this manner, .specific_card(suit="Clubs",rank=2) or .specific_card(suit="Clubs",rank="Ace")
		Otherwise the method will only return None. There is no default input. This method checks whether a hand has the specific card that was inputted. 
		For example, if the Ace of Clubs was inputed then the method iterates through the list of the Hand variable and checks if the card is in the list. 
		If it is, then it will return that specific card by invoking the place_card method (Refer to place_card description for clarification). If the 
		specific card is not in the hand, then the method will simply return None. 
	
	vi) def add_card(self,card): 
		This method takes one input of a Card variable. This method will iterate through the list of a Hand variable and assess whether the inputted card
		is in the hand or not. If it is not, then it will add it to the hand. If the card is already in the hand, then the method will not add the card to 
		the hand. The assumption is that there was only one deck that was used to create the hand. There is no default input for this method.

	vii) def __str__(self):
		This method returns a string of the cards in the hand. The format that this method follows is that one card will show up in one line. If there are
		5 cards, then the returned string will have 5 lines. There is no particular order. The returned string will be in the order in which the list of 
		the Hand variable is. For example, consider a hand of 4 cards.
		"Queen of Hearts"
		"Ace of Spades"
		"7 of Clubs"
		"Jack of Spades"

4) def play_war_game(testing=False):
	The code of this function runs the simulation of an altered version of the war card game. The parameter of the function has testing in it so that it can be
	tested. If it is called with the input "testing=False" then the game runs, if it is called with the input "testing=True" then the game can be used to test 
	the code inside the function instead.
 
	The function assigns two different players with two initial decks and assigns each of them with an intial score of 0. The decks are then shuffled before the
	"game" is run. The purpose of the game is to accumulate as many points as possible before the end of the game. The function goes through each player's deck one
	by one pulling one card from each. The cards are randomized since the decks were shuffled before. The function also prints out every card each player plays
	so that the viewer can see each play. During each turn, the function compares which player played a card with the higher rank. The player with the higher 
	rank receives one point to their score and the function prints out who won the point. If the ranks are the same, then the function prints out a message for 
	a tie and does not award either player points. Eventually, the function goes through both of the decks and compares the two scores of the players. The player
	with the highest score will be declared winner & if there was a tie then the function will declare a tie.

	This is just one example of how the classes: Card, Deck and Hand can be used to create a simulation of a card game. In this particular game the Hand class 
	was not used nor were all of the methods created used. It is up to you, the reader, to now use the classes to create your very own game or simply mirror a
	card game which you may love. Some examples to consider: Poker, Black Jack, Euchre etc.

Thank you for reading this documentation. I really hope that the you find the code & documentation helpful.

Note: This code was created in collaboration with the SI 206: "Data Oriented Programming" course within the School of Information at the University of Michigan. My
instructors are Jackie Cohen, Maulishree Pandey & Yu-Jen Lin. My responsibilites included writing this documentation as well as designing multiple test cases for 
the code.   
	


