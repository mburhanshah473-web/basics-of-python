lis=[]
n=int(input("Enter the total number of elements of the list: "))
for i in range(n):
    small=int(input("Enter the numbers: "))
    lis.append(small)
smallest=lis[0]
for num in lis:
    if(num<smallest):
        smallest=num
print(f"the smallest number in the list is {smallest}")        