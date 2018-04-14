import numpy as np
import matplotlib.pyplot as plt


b=[]
def ex1fun(a,m):
    temp=0
    for i in range(0,len(a),4):
        if i+m<len(a) or i+m==len(a):
            for j in range(i,i+m):
                temp=temp+a[j]
            b.append(temp/4)
            temp=0
    print("The number of elements in b: "+str(len(b)))
    print("\n")
    print("The minimum value amongst all elements of the matrix b: "+str(min(b)))
    print("\n")
    print("The maximum value amongst all elements of the matrix b: "+str(max(b)))
    avg=(sum(b)/len(b))
    print("\n")
    print("The average value of elements of b: "+str(avg))
    sd=np.std(b)
    print("\n")
    print("The standard deviation of elements of b: "+str(sd))
    plt.hist(b,color="red", label="Histogram of B")
    plt.show()
    
a=[]
fname=open("ex1a")
fline = fname.readline()
while (fline):
    a.append(int(fline))
    fline=fname.readline()


m=int(input("enter the value of M"))

ex1fun(a, m)




