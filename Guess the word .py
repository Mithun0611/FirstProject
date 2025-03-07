store = []
try_p = 8
guessed_word = "python"  
hint = guessed_word[0] + guessed_word[-1] 

a = input("Enter your name: ")
print("Welcome to the word game,", a)
print("You have 6 chances to guess the word.")

for guess in range(try_p):
    while True:
        letter = input("Enter a letter: ")
        if len(letter) == 1:
            break
        else:
            print("Oops..! Please guess a single letter!")

    if letter in guessed_word: 
        print("Good guess!")
        store.append(letter)
    else:
        print("Oops..! Try again!")

    if guess == 3:  
        print()
        clue_req = input("Do you want a clue? (yes/no): ")
        if clue_req.lower().startswith('y'):
            print("\nClue: The first and last letter of the word is", hint)
        else:
            print("You are very confident!")

print("\nNow let's see what you have guessed so far. You have guessed", len(store), "letters.")
print("These letters are:", store)

word_guess = input("Now guess the word: ").lower()
if word_guess == guessed_word:  
    print("Congratulations! You have guessed the word correctly 🎉")
else:
    print("Sorry! The word was", guessed_word)

print("Thanks for playing the game,", a)
print("Hope you enjoyed the game!")
print("Goodbye!")
