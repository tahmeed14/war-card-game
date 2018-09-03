import random
import unittest

# NAME: Tahmeed R. Tureen
# Course: SI 206
# Sec: Friday 1-2PM with Mauli Pandey
# Collaborated with: None

class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison 

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)

class Deck(object):
	def __init__(self): # Don't need any input to create a deck of cards
		# This working depends on Card class existing above
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card) # appends in a sorted order

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	def pop_card(self, i=-1):
		# removes and returns a card from the Deck
		# default is the last card in the Deck
		return self.cards.pop(i) # this card is no longer in the deck -- taken off

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = []
		for c in self.cards:
			card_strs.append(c.__str__())
		if card.__str__() not in card_strs:
			self.cards.append(card)

	def sort_cards(self):
		# Basically, remake the deck in a sorted way
		# This is assuming you cannot have more than the normal 52 cars in a deck
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)


# Class Hand: Represents a hand of cards for a game, with basic functionality
# Functionality available: Number of cards attribute
# Methods: Can place a card out of the hand, add a card to the hand that is not a duplicate, find all suits available, find all ranks available, look for a specific card in the hand and return it if there
class Hand(object): 
	def __init__(self,deck_to_use,num_cards=5): # Constructor
		self.deck = deck_to_use # Needs a deck
		self.cards_in_hand = [] 
		for i in range(num_cards):
			self.cards_in_hand.append(self.deck.pop_card(-1))

	def place_card(self,i=0):
		return self.cards_in_hand.pop(i) # Basically the same as pop_card from the deck, but referencing the HAND's cards

	def get_suits_available(self): # Returns list of all the suits that are in the hand
		suits = []
		for c in self.cards_in_hand:
			if c.suit not in suits:
				suits.append(c.suit)
		return suits

	def get_ranks_available(self): # Returns list of all the ranks that are in the hand
		ranks = []
		for c in self.cards_in_hand:
			if c.rank not in ranks:
				ranks.append(c.rank)
		return ranks

	def specific_card(self,suit,rank):
		card_strs = []
		ind = 0
		for c in self.cards_in_hand:
			if c.suit == suit and c.rank == rank:
				return self.place_card(ind) # If find the card in the hand, get rid of that card from the hand and return it from this method
			ind = ind + 1
		return None # if there is none such card in the hand, return None value
		
	def add_card(self,card): # add card to hand (if there is no identical one, assuming working with 1 deck here)
		card_strs = []
		for c in self.cards_in_hand:
			card_strs.append(c.__str__())
		if card.__str__() not in card_strs:
			self.cards_in_hand.append(card)

	def __str__(self):
		total = []
		for card in self.cards_in_hand:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

#### Functions for games ####

# Function that plays an altered version of the game of War when invoked.
def play_war_game(testing=False):
	player1 = Deck()
	player2 = Deck()

	p1_score = 0
	p2_score = 0

	player1.shuffle()
	player2.shuffle()
	if not testing:
		print("\n*** BEGIN THE GAME ***\n")
	for i in range(52):
		p1_card = player1.pop_card()
		p2_card = player2.pop_card()
		if not testing:
			print("Player 1 plays", p1_card,"& Player 2 plays", p2_card)

		if p1_card.rank_num > p2_card.rank_num:
			if not testing:
				print("Player 1 wins a point!")
			p1_score += 1
		elif p1_card.rank_num < p2_card.rank_num:
			if not testing:
				print("Player 2 wins a point!")
			p2_score += 1
		else:
			if not testing:
				print("Tie. Next turn.")

	if p1_score > p2_score:
		return "Player1", p1_score, p2_score
	elif p2_score > p1_score:
		return "Player2", p1_score, p2_score
	else:
		return "Tie", p1_score, p2_score

