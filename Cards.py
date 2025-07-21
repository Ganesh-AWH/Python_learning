import random

def deal_card():
    """Return a random card from the cards list"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    #below if block indicates black jack
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    #removing ace and choosing 1
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare_score(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif u_score == 0:
        return "Win with a blackjack"
    elif c_score == 0:
        return "Computer win with blackjack"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "Computer over. You lose"
    elif u_score > c_score:
        return "You win, by leading score"
    else:
        return "You lose, computer takes leading score"


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
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if(user_score == 0 or computer_score == 0 or user_score > 21):
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if user_should_deal == 'y':
            user_cards.append(deal_card())
        else:
            is_game_over = True
    

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
    
print(f"Your final hand {user_cards}, Your final score {user_score}")
print(f"Computer's final hand {computer_cards}, Computer final score {computer_score}")
print(compare_score(user_score, computer_score))
