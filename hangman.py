import random
from hangman_art import stages

def load_words(filename):
    """Load words from a text file into a list."""
    with open(filename, 'r') as file:
        return [word.strip().lower() for word in file.readlines()]

def choose_random_word(word_list):
    """Return a random word from the list."""
    return random.choice(word_list)

def display_word(word, guessed_letters):
    """Return a string with guessed letters revealed and others as underscores."""
    return ' '.join([letter.upper() if letter in guessed_letters else '_' for letter in word])

def get_player_guess(guessed_letters):
    """Prompt the user for a valid guess."""
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single alphabet letter.")
        elif guess in guessed_letters:
            print("⚠️ You've already guessed that letter.")
        else:
            return guess

def play_hangman():
    word_list = load_words("words.txt")
    word = choose_random_word(word_list)
    guessed_letters = set()
    wrong_letters = set()
    max_attempts = len(stages) - 1
    attempts_left = max_attempts

    print("\n🎮 Welcome to Hangman!")
    
    while attempts_left > 0:
        print(stages[max_attempts - attempts_left])
        print("\nWord:", display_word(word, guessed_letters))
        print("Wrong guesses:", ', '.join(sorted(wrong_letters)))
        print(f"Attempts remaining: {attempts_left}\n")

        guess = get_player_guess(guessed_letters.union(wrong_letters))

        if guess in word:
            print("✅ Good guess!")
            guessed_letters.add(guess)
        else:
            print("❌ Wrong guess.")
            wrong_letters.add(guess)
            attempts_left -= 1

        if all(letter in guessed_letters for letter in word):
            print("\n🎉 You won! The word was:", word.upper())
            break
    else:
        print(stages[-1])
        print("\n💀 Game Over. The word was:", word.upper())

def main():
    play_hangman()

if __name__ == "__main__":
    main()
