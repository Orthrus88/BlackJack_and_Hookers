import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
# random.shuffle(deck)

def calculate_hand_value(hand):
    value = 0
    aces_count = 0

    for card in hand:
        rank = card['rank']
        if rank == 'Ace':
            aces_count += 1
        elif rank in ['Jack', 'Queen', 'King']:
            value += 10
        else:
            value += int(rank)

    return value

#def deal_card():
    #return deck.p

def display_hand(hand):
    return ', '.join(card['rank'] + ' of ' + card['suit'] for card in hand)

def hit(hand):
    hand.append(deal_card())

def is_bust(hand_value):
    return hand_value > 21

def is_blackjack(hand_value):
    return hand_value == 21

def compare_hands(player_value, dealer_value):
    if player_value == dealer_value:
        return "It's a tie!"
    elif player_value > dealer_value:
        return "You win!"
    else:
        return "Dealer wins!"

def blackjack_game():
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    while True:
        player_hand_value = calculate_hand_value(player_hand)
        dealer_hand_value = calculate_hand_value(dealer_hand)

        print("Your hand: " + display_hand(player_hand))
        print("Your hand value:", player_hand_value)
        print("Dealer's face-up card:", display_hand([dealer_hand[0]]))

        if is_blackjack(player_hand_value):
            print("Blackjack! You win!")
            break

        if is_bust(player_hand_value):
            print("Bust! You lose!")
            break

        choice = input("Do you want to hit or stand? (h/s): ").lower()
        if choice == 'h':
            hit(player_hand)
        elif choice == 's':
            while dealer_hand_value < 17:
                hit(dealer_hand)
                dealer_hand_value = calculate_hand_value(dealer_hand)

            print("Dealer's hand:", display_hand(dealer_hand))
            print("Dealer's hand value:", dealer_hand_value)

            if is_bust(dealer_hand_value):
                print("Dealer busts! You win!")
            else:
                print(compare_hands(player_hand_value, dealer_hand_value))
            break
        else:
            print("Invalid input. Enter 'h' for hit or 's' for stand.")

if __name__ == "__main__":
    blackjack_game()