#What it does:
#The correct number is set to 33.
#It repeatedly asks the user to guess the number.
#If the guess is correct, it prints a success message and exits.
#If the guess is too low or too high, it gives a hint and asks again.
#The strip() method is used to remove any extra spaces from the input.
#The int() function converts the input from a string to an integer, since input() returns a string by default in Python.


number = 33

while True:
    guess = int(input("Enter a number:").strip())

    if number == guess:
        print("Congratulation u guessed it")
        break
    elif guess < number:
        print("No, Its a little higher than that")
    else:
        print("No, its a little lower than that")
