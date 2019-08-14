import matplotlib.pyplot as mpplot
import matplotlib.image as mpimg
import os
import random

class Card():
    VALUES = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]

    SUITS = ["hearts", "clubs", "diamonds", "spades"]

    def __init__(self, value, suit):
        self.__value = value
        self.__suit = suit

    def __str__(self):
        return f"{self.__value} of {self.__suit}"

    @property
    def image_name(self):
        return f"{self.__value}_of{self.__suit}.svg.png"


class CardDeck():

    def __init__(self):
        self.__deck = []
        self.__card_index = 0
        for value in Card.VALUES:
            for suit in Card.SUITS:
                self.__deck.append(Card(value, suit))
        self.__deck.append("joker")

    def card_count(self):
        return len(self.__deck)

    def __str__(self):
        return self.show_the_cards()

    def show_the_cards(self):
        returnstr = ""
        for card in self.__deck:
            returnstr += card.__str__() + "\n"
        return returnstr

    def hand_card(self):
        card_to_return = self.__deck[self.__card_index]
        self.__card_index += 1

    def print_card(self):
        for card in self.__deck:
            print(card.__str__())

    def shuffle(self):
        self.__card_index = 0
        random.shuffle(self.__deck)

deck_of_cards = CardDeck()
deck_of_cards.shuffle()
# print(deck_of_cards.get_card())
cards_to_deal = 5
figure, axes = mpplot.subplots(nrows=1, ncols=cards_to_deal)
for ax in axes.ravel():
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    img = mpimg.imread(str(os.path.join(os.getcwd(), "cards", deck_of_cards.hand_card().image_name)))
    ax.imshow(img)
figure.show()
figure.waitforbuttonpress()

# deck_of_cards = CardDeck()
# deck_of_cards.shuffle()
# print(deck_of_cards.card_count())
# print(deck_of_cards.__str__())
