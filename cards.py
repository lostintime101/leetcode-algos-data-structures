import random

"""

You have a normal shuffled deck of cards. We will draw cards 1 at a time until the entire deck is finished. 
Before any card is drawn you may bet (or not) on whether it is red or black. 
Construct the best strategy (win the most) regardless of card distribution.
You have 100000 to bet with and can bet any amount / fractional amount as long as it doesn't exceed your current total

"""

class Deck:
    def __init__(self, num_of_cards):
        self.reds = num_of_cards // 2
        self.blacks = num_of_cards // 2

    def pull_next_card(self):

        if self.reds and self.blacks: next_card = random.choice(["black", "red"])
        elif self.reds: next_card = "red"
        elif self.blacks: next_card = "black"
        else: return None

        if next_card == "red": self.reds -= 1
        if next_card == "black": self.blacks -= 1

        return next_card


class Player:
    def __init__(self, dollars):
        self.bankroll = dollars

    def calculate_optimal_choice(self, card_deck):
        red_odds = card_deck.reds / (card_deck.reds + card_deck.blacks)
        black_odds = 1 - red_odds

        if red_odds > black_odds: return ["red", round(red_odds, 4)]
        elif black_odds > red_odds: return ["black", round(black_odds, 4)]
        else: return None

    def make_bet(self, odds):

        color, chance = odds[0], odds[1]
        size = (((chance * chance) - (1-chance)) / chance) # KELLY CRITERION

        return [color, round(self.bankroll * size, 2)]


# GLOBALS
STARTING_CAPITAL = 100000
STARTING_DECK_SIZE = 52  # MUST BE EVEN

deck = Deck(STARTING_DECK_SIZE)
player = Player(STARTING_CAPITAL)

while deck.reds or deck.blacks:

    new_bet = 0
    optimal_choice = player.calculate_optimal_choice(deck)
    new_card = deck.pull_next_card()  # RANDOM PICK RED OR BLACK

    if optimal_choice:  # NO BET IF 50/50
        new_bet = player.make_bet(optimal_choice)

    if new_bet:
        if new_card == optimal_choice[0]:
            player.bankroll += round(new_bet[1], 2)
        else: player.bankroll -= round(new_bet[1], 2)

    print(f"Card was {new_card}. Player bet {new_bet}. Player bankroll ${round(player.bankroll, 2)}")

print(f"Player's final bankroll: ${round(player.bankroll, 2)}. Profit was ${round(player.bankroll - STARTING_CAPITAL, 2)}")








