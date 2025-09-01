n=int(input("input the number : "))
num=n
count=0
total=0
numtemp=num
while(num>0):
    count+=1
    num=num//10
while(numtemp>0):
    temp=numtemp%10
    total+= temp**count
    numtemp=numtemp//10
if(total==n):
   print("the number is armstrong number")
else:
    print("the number is not armstrong number")
    

# Armstrong number is a number that is equal to the sum of cubes of its digits. For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.
# Another example is 370, where 3^3 + 7^3 + 0^3 = 370.
#time complexity is O(logn⋅loglogn) and its optimal
