nums= [1,2,2,1,1,5,7,6,6]
frequency_map=dict()
n=len(nums)
for i in range(0,n):
    if nums[i] not in frequency_map:
        frequency_map[nums[i]]=1
    else:
        frequency_map[nums[i]]+=1
print(frequency_map)