## Below this line, indented beneath it, goes function invocations, any code you want to run when you run this file.
if __name__ == "__main__":

	print("Test code here!\n")
	## The following is code to try out functionality of the class Hand. Uncomment the following lines to try it out. Note that each line depends on the former lines!

	deck_to_play = Deck() # Create a deck
	deck_to_play.shuffle() # Shuffle the deck!
	single_hand = Hand(deck_to_play,num_cards=5) # Deal one hand of 5 cards
	print(single_hand) # Print the hand to view it
	print("\n\n\n") # Print new lines, just for clarity


########### TESTS SHOULD GO BELOW THIS LINE ###########

# INCLUDE YOUR TESTS FROM HW2 HERE.

## TEST FOR CARD & DECK CLASS ****************************************************************
class TestCardsCode(unittest.TestCase):
## Test that if you create a card with rank 12, its rank will be "Queen"

	def test_queen(self):
		queen_test = Card(0,12)
		self.assertEqual(queen_test.rank, 'Queen')

## Test that if you create a card with rank 1, its rank will be "Ace"

	def test_ace(self):
		ace_test = Card(0,1)
		self.assertEqual(ace_test.rank, 'Ace')
 
## Test that if you create a card instance with rank 3, its rank will be 3
	
	def test_3(self):
		three_test = Card(0,3)
		self.assertEqual(three_test.rank, 3)

## Test that if you create a card instance with suit 1, it will be suit "Clubs"

	def test_clubs(self):
		clubs_test = Card(1,1)
		self.assertEqual(clubs_test.suit, 'Clubs')

## Test that if you create a card instance with suit 2, it will be suit "Hearts"

	def test_hearts(self):
		love_test = Card(2,1)
		self.assertEqual(love_test.suit, 'Hearts')

## Test that if you create a card instance, it will have access to a variable suit_names that contains the list ["Diamonds","Clubs","Hearts","Spades"]
	
	def test_suit_names(self):
		card_instance1 = Card() # no need for parameters
		
		self.assertEqual(card_instance1.suit_names, ["Diamonds","Clubs","Hearts","Spades"])

## Test that if you invoke the __str__ method of a card instance that is created with suit=2, rank=7, it returns the string "7 of Hearts"
	
	def test_str_method(self):

		invoke_strTest = Card(2,7)
		self.assertEqual(invoke_strTest.__str__() , "7 of Hearts")
		
## Test that if you create a deck instance, it will have 52 cards in its cards instance variable

	def test_52cards(self):

		deck_instance_test = Deck()
		deck_instance_test.cards
		num_cards = 0

		for i in deck_instance_test.cards:
			num_cards = num_cards + 1

		self.assertEqual(num_cards, 52)


## Test that if you invoke the pop_card method on a deck, it will return a card instance.
	
	def test_pop_card(self):
		deck1 = Deck()
		x = Card() # a card instance
		self.assertEqual(type(deck1.pop_card()) , type(x))


## Test that the return value of the play_war_game function is a tuple with three elements, the first of which is a string. 
## (This will probably require multiple test methods!)
	
	def test_play_war_game(self):
		x = len(play_war_game(testing=True))
		
		y = play_war_game(testing=True)

		self.assertEqual(type(y), type((1,"Jim Harbaugh", True)) ) #testing that the return value is a tuple itself
		self.assertEqual(x, 3) #testing the size of the tuple, which should be 3
		self.assertEqual(type(y[0]), type("HAIL TO THE VICTORS VALIANT")) #Index zero refers to the first element in the tuple which is compared to a string


## Write at least 2 additional tests (not repeats of the above described tests). Make sure to include a descriptive message in these two so we can easily see what you are testing!


#The following test will check whether the shuffle method in the Deck class will actually shuffle the deck.
#In other words, the deck will be arranged differently from when it was created. We can check this because when a deck is created it is initially sorted.

	def test_shuffle_deck(self):
		deck1 = Deck() #Note that the deck is sorted/ordered correctly when it is first created. **Checked by printing deck1 multiple times**
		deck1.shuffle()
		sorted_deck = Deck()
		
		self.assertNotEqual(str(deck1), str(sorted_deck)) #deck1 should NOT be the same as sorted_deck since deck1 was shuffled

