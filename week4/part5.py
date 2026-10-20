ticket=1000
i=1


for alyssa in range(20, 1001):
    for ben in range(0, 1001):
        cindy = alyssa * 2

        if ben == alyssa - 20 and alyssa + ben + cindy == ticket:
            print(f"Alyssa: {alyssa}, Ben: {ben}, Cindy: {cindy}")
            break


#for i in range(i, 300):
    ben=i-20
    cindy=i*2
    if 4*i-20==ticket:
        print(f"Ben is {ben} and Cindy is {cindy} and Alysa is {i}")
        break
    i+=1