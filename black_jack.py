#Add Split Option
#fix double option

import random
from black_jack_art import logo

chips = 500
bet_amount = 0

def start_game():
    print(logo)
    global chips
    global bet_amount
    bet_amount = int(input("How many chips would you like to bet?: "))
    chips -= bet_amount
    print(f"You bet {bet_amount} chips.  You have {chips} chips left")
    deal_cards()

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    global chips
    global bet_amount
    if u_score == c_score:
        chips += bet_amount
        return "Draw "
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score == 0:
        return "You win with a Blackjack"
        win()
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        chips += (bet_amount * 2)
        return "Opponent went over. You win"
    elif u_score > c_score:
        chips += (bet_amount * 2)
        return "You win"
    else:
        return "You lose"

def deal_cards():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        if user_score > 21:
            print((f"Your cards: {user_cards}, You bust"))
        else:
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'hit' to get another card, type 'stay' to stay, or type 'double' to double down: ").lower()
            if user_should_deal == "hit":
                user_cards.append(deal_card())
            elif user_should_deal == "double":
                user_cards.append(deal_card())
                #global chips -= bet_amount
                is_game_over = True
            elif user_should_deal == "stay":
                is_game_over = True
            else:
                print("Not a option, try again")

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    if user_score > 21:
        print(f"Your final hand: {user_cards}, You busted")
    else:
         print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input(f"Do you want to play a game of Blackjack? Your chips total is {chips}. Type 'yes' or 'no': ") == "yes":
    print("\n" * 20)
    start_game()








