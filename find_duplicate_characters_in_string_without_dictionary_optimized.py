str="abbagggghhhhhjzzyw"
char=['a','b','c','z','w', 'y','g']
hashing_list=[0]*123
for i in str:
   index= ord(i)
   hashing_list[index]+=1
for i in char:
  print (f"the word {i} appeared in string for {hashing_list[ord(i)]} times")
# This makes the complexity:
#   Time: O(n + m)

# Space: O(1)