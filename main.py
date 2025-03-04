import os
import random

# List of vocabulary words and definitions
vocab_list = [
    {"word": "algorithm", "definition": "A process or set of rules to be followed in calculations or other problem-solving operations, especially by a computer."},
    {"word": "abstraction", "definition": "The process of simplifying and hiding complexities to focus on problems of greater importance."},
    {"word": "iteration", "definition": "The repetition of a process in order to generate a sequence of outcomes."},
    {"word": "selection", "definition": "Decision-making that allows for choosing different paths based on conditions."},
    {"word": "variable", "definition": "A named storage location in a program that holds a value."}
]

# Helper function to clear the screen
def clear():
    os.system("clear")

# Function that picks a random word and quizzes the user
def quiz_user():
    entry = random.choice(vocab_list)  # Selects a random vocabulary entry
    word = entry["word"]
    correct_definition = entry["definition"]

    # Creating a list of possible definitions for multiple choice
    definitions = [correct_definition]
    for _ in range(3):
        random_def = random.choice(vocab_list)["definition"]
        definitions.append(random_def)
    random.shuffle(definitions)

    print(f"What is the definition of '{word}'?")
    print()
    for i, definition in enumerate(definitions, 1):
        print(f"{i}. {definition}")

    # Get user input
    print()
    user_choice = int(input("Enter the number of your choice: "))
    print()

    # Check if correct
    if definitions[user_choice - 1] == correct_definition:
        print("Correct! Well done.")
        print()
    else:
        print(f"Incorrect. The correct definition is: {correct_definition}")
        print()

# Main program loop
def main():
    print("Welcome to the Vocabulary Quiz!")
    print("="*40)
    print()
    
    while True:
        quiz_user()
        keep_playing = ["yes", "y"]
        play_again = input("Would you like to play again? (yes/no): ").lower()
        clear()
        if play_again not in keep_playing:
            print("Thanks for playing!")
            break

# Run the program
if __name__ == "__main__":
    main()


# Collection: A list of dictionaries (vocab_list) stores words and definitions.
# Managing Complexity: Using this list simplifies accessing and randomizing quiz questions. It also means I can easily add more words and definitions without changing the program.
# Procedural Abstraction: The quiz_user() function abstracts the quiz process.
# Algorithm Explanation:
# - Sequencing: Code executes in order (select word, display choices, get input, check answer).
# - Selection: Uses if statement to check correctness.
# - Iteration: Uses a loop to keep the quiz running.
# Testing: The quiz function is called multiple times with different random words.
