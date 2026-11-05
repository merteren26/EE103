import EE103.week6.secret_data as secret_data
counter=0 
i=1
while i*i<secret_data.secret_year:
    counter+=1
    i+=0.1

print("The square root of the secret year is approximately:", i)
print("Number of iterations:", counter)
