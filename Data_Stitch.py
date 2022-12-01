# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 11:05:33 2021

@author: Greg.Kelly
"""

import pandas as pd
import numpy as np
import re
import os
import matplotlib.pyplot as plt

filepath = 
Test_ID = 'Test_ID_15_speed_ramp'
p=re.compile(Test_ID + '\s\d{4}_\d{2}_\d{2}\s\d{2}_\d{2}_\d{2} mean \(5 Hz\) 0\.lvm')
df=pd.DataFrame()

for root,dirs, files in os.walk(filepath):
    for file in files:
        if p.match(file):
            name = file
            modified    = os.path.getctime(filepath + '\\' +name)
            df0=pd.read_csv(filepath+ '\\'+ name,sep =" ",header = None)
            df=df.append(df0)
            #print(name,modified)
        

#time=df.iloc[:,5]
df=df.reset_index(drop=True)
#x=np.linspace(0,len(df),len(df))
cof=df.iloc[:,7]
df['cycle']=[1 if x>0 else 0 for x in cof]
plt.plot(df.index,cof)
plt.xlabel('Cycle')
plt.ylabel('CoF')
plt.title(Test_ID)
plt.savefig(filepath+'\\'+Test_ID,dpi=250)
df.to_csv(filepath+'\\'+Test_ID +'.csv')
'''
sign_change=0
cycle=0
rms=0
start=0
while sign_change<2:
 for i in range(start,len(df)):
   #x=cof[i]**2
   #rms=rms+x
  cycle1=df.cycle[i] 
  if cycle1 != cycle:
            sign_change=sign_change+1
            print(sign_change)
'''        
