import random

# Card
class Card:
    def __init__(self, val, suit):
        self.val = val
        self.suit = suit
        self.points = int

    def __str__(self):
        return self.val + " of " + self.suit

    def __repr__(self):
        return self.val + " of " + self.suit

deck = []
suits = [
    "Clubs",
    "Diamonds",
    "Hearts",
    "Spades"
]

values = [
    ("Ace", 11),
    ("Two", 2),
    ("Three", 3),
    ("Four", 4),
    ("Five", 5),
    ("Six", 6),
    ("Seven", 7),
    ("Eight", 8),
    ("Nine", 9),
    ("Ten", 10),
    ("Jack", 10),
    ("Queen", 10),
    ("King", 10)
]

for suit in suits:
    for value in values:
        new_card = Card(value[0], suit)
        new_card.points = value[1]
        deck.append(new_card)


# Deck
class Deck:
    def __init__(self):
        self.cards = deck

    # Give dealer their cards
    def dealer_cards(self, dealer):
        first_card = random.choice(self.cards)
        self.cards.remove(first_card)
        second_card = random.choice(self.cards)
        self.cards.remove(second_card)
        dealer.hand.append(first_card)
        dealer.hand.append(second_card)

    def deal(self, players):
        print("Dealing Cards...")
        for player in players:
            # First Card
            choice = random.choice(self.cards)
            self.cards.remove(choice)
            player.hand.append(choice)
            # Second Card
            choice = random.choice(self.cards)
            self.cards.remove(choice)
            player.hand.append(choice)

    def shuffle(self):
        self.cards = deck

    # Give player one card
    def hit(self, player):
        choice = random.choice(self.cards)
        self.cards.remove(choice)
        player.hand.append(choice)

    # Print out decks Cards and points
    def view_deck(self):
        for card in self.cards:
            print(card.val, card.points)

# test_deck = Deck()

# test_deck.view_deck()

