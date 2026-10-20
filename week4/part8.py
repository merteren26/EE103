binary=""
a=0.375

while a>0:
    binary=binary+str(int(a*2))
    a=a*2-int(a*2)

print(binary)

last="0."+binary
print(f"The binary representation of 0.375 is {last}")