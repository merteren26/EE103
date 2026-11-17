L=[1,3,5,7]
tupple=()

def length_and_square(L):
    length=len(L)
    squares=[]
    for x in L:
        squares.append(x**2)

    return(length, squares)

print(length_and_square(L))