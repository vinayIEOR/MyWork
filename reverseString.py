

rev=""
def ReverString(string):
    global rev
    for s in range(len(string)-1,-1,-1):
        rev=rev+string[s]
     
    print(string)
    print(rev)
        
ReverString("1234abcd")        
    