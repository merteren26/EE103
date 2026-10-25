x=float(input("What x to find cube root of? "))
g=float(input("What is the guess? "))

next_guess=(g-(g**3-x)/(3*g**2))
print(f"The next guess is: {next_guess}")
