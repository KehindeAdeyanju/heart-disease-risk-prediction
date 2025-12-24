

secret_word = "giraffe"
#create a variable that will store all the users response.
guess = "" #empty string
guess_count = 0
guess_limit = 3
out_of_guesses = False  # boolean

# prompt the user to input the secret word

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1 #add 1 to the guess_count each time we run the loop
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print( "You win!")