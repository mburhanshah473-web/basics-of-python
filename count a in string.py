str=input("Enter the string elements: ")
print(str)
count=0
for i in str:
    if (i)=="a"or(i)=="A":
        count+=1
print(f"the letter a appeared in the string {count} times")        