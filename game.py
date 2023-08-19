def display_menu():
    print("Wellcome to Hangman!") 

def display_word(word,guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

    