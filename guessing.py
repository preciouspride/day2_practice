
#Let the computer generate a random number between between 1 and 10
computer_guess = 0 ## Assignment => Check how to generate a random number between 1 and 10 using python. Hint Look at the python random module
your_guess = int(input("Enter your guess: "))

while computer_guess != your_guess:
    your_guess = int(input("That was not right. Guess again: "))
print("Yes, you guessed right! You WON")