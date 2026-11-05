def binary_conventor(decimal_number):
    binary_number = ""
    
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = str(remainder) + binary_number
        decimal_number //= 2
    return binary_number

n=input("Enter positive n: ")
total=0.0
n=int(n)
for i in range(n):
    total+=0.1
print("Total: ", total)
if total==n/10:
    print("Equal: True")
else:
    print("Equal: False")
if abs(total- n/10)<1e-9:
    print("Close enough: True")
else:
    print("Close enough: False")