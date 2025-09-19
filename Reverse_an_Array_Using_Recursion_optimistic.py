def reverseArr(arr,right,left):
    if right<=left:
        return arr
    arr[right],arr[left]=arr[left],arr[right]
    return reverseArr(arr,right-1,left+1)

arr=[3,4,1,6,2,3,4,0]
right=len(arr)-1
left=0
result = reverseArr(arr,right,left)
print(result)