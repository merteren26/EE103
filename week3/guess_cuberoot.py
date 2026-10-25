n=int(input("Choose a number"))

i=0
target = abs(n)
while i**3<=target:
    if i**3==target:
        root = i if n >= 0 else -i
        print(f"The cube root of {n} is {root}")
        break
    i+=1
else:
    print(f"{n} is not a perfect cube")