import random

# Data Structures for Suits, Ranks, and Values
suits = ["Spades", "Diamonds",  "Hearts", "Clubs"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King" ]
values = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10 }

# Define CLass Objects: Card, Deck, Player, and Hand
class Card: 
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

        def __str__(self):
            return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []

    def build(self):
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)
        print("The deck is shuffled.")

    def deal(self):
        return self.cards.pop()




class Player:
    def __init__(self, bank=100):
        self.bank = bank
        self.bet = 0
    
    def sub_bank(self, amount):
        self.bank -= amount
        self.bet += amount

    def add_bank(self):
        self.bank += self.bet * 2


class Hand:
    def __init__(self):
        self.hand = []
        self.value = 0

    def draw(self, card):
        self.hand.append(card)
        if (card.rank == "Ace" and self.value < 12):
            self.value += (values[card.rank] + 10)
        else:
            self.value += values[card.rank]

    def show(self):
        for card in self.hand:
            print(card)
    
    def __del__(self): 
        pass


    # Functions: win_check(), replay(), game_switch()

    def win_check():
        pass


    def replay():
        pass


    def game_switch():
        pass


    # Game State Variables



    # Game Loop