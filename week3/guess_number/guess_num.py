from secret_number import secret_num

for i in range(5):
    guess = int(input("What is your guess? "))
    if guess < secret_num:
        print("Too low.")
    elif guess > secret_num:
        print("Too high")
    else:
        print("Your guess is correct!")
        break
else:
    print("You ran out of guesses.")
    while secret_num==6:
        print("Ohh!Nooooooooooo!")