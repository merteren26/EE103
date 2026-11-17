dummy1=(3)
dummy2=(3,)
print(type(dummy1))
print(type(dummy2))

total=0
dummy_range=range(10)
dummy_list_1=list(dummy_range)
dummy_list_2=[]

for i in range (10):
    dummy_list_2.append(i)

print(dummy_list_1==dummy_list_2)

for i in dummy_list_1:
    total+=i

print(total)

dummy_list=[x**2 for x in range(10)]
for index, value in enumerate(dummy_list):
    print(index,value)
