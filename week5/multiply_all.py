start=int(input("Enter a number: "))
end=int(input("Enter another number: "))
def multiply_all1(start, end):
    result = 1
    for i in range(start, end+1):
        result *= i
    return result

def multiply_all2(start, end):
    result= 1
    while start <= end:
        result *= start
        start += 1
    return result

if multiply_all1(start, end) == multiply_all2(start, end):
    print("Both functions give the same result:", multiply_all1(start, end))
else:
    print("The functions give different results.")