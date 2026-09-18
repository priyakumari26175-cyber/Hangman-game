
import random

# 5 predefined words
words = ["python", "computer", "hangman", "keyboard", "program"]

# Funny messages
correct_messages = [
    "🔥 Nice! You got it!",
    "😎 Great guess!",
    "🎯 Bullseye!",
    "🚀 You're doing great!",
]

wrong_messages = [
    "❌ Nope! Try again!",
    "😬 Oops! Wrong letter!",
    "💀 That letter isn't here!",
    "😂 Better luck next time!",
]

print("=" * 40)
print("        🎮 WELCOME TO HANGMAN 🎮")
print("=" * 40)

play_again = "yes"

while play_again == "yes":

    word = random.choice(words)

    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    print("\n🔤 A random word has been selected!")
    print("❤️ You have 6 lives.")
    print("💡 Guess one letter at a time.")

    while wrong_guesses < max_wrong:

        # Display hidden word
        display = ""

        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print("\n" + "-" * 40)
        print("Word :", display)
        print("❤️ Lives left:", max_wrong - wrong_guesses)

        if guessed_letters:
            print("📝 Guessed letters:", " ".join(guessed_letters))

        # Check if player won
        complete = True

        for letter in word:
            if letter not in guessed_letters:
                complete = False

        if complete:
            print("\n🎉🎉 YOU WON! 🎉🎉")
            print("🏆 The word was:", word)

            score = (max_wrong - wrong_guesses) * 10
            print("⭐ Your score:", score)

            break

        # Take input
        guess = input("\n👉 Enter a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter only ONE letter!")
            continue

        # Check repeated guess
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        # Correct or wrong guess
        if guess in word:
            print(random.choice(correct_messages))
        else:
            wrong_guesses += 1
            print(random.choice(wrong_messages))

    else:
        print("\n" + "=" * 40)
        print("          💀 GAME OVER 💀")
        print("=" * 40)
        print("😢 You ran out of lives!")
        print("🔑 The word was:", word)

    # Play again
    play_again = input("\n🔄 Do you want to play again? (yes/no): ").lower()

    while play_again != "yes" and play_again != "no":
        print("⚠️ Please enter yes or no.")
        play_again = input("Play again? (yes/no): ").lower()

print("\n========================================")
print("👋 Thanks for playing Hangman!")
print("🏆 See you next time, Word Master!")
print("========================================")


