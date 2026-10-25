n=int(input("Choose a number"))
sum=0
for i in range(1,n+1):
    sum+=i

print(f"The sum of numbers from 1 to {n} is {sum}")

real_sum= n*(n+1)/2

if real_sum==sum:
    print("The sum is correct")
else:
    print("The sum is incorrect")