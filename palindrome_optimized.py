n=int(input("enter the number :"))
num = n
total=0
while(num>0):
    lastDigit=num%10
    total= total*10+lastDigit
    num=num//10
if(n==total):
    print("the number is palindrome")
else:
    print("the number is not palindrome")