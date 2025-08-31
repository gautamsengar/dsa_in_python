num=int(input("Enter the number :"))
count=0
list1=[]
temp=num

while(num>0):
   count+=1
   extracted_lastdigit =num%10
   list1.insert(0,extracted_lastdigit)
   num =num//10
print(f"the number of digits present in given number is {count}")
start =0
end= count-1
while(start<end):
   if (list1[start]==list1[end]):
      start+=1
      end-=1
   else: 
      print("the number is not panlindrome")
      break
else:
   print("the number is palindrome")
