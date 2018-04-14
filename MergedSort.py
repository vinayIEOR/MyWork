'''
Merged sort algorithm
'''
x=[12,5,6,15,-2,3]
def merge(a,b):
    print(a)
    print("vinay")
    print(b)

def mergesort(x):
    """ Function to sort an array using merge sort algorithm """
    if len(x) == 0 or len(x) == 1:
        return(x)
    else:
        middle = len(x)//2
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])
        return merge(a, b)

mergesort(x)
