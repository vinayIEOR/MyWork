import pandas as pd
"""this programme represent all type of processing data in chunk
    when dataset is too large we have process in chunk\
    diff function show how to use chunk data with diif form"""

    
def Chunks1(file): 
    """ TO identify how many nation repeat how may time using dict  in chumk size=1000"""
    
    with open(file) as File:
        File.readline()  #read first line to skip the column name
        count_dict={}
        
        for i in range(1000):
            line=File.readline().split(',')
            first_col=line[0]
            if  first_col in count_dict.keys():
                count_dict[first_col] +=1
            else :
                count_dict[first_col]=1
    
    print(count_dict)

def Generator_Func(file):
    """read large file using GENERATOR function"""
    while True:
        data=file.readline()
        if not data:
            break
        yield data
    
def chunks2(file):
    with open(file) as File:
         # Create a generator object for the file: gen_file
        count_dict={}
        for data in Generator_Func(File):
            line=data.split(",")
            if line[0] in count_dict.keys():
                count_dict[line[0]]+=1
            else:
                count_dict[line[0]]=1
            
        print(count_dict)          












chunks2('world_ind_pop_data.csv')
    














""" European Union EUU
    South Asia    SAS
    Least developed countries: UN classification   LDC """