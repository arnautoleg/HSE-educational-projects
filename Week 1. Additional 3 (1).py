#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math

P = float(input())
X = int(input())
Y = int(input())
K = int(input())
T = X*100 + Y

for i in range (K):
    T = T*(1+P/100)
    print(T)
    T = math.floor(T)
    
      
#print(T//100, T%100)

