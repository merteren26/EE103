n=int(input("Choose a number"))

i=0
if 0<=n:
    while i*i<=n:
        if i*i==n:
            print(f"The square root of {n} is {i}")
            break
        i+=1
    else:
        print(f"{n} is not a perfect square")   
else:
    print("Please enter a non-negative number")