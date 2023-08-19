import game as g
import extract_words
import os

def game():
    word = extract_words.random_word()
    attempts = 6
    guessed_letters = []
    g.display_menu()
    print(g.display_word(word,guessed_letters))

    while True:
        guess = input('Guess a letter:').lower()
        os.system('cls')

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one valid letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed this letter before.")
            continue
        
        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print(f"Wrong answer! You still have {attempts} left.")
            if attempts == 0:
                print(f"You lost! The word was: {word}")
                break
        
        word_display = g.display_word(word,guessed_letters)
        print(word_display)

        if '_' not in word_display:
            print("Congratulations! You won!")
            break

game()

