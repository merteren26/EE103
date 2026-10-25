binary = "0."
a = 0.1
result = 0
weight = 0.5

while abs(result - a) >= 0.00001:
    a = a * 2
    bit = int(a)
    binary = binary + str(bit)

    result = result + bit * weight
    a = a - bit
    weight = weight / 2

print("Binary representation of 0.1 is: " + binary)
print(f"Approximate value: {result:.5f}")