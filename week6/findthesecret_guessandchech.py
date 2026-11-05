import EE103.week6.secret_data as secret_data
x=0
guess= 1000
while guess != secret_data.secret_year:
    x+=1 
    if guess < secret_data.secret_year:
        guess += 1
    elif guess > secret_data.secret_year:
        guess -= 1

print("The secret year is:", guess)

print("Number of guesses:", x)