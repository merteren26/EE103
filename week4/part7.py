binary=""

a=13

while a>0:
    binary=str(a%2)+binary
    a=a//2

print(binary)