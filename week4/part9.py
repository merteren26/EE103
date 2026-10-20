binary="0."

a=0.399
result=float(binary)

while  result < 0.000001:
    a=a*2
    if a >= 1:
        binary += "1"
        a -= 1
    else:
        binary += "0"
    result=float(binary)

print("Binary representation of 0.371 is: "+binary)