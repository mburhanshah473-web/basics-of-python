lis=[]
n=int(input("How many numbers you want to add: "))
sum=0
for i in range(n):
    num=int(input("Enter the number: "))
    lis.append(num)
    sum+=num
print(f"the sum of all ements of the list is {sum}")    