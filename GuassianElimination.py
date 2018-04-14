
'''
we have m equation with n variable 
we have to find the solution for given equation
arrange all the equation in matrix and use guassian elimination  
'''
import numpy as np

def InputMatrix(m,n):
    np.random.seed(100)
    Mat=[]
    TempRow=[]
    choice=input("Do You want to enter the matrix if yes press 1 ow. 0")
    if choice=="0":
        
        for i in range(0,m):
            for j in range(0,n):
                a=np.random.randint(1,10)
                TempRow.append(float(a))
            Mat.append(TempRow)
            TempRow=[]
        return np.array(Mat)
    else:
        
        for i in range(0,m):
            for j in range(0,n):
                a=float(input("enter the element of matrix (Row wise): "))
                TempRow.append(a)
            Mat.append(TempRow)
            TempRow=[]
        return np.array(Mat)


            
def GuassianElimination():
    global m,n
    b=[]
    
    mat=InputMatrix(m, n)
    print(mat)
    print("\n")
    B=input("Do you want enter right hand for system of equation press:- 1 ")
        
    if B=="1":
        for s in range(0,m):
            a=int(input("enter the values of b column: "))
            b.append(a)
    print(b)
    print("\n")
    for k in range(0,m-1):
            for i in range(k+1,m):
                if mat[k,k]==0 :
                    x=k
                    for y in range(0,n):
                        temp=mat[x,y]
                        mat[x,y]=mat[x+1,y]
                        mat[x+1,y]=temp
                    temp1=b[x]
                    b[x]=b[x+1]
                    b[x+1]=temp1
                        
                
                coef=mat[i,k]/mat[k,k]
                for j in range(0,n):
                    mat[i,j]=mat[i,j]-coef*mat[k,j]
                if len(b)>0:
                    b[i]=b[i]-coef*b[k]
            print("\n")
            print(mat,b)
        
    
    
    
    print("\n")
    if mat[-1,-1]==0:
        print("system has no solution")
    else:
            

        for k in range(m-1,0,-1):
            for i in range(0,m-1):
                c=mat[i,k]/mat[k,k]
                for j in range(0,n):
                    if i==j and k==j:
                        continue
                    mat[i,j]=mat[i,j]-c*mat[k,j]
                if len(b)>0:
                    if i==k:
                            continue
                    b[i]=b[i]-c*b[k]
        print(mat,b)
    
    
    
        for i in range(0,m):
            if mat[i,i]==0:
                continue
            if len(b)>0:
                b[i]=b[i]/mat[i,i]
                mat[i,i]=mat[i,i]/mat[i,i]
        print("\n")
        print(mat,b)
            
            
            
m=int(input("enter the no. of row in matrix"))
n=int(input("enter the no. of column in matrix"))


GuassianElimination()


#MAtrix=InputMatrix(3, 4) 
#print(MAtrix)   