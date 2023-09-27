def upper_lower(str1):
    upper=0
    lower=0
    for i in range(len(str1)):
        if ord(str1[i])>=65 and ord(str1[i])<=90:
            upper+=1
        if ord(str1[i]) >=97 and ord(str1[i])<=122:
            lower+=1
    return upper,lower

str1=input("enter your string:")
upper,lower=upper_lower(str1)
print(f"upper: {upper}  lower: {lower}" )
