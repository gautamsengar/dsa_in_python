num=int(input("Enter the number : "))
count=0
while(num>0):
   count+=1
   num =num//10
print(f"the number of digits present in given number is {count}")