#The following test will check whether the sort_cards method actually sorts a shuffled deck. Similar to the test above, we compare our sorted deck with an initialized deck since it is already sorted.
	
	def test_sort_decks(self):
		mydeck1 = Deck() #Note that deck is sorted when it is first created
		mydeck1.shuffle() #The shuffle method will shuffle mydeck1. **shuffle has been tested earlier
		mydeck1.sort_cards()

		initial_deck = Deck() #Again, this is sorted in the correct order

		self.assertEqual(str(mydeck1), str(initial_deck)) # mydeck1 should be the same as initial_deck since they are both sorted/ordered correctly


## TEST FOR HAND CLASS *********************************************************************
## Add tests, as described in instructions.
## Here is a sample.
class HandClassTests(unittest.TestCase):

# 0 GIVEN FROM INSTRUCTORS
# The following test will check whether the add_card function actually adds one more card to the hand. We check by seeing how many cards are in the hand 
# after the method is invoked

	def test_add_card(self):
		d = Deck()
		h = Hand(d) # default number of cards
		num = len(h.cards_in_hand) # length of the cards list in the hand
		new_card = d.pop_card() # pop another card off the deck
		h.add_card(new_card) # invoke add_card method with the card that we popped off the deck
		self.assertEqual(len(h.cards_in_hand),num+1) # Testing that the new number of cards in the hand is equal to the old number plus 1
	
	# Add more here!

# 1 The following test will check whether the functions get_suits_available and get_ranks_available return type list
	def test_suitsANDranks_available(self):
		x = ["alpha","beta,","gamma"] #This will be our variable that we compare the functions to

		random_deck = Deck()
		random_deck.shuffle() #shuffles the deck to randomize it
		our_hand = Hand(random_deck) 

		suits_available1 = our_hand.get_suits_available()
		ranks_available1 = our_hand.get_ranks_available()


		self.assertEqual(type(suits_available1), type(x), "the suits function did not work")
		self.assertEqual(type(ranks_available1), type(x), "the ranks function did not work")

# 2 The following test will check if the Hand class constructor creates a hand with the correct number of cards as the input-ted parameter
	def test_hand_correct_num(self):
		random_deck = Deck()
		random_deck.shuffle()

		our_hand1 = Hand(random_deck, 5)
		our_hand2 = Hand(random_deck,10)
		our_hand3 = Hand(random_deck, 1)
		our_hand4 = Hand(random_deck, 0)
		our_hand5 = Hand(Deck(), 52)


		self.assertEqual(len(our_hand1.cards_in_hand), 5)
		self.assertEqual(len(our_hand2.cards_in_hand), 10)
		self.assertEqual(len(our_hand3.cards_in_hand), 1)
		self.assertEqual(len(our_hand4.cards_in_hand), 0)
		self.assertEqual(len(our_hand5.cards_in_hand), 52)

# 3 The following test will check whether the place_card method actually removes a card from the hand. We check this by testing whether the number of cards
# in the hand has decreased by 1

	def test_place_card(self):
		random_deck = Deck()
		random_deck.shuffle()

		#Test some different number hands
		our_hand1 = Hand(random_deck,5)
		our_hand2 = Hand(random_deck,7)
		our_hand3 = Hand(random_deck,26)

		num_hand_cards1 = len(our_hand1.cards_in_hand)
		num_hand_cards2 = len(our_hand2.cards_in_hand)
		num_hand_cards3 = len(our_hand3.cards_in_hand)

		our_hand1.place_card()
		our_hand2.place_card()
		our_hand3.place_card()

		self.assertEqual(len(our_hand1.cards_in_hand), num_hand_cards1 - 1)
		self.assertEqual(len(our_hand2.cards_in_hand), 6)                   #Simply testing whether this format works also
		self.assertEqual(len(our_hand3.cards_in_hand), num_hand_cards3 - 1)

