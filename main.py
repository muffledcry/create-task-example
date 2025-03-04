import random

# List of vocabulary words and definitions
vocab_list = [
    {"word": "algorithm", "definition": "A step-by-step procedure for solving a problem or accomplishing a task."},
    {"word": "abstraction", "definition": "The process of simplifying complex reality by modeling classes appropriate to the problem."},
    {"word": "iteration", "definition": "The repetition of a process in order to generate a sequence of outcomes."},
    {"word": "selection", "definition": "A decision-making structure that allows for choosing different paths based on conditions."},
    {"word": "variable", "definition": "A named storage location in a program that holds a value."}
]

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
    for i, definition in enumerate(definitions, 1):
        print(f"{i}. {definition}")
    
    # Get user input
    user_choice = int(input("Enter the number of your choice: "))
    
    # Check if correct
    if definitions[user_choice - 1] == correct_definition:
        print("Correct! Well done.")
    else:
        print(f"Incorrect. The correct definition is: {correct_definition}")

# Main program loop
def main():
    print("Welcome to the Vocabulary Quiz!")
    while True:
        quiz_user()
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

# Run the program
if __name__ == "__main__":
    main()
