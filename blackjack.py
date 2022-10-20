import random
#Blackjack

dealer_cards = []

player_cards = []

# Dealer cards
while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print("Dealer has x &", dealer_cards[1])

# Player cards
while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))
    if len(player_cards) == 2:
        print("You have", player_cards)

#win conditions
while sum(player_cards) < 21:
    choice_made = str(input("Do you want to stay or hit? "))
    if choice_made == "hit":
        player_cards.append(random.randint(1, 11))
        print("You now have " + str(sum(player_cards)) + " with ", player_cards)
    else:
        print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
        print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
        if sum(dealer_cards) > sum(player_cards):
            print("Dealer wins")
            break
        else:
            print("You win")
            break

if sum(player_cards) > 21:
    print("You bust, dealer wins")
elif sum(player_cards) == 21:
    print("You win")