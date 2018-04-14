"""Implementation of selection sort Algorithm"""

def SelectionSort(Array):
    for i in range(len(Array)):
        MinIndex=i
        MinValue=Array[i]
        for j in range(i,len(Array)):
            if MinValue>Array[j]:
                MinValue=Array[j]
                MinIndex=j
        temp=Array[i]
        Array[i]=Array[MinIndex]
        Array[MinIndex]=temp
    print(Array)
SelectionSort([22, 11, 99, 88, 9, 7, 42])

    
"""
in selection sort algorithm 1st we find minimum value and 
replace it with 1st element(index 0) in given array,
then find second smallest value in array and replace it 
with 2nd position (index 1) and so on..so forth
"""