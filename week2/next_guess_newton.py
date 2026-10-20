x= float(input("What x to find the square root of? "))
g= float(input("What guess to start with?"))

print("Current estimate squared:" + str(g**2))

f= g**2 - x 
next_guess= g - f/(2*g)

print("Next guess is: ", next_guess)