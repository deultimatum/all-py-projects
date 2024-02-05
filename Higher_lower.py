from logo wordlist stages import logo_higher_lower, vs, data
import random
from replit import clear
def format_data(account):
    """Get data from the dictionary and format in a printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(user_input, a_follower_count, b_follower_count):
    """Take the users answer and compare to find the correct answer"""
    if a_follower_count > b_follower_count:
        return user_input == "a"
    else:
        return user_input == "b"

print(logo_higher_lower)
compare_b = random.choice(data)
score = 0
continue_game = True
while continue_game:
    compare_a = compare_b
    compare_b = random.choice(data)

    while compare_b == compare_a:
        compare_b = random.choice(data)

    print(f"Compare A : {format_data(compare_a)}")
    print(vs)
    print(f"Against B : {format_data(compare_b)}")

    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follow_count = compare_a["follower_count"]
    b_follow_count = compare_b["follower_count"]
    is_correct = check_answer(user_input, a_follow_count, b_follow_count)

    clear()
    print(logo_higher_lower)

    if is_correct:
        score += 1
        print(f"You are right! current score {score}")
    else:
        continue_game = False
        print(f"Sorry, that's wrong. Final score: {score}")
