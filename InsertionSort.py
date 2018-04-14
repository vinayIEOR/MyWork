"""implementation of insertion sort ALgorithm"""

def insert(SortArray,key): 
    index=SortArray.index(key)
    for i in range(len(SortArray)-2,-1,-1):
        if key<SortArray[i]:
            SortArray[i+1]=SortArray[i]
            index=i
        
        elif key >= SortArray[i]:
            break
    
    SortArray[index]=key
    return SortArray
 
def InsertionSort(Array):
    i=1
    print(Array)
    while i <= len(Array)+1:
        SubArray=Array[:i]
        A=insert(SubArray,SubArray[-1])
        Array[:i]=A
        i=i+1
    print(Array)


    

InsertionSort([10,7,3,13,2,8,5,1,8,3,5,4,10,15])
InsertionSort([22, 11, 99, 88, 9, 7, 42])

