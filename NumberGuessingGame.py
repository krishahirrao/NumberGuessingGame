import random

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5

def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high!")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low!")
        return turns - 1
    else:
        print(f"You got the correct answer!: {actual_answer}")

def set_difficulty():
    level = (input("Choose a difficulty. Type 'easy' or 'hard': ")).lower()
    if level == "easy":
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN


def game():
    print("Welcome to number guessing game!")
    print("I am thinking of a number between 1 and 100")
    answer = random.randint(1,100)


    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} guesses left")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if guess == 0:
            print("You have no more guesses")
            return

game()
