import random

words = ["python", "computer", "developer", "programming", "student"]

secret_word = random.choice(words)

guessed_letters = set()
wrong_guesses = 0
max_attempts = 6

stages = [
    """
     -----
     | |
         |
         |
         |
    =========
    """,
    """
     -----
     | |
     O |
         |
         |
    =========
    """,
    """
     -----
     | |
     O |
     | |
         |
    =========
    """,
    """
     -----
     | |
     O |
    /| |
         |
    =========
    """,
    """
     -----
     | |
     O |
    /|\\ |
         |
    =========
    """,
    """
     -----
     | |
     O |
    /|\\ |
    / |
    =========
    """,
    """
     -----
     | |
     O |
    /|\\ |
    / \\ |
    =========
    """
]

print("WELCOME TO HANGMAN GAME!")

while wrong_guesses < max_attempts:

    print(stages[wrong_guesses])

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Wrong attempts:", wrong_guesses, "/", max_attempts)

    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You Won!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.add(guess)

    if guess in secret_word:
        print("Correct Guess!")
    else:
        print("Wrong Guess!")
        wrong_guesses += 1

else:
    print(stages[wrong_guesses])
    print("GAME OVER!")
    print("The correct word was:", secret_word)
