#factorial using recursion
number = int(input("Enter the number whose factorial you want : "))
def fact(number):
    if number==1 or number ==0   :
        return 1
    else:
        return number * fact(number-1)
    
print("the factorial of given number is ",fact(number))

 #time complexity : O(n)
 #space complexity : O(n) (recursion stack involved)