import random

def genetic_algorithm_number_guessing_game():
    print("Think of a number between 1 and 100, and I (the AI) will try to guess it.")

    population_size = 10  # Number of guesses in each generation
    population = [random.randint(1, 100) for _ in range(population_size)]  # Initial random population
    attempts = 0

    while True:
        # Evaluate fitness based on player's feedback
        for guess in population:
            attempts += 1
            print(f"AI's guess is: {guess}")
            feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()

            if feedback == 'c':
                print(f"I (AI) guessed the number in {attempts} attempts!")
                return
            elif feedback == 'h':
                # Adjust guesses that were too high
                population = [g if g < guess else random.randint(1, guess - 1) for g in population]
            elif feedback == 'l':
                # Adjust guesses that were too low
                population = [g if g > guess else random.randint(guess + 1, 100) for g in population]

        # Mutation step (randomly change some guesses)
        if attempts % 5 == 0:
            population = [random.randint(1, 100) if random.random() < 0.1 else g for g in population]

# Call Genetic Algorithm version
genetic_algorithm_number_guessing_game()
