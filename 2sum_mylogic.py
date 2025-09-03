element=int(input("enter the number of elements you want to enter in list : "))
t=0
a=[]
while (t<element):
    values=int (input( "enter values in list : "))
    a.append(values)
    t=t+1
target=int(input("enter your target value for two sum : "))
num=int(len(a))
i=0
j=1
while(i<num-1):
    
    if(target==(a[i]+a[j])):
        print(f" the indices value whose sum is {target} are {i},{j} ")
        break
    elif(j==num-1):
        i=i+1
        j=i+1
    else:
        j=j+1
