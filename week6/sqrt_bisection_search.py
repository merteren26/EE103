import EE103.week6.secret_data as secret_data
counter=0

low=1
high=18
while low <= high:
    counter+=1
    mid=(low+high)//2
    if mid*mid < secret_data.secret_year:
        low=mid+1
    elif mid*mid > secret_data.secret_year:
        high=mid-1 
    elif mid*mid == secret_data.secret_year:
        break
        

print("Number of iterations:", counter)
print(mid)