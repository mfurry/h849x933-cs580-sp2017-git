#Matthew Furry
#H849X933
#Psuedo code:
#init: initializes card with a rank and a suit
#getRank: returns the rank
#getSuit: returns the suit
#BJValue: returns the blackjack value of the card
#str: returns the card as a string
#draw: Displays the card in a window
#
#main:
#open window
#set coordinates for cards
#loop
# randomize values
# draw card

from graphics import *
from random import randint

class Card:

    def __init__(self, rank, suit):
        #Initializes card with a rank and a suit
        self.rank = rank
        self.suit = suit

    def getRank(self):
        #Returns the rank
        return self.rank

    def getSuit(self):
        #Returns the suit
        return self.suit

    def BJValue(self):
        #Returns the blackjack value of the card
        if self.rank < 11:
            return self.rank
        else:
            return 10

    def __str__(self):
        #Returns the card as a string
        if self.rank == 1:
            card = "Ace"
        elif self.rank == 11:
            card = "Jack"
        elif self.rank == 12:
            card = "Queen"
        elif self.rank == 13:
            card = "King"
        else:
            card = self.rank
        if self.suit == "c":
            suit = "clubs"
        elif self.suit == "s":
            suit = "spades"
        elif self.suit == "h":
            suit = "hearts"
        else:
            suit = "diamonds"
        return (card + "of" + suit)

    def draw(self, win, center):
        #Displays the card in a window
        if self.rank == 11:
            imgFile = self.suit + "j.png"
        elif self.rank == 12:
            imgFile = self.suit + "q.png"
        elif self.rank == 13:
            imgFile = self.suit + "k.png"
        else:
            imgFile = self.suit + str(self.rank) + ".png"
        cardImage = Image(center, imgFile)
        cardImage.draw(win)

def main():
    win = GraphWin("Cards", 600, 150)
    win.setCoords(0, 0, 6, 2)
    win.setBackground("dark green")

    for n in range(1,6): #Loop for 5 cards
        x = randint(1,4) #Random suit
        if x == 1:
            suit = "c"
        elif x == 2:
            suit = "s"
        elif x == 3:
            suit = "h"
        elif x == 4:
            suit = "d"
        card = Card(randint(1,13), suit)
        card.draw(win, Point(n,1))

main()
