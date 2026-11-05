year=int(input("What year is this?"))
x=0
y=0
for digit in str(year):
    y+=1 #Number of digits
    digit=int(digit)
    x+=digit

print("x/y =", x/y)