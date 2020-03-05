# The Game of Black Jack
import random
print( ' INSTRUCTION : Reveal dealer hand , press space before giving input')
print( '             : type hit to get more card, otherwise stay')
# GAME RULE FOR EACH ROUND
# Dealer cars
dealer_cards = []
# Player 1 hand
player1_cards =[]
# Player 2 hand
player2_cards =[]
# Dealer cards
while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print('Dealer has X and', dealer_cards[1])
        break
action_taken = str(input(" Reveal dealer hand, type YES to continue , type NOPE to fold the game"))
if action_taken == " yes" :
    print("Dealer now has " + str(sum(dealer_cards))+ " from these cards", dealer_cards)
else :
    print("both players fold and dealer win")
# Player 1 cards
while len(player1_cards) != 2:
    player1_cards.append(random.randint(1, 11))
    if len(player1_cards) == 2:
        print('Player 1 has', player1_cards)

# Player 2 cards
while len(player2_cards) != 2:
    player2_cards.append(random.randint(1, 11))
    if len(player2_cards) == 2:
        print("Player 2 has", player2_cards)

# Sum of Dealer hand
while sum(dealer_cards) < 21 :
    action_taken = str(input(" Dealer : hit or stay?"))
    if action_taken == " hit" :
        dealer_cards.append(random.randint(1,11))
        print("Dealer now have a total of " + str(sum(dealer_cards)) + " from these cards ", dealer_cards)
    else:
        print("Dealer have a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
        break
if sum(dealer_cards) > 21:
    print("Dealer has busted")
elif sum(dealer_cards) == 21:
        print("Dealer has Black Jack and win")
# Sum of Player 1 hand
while sum(player1_cards) < 21:
    action_taken = str(input(" Player 1 :do you want to stay or hit? ")) # If p1 hand is less than 21 = option hit or stay
    if action_taken == " hit":
        player1_cards.append(random.randint(1,11))
        print("You now have a total of " + str(sum(player1_cards)) + " from these cards ", player1_cards)
    else:
        print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
        print("You have a total of " + str(sum(player1_cards)) + " with ", player1_cards)
        if sum(dealer_cards) > sum(player1_cards) and sum(dealer_cards) < 21:
            print("Dealer wins!")
        else:
            print("You win!")
            break
if sum(player1_cards) > 21 : # If P1 hand is over 21 = bust
    print(" You busted ")
elif sum(player1_cards) == 21:
    print('You have blackjack and win')

# Sum of Player 2 hand
while sum(player2_cards) < 21:
    action_taken = str(input(" Player 2 : do you want to stay or hit? ")) # If p1 hand is less than 21 = option hit or stay
    if action_taken == " hit":
        player2_cards.append(random.randint(1,11))
        print("You now have a total of " + str(sum(player2_cards)) + " from these cards ", player2_cards)
    else:
        print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
        print("You have a total of " + str(sum(player2_cards)) + " with ", player2_cards)
        if sum(dealer_cards) > sum(player2_cards):
            print("Dealer wins!")
        else:
            print("You win!")
            break
if sum(player2_cards) > 21 : # If P1 hand is over 21 = bust
    print(" You busted ")
elif sum(player2_cards) == 21:
    print('You have blackjack and win')
