# Let's build a Blackjack game
# player against dealer

import random

Cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


def choose_card():
    return random.choice(Cards)


player_cards = []
dealer_cards = []

for i in range(2):
    player_cards.append(choose_card())
    dealer_cards.append(choose_card())

game_over = False
while not game_over:
    player_score = sum(player_cards)
    dealer_score = sum(dealer_cards)
    print("Your cards: ", player_cards, "current score: ", player_score)
    print("Dealer's first card:", dealer_cards[0])

    if player_score > 21:
        print("You went over. You lose!")
        game_over = True
    else:
        choice = input("Type 'y' to get another card, type 'n' to pass: ")
        if choice == "y":
            player_cards.append(choose_card())
        else:
            game_over = True

while dealer_score < 17:
    dealer_cards.append(choose_card())
    dealer_score = sum(dealer_cards)

print("Your final cards:", player_cards, "final score: ", player_score)
print("Dealer's final cards:", dealer_cards, "final score: ", dealer_score)
if dealer_score > 21:
    print("Dealer went over. You win!")
elif dealer_score > player_score:
    print("You lose!")
elif player_score > dealer_score:
    print("You win!")
else:
    print("It's a draw!")