# 4 The following test will check whether the appended element by the add_card method appends an element of the type card

	def test_add_cardtype(self):
		normaldeck = Deck()
		empty_hand = Hand(normaldeck, 0) #We tested that this works on test_hand_correct_num
		random_card = Card() # The arguments for Card() are the default values of 0,2
		empty_hand.add_card(random_card) #The hand will now have 1 card

		self.assertEqual(type(empty_hand.cards_in_hand[0]), type(Card())) #Index will be 0 because there is only one element in the list now

# 5 The following test will check whether the specific_card method returns None if the specific card is not in the hand and returns the specific card if
# the card is in the hand...

	def test_specific_card(self):
		normaldeck = Deck()
		bigHAND = Hand(normaldeck, 52)
		x = bigHAND.specific_card(suit = "Hearts", rank = 5)      #The inputed parameters must be of this form
		y = bigHAND.specific_card(suit = "Clubs", rank = "Queen")
		y1 = bigHAND.specific_card(suit= "Spades", rank = "Ace")


		empty_hand = Hand(Deck(),0)
		z = empty_hand.specific_card(suit = "Spades", rank = "Ace")

		self.assertEqual(x.suit, "Hearts")
		self.assertEqual(x.rank, 5)

		self.assertEqual(y.suit, "Clubs")
		self.assertEqual(y.rank, "Queen") # The ranks of face cards are strings, not integer types

		self.assertEqual(y1.suit, "Spades")
		self.assertEqual(y1.rank, "Ace")

		self.assertEqual(z, None) #Should return None since hand is empty

# 6 The following test will check when multiple hands are created from one single deck, the deck will have lesser and lesser cards each time since the
# pop card method is invoked
	
	def test_remaining_cards(self):
		normaldeck = Deck()
		randomhand = Hand(normaldeck,7)
		x = len(normaldeck.cards)
		self.assertEqual(x,45)

		randomhand2 = Hand(normaldeck) # Since the normalized hand size is 5, this will create a hand of 5 cards
		y = len(normaldeck.cards)
		self.assertEqual(y,40)

		randomhand3 = Hand(normaldeck,40)
		z = len(normaldeck.cards)
		self.assertEqual(z, 0)

# 7 The following test will check whether the get_suits and get_ranks method will have all four suits and all 13 ranks listed if 
# used on a hand with all 52 cards, meaning they have all of the suits and all of the ranks

	def test_getsuitsANDranks_all(self):
		normaldeck = Deck()
		bigHAND = Hand(normaldeck,52)
		
		self.assertEqual(bigHAND.get_suits_available(), ['Spades', 'Hearts', 'Clubs', 'Diamonds']) # the order should be in this format
		self.assertEqual(bigHAND.get_ranks_available(), ['King', 'Queen', 'Jack', 10, 9, 8, 7, 6, 5, 4, 3, 2, 'Ace']) # the order should be in this format

# 8 The following test will check whether every element of the returned list by the get_suits method will be type string
	
	def test_getsuits_alltypeString(self):
		normaldeck = Deck()
		bigHAND = Hand(normaldeck,52)

		suits_list = bigHAND.get_suits_available()

		for i in suits_list:
			
			self.assertEqual(type(i), type("Tom Brady will be SUPERBOWL MVP")) #the types of the elements will have to be strings


## Hints to help come up with tests:
## - Create a Deck instance in each method where you want to test an instance of class Hand, because you need a Deck instance to create a Hand instance!
## - To test the Hand constructor, you may want to test that the Hand class creates a hand with 3 cards if you pass in a Deck instance to the constructor, and use the default num_cards.
## - You should also test that if you pass in a specific number of cards to the Hand class constructor, it creates an instance of class Hand with that specific number of cards! Gotta be sure that part of the Hand class constructor (__init__ method) works correctly.


#############

unittest.main(verbosity=2) 