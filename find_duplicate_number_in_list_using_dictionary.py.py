num=[1,1,1,2,1,3,3,4]
hash_map={}
for i in range(0,len(num)):
 if num[i] not in hash_map:
  hash_map[num[i]]=1
 else:
  hash_map[num[i]]+= 1
print(hash_map)
for i in hash_map:
 if (hash_map[i] >1):
  print (f"{i} is duplicate as it appeared {hash_map[i]} times")
 else:
  print(f"{i} is not duplicate")

