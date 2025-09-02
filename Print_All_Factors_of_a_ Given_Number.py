n=int(input("enter the number by the user :"))
print(f"the factors of {n} are : ",end="")
for i in range(1,n+1):
    if(n%i==0):
        print(f"{i},",end="")
