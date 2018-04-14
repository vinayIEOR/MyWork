from math import *
import numpy as np
import matplotlib.pylab as plt

def ex1fun(a,m):
    b=[]
    for i in range (0,len(a),m):
      d=a[:m]
      b.append((sum(d)/m))
      del a[:m]
    return(b);
a=[]
fname=open("ex1a")
fline = fname.readline()
while (fline):
    a.append(int(fline))
    fline=fname.readline()
m=int(input("enter m"))
b=ex1fun(a,m)

x=min(b)
y=max(b)
z=sum(b)/len(b)
temp=0
for i in range (0,len(b)):
   Var=(b[i]-z)**2
   temp=temp+Var
SD=(temp/(len(b)-1))**0.5
    
avg=(sum(b)/len(b))

print("No.of elements in element of b",len(b))
print(b)
print ("min in b",min(b))
print ("max in b",max(b))
print ("avarage b",avg)
print ("standard deviation of b",SD)
plt.hist(b)
plt.title("b Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
