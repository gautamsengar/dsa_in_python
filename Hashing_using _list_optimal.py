m=[1,2,3,2,3,6,3,9,6,6,6]       
n=[0,100,2,3,9,1,6]
hashing_list=[0]*11
for i in m:
        hashing_list[i]+=1
for i in n:
   if(i<0 or i>10):
       print(0)
   else:
       print(f"the number {i} is present in list {hashing_list[i]} times")
