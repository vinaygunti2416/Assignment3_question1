def Sum(list1):
    return sum(list1)


size=int(input("enter your list size:"))
list1=[]
for i in range(size):
    print("enter your element:",end="")
    list1.append(int(input()))
total=Sum(list1)
print("sum of all elements:",total)
