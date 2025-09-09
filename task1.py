import random

# Predefined list of words
word_list = ["python", "sensor", "energy", "climate", "iot"]

# Randomly select a word
chosen_word = random.choice(word_list)
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

# Create a display version of the word with underscores
display_word = ["_" for _ in chosen_word]

print("🎯 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses. Good luck!\n")

# Game loop
while incorrect_guesses < max_attempts and "_" in display_word:
    print("Word: " + " ".join(display_word))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single alphabetic character.\n")
        continue

    if guess in guessed_letters:
        print("🔁 You've already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("✅ Good guess!\n")
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong guess! You have {max_attempts - incorrect_guesses} tries left.\n")

# Final result
if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("💀 Game Over! The word was:", chosen_word)