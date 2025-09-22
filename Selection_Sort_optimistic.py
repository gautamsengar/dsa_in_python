def Selection_Sort(array):
    n=len(array)
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if array[j]<array[min_index]:
                  min_index=j
        array[min_index],array[i]=array[i],array[min_index]
    return array
array=[7,6,5,8,9,1,0]
print(Selection_Sort(array))