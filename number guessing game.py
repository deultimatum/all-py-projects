from logo wordlist stages import logo_guess
import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    """Checks the user guess against computer guess. Returns the number of turns remaining for user"""
    if guess < answer:
        print("Too low")
        return turns - 1
    elif guess > answer:
        print("Too High.")
        return turns - 1
    else:
        print(f"You got it ! your answer is {guess}")

def check_difficulty(): 
  """Checks deficulty according users input"""
    level = input("Choose a difficulty. Type 'easy' or 'hard' ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
  """to start the game """
    print(logo_guess)
    print("Welcome to number guessing game.")
    print("I am thinking of a number between 1 and 100")
    answer = random.randrange(1, 100)# guesss number between 1 and hundred. 
    print(answer)
    turns = check_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} remaining to guess the number.")
        guess = int(input("Make a guess:"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have ran out of guess. You lose!.")
            return
        elif guess != answer:
            print("Guess again ")

game()

