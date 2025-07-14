import random

suits = ['Hearts','Diamonds','Clubs','Spades']
ranks = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
    def __str__(self):
        return f"{self.rank} of {self.suit} "

class Deck:
    def __init__(self):
        self.cards = [Card(rank,suit) for suit in suits for rank in ranks]
        random.shuffle(self.cards)
    def deal_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.total = 0
        self.aces = 0
    def add_card(self,card):
        self.cards.append(card)
        self.total += card.value
        if card.rank == 'Ace':
            self.aces += 1
        self.adjust_for_ace()
    def adjust_for_ace(self):
        while self.total > 21 and self.aces:
            self.total -= 10
            self.aces -=1
    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

def show_some(player,dealer):
    print("\nDealer's Hand: <hidden> ,",dealer.cards[1])
    print("Your Hand: ",player)

def show_all(player,dealer): 
    print("\nDealer's Hand: ",dealer)
    print("Dealer's Total: ", dealer.total)
    print("Your Hand: ",player)
    print("Your Total: ",player.total)

def check_winner(player,dealer):
    if player.total > 21:
        return "You bust! Dealer wins"
    elif dealer.total > 21:
        return "Dealer busts! You win"
    elif player.total > dealer.total:
        return "You win!"
    elif dealer.total > player.total:
        return "Dealer wins!"
    else:
        return "Draw!"

def play_game():
    while True:
        print("\n-----------BLACKJACK GAME-----------")
        deck = Deck()
        player = Hand()
        dealer = Hand()

        player.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())

        show_some(player,dealer)

        while player.total < 21:
            move = input("\nDo you want to hit or stand? (h/s): ").lower()
            if move == 'h':
                player.add_card(deck.deal_card())
                print("Your Hand: ",player)
                print("Your Total: ",player.total)
            else:
                break
        
        while dealer.total < 17:
            dealer.add_card(deck.deal_card())
        
        show_all(player,dealer)
        print(check_winner(player,dealer))

        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing")
            break

play_game()