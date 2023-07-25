# Guess the Number!

import random
number = random.randint(1, 100)

player_name = input("Hello Man!,  what's your name ? : ")

number_of_guesses = 0
print(f"Okay! {player_name} I'm Guessing a number between 1 to 100 : ")

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1

    if guess < number:
        print("Your guess is too low")
    if guess > number:
        print("Your guess is too high")

if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + 'tries!')
else:
    print(" ")
    print('You did not guess the number, The number was ' + str(number))
    print("Try Once again!")