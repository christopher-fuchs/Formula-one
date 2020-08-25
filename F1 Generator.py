#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import math
from itertools import combinations
import itertools
import re
import time


# In[ ]:


data_2019 = pd.read_excel('Formula 1.xlsx',sheet_name = '2019')
data_2018 = pd.read_excel('Formula 1.xlsx',sheet_name = '2018')
data_2017 = pd.read_excel('Formula 1.xlsx',sheet_name = '2017')
data_2016 = pd.read_excel('Formula 1.xlsx',sheet_name = '2016')


# In[ ]:


#The following function turns the races 1-21 into an array containing all drivers. This Group_Gen allows 
#the combination function to find all correpsonding combinations 

def Group_Gen(df_arr,df):
    Group = []
    for i in range(len(df.columns[2:-1])):
        Group.append(df_arr[:,[1,2+i]])
    return Group

def Names_Gen(Names,ok):
    finale = np.zeros(len(Names))
    for j in range(len(finale)):
        finale[j] = (np.count_nonzero(Names[j] == ok[:,0,0,0]))/len(ok)        
    return finale
                
def Process_Gen(ok,i):
    
    for j in range(len(ok[i])): #length of combinatoins per box, 1,2,3,4,5
        if j==0:
            K = (ok[i,j])
            M = K[:,1]
            N = K[np.argmax(M),0]
            
        if j>0:
            Q = ok[i,j,:,1:]
            K = np.append(K,Q,axis=1)
            
            for z in range(len(K)):
                K[z,1] = np.sum(K[z,1:],axis=0)
                
            K = np.delete(K,np.s_[2:],axis=1)
            M = K[:,1]
            
            if len(np.argwhere(M ==np.amax(M))) == 1:
                N = K[np.argmax(M),0]
           
    return N 


# In[ ]:


def Probability_Gen(df):
    
    df_arr = np.array(df)
    Names = df_arr[:,1]
    Group = Group_Gen(df_arr,df)

    for e in range(len(df.columns[2:-1])):

        start = time.time()
        
        ok = np.array(list(itertools.combinations(Group,e+1))) #possibly 1,2,3,4,5 etc
        length = len(ok)
        for i in range(len(ok)): 
            ok[i] = Process_Gen(ok,i)
            
        finale = Names_Gen(Names,ok)
                
        for i in range(len(finale)):
            df_arr[i,2+e] = finale[i]
            
        end = time.time()
        print(end - start)
        df = pd.DataFrame(df_arr)
        
    return df


# In[ ]:


Data_2019 = Probability_Gen(data_2019)


# In[ ]:




