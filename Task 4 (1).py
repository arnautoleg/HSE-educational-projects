#!/usr/bin/env python
# coding: utf-8

# In[9]:


import math

P = int(input())
X = int(input())
Y = int(input())
K = int(input())
T = X*100 + Y

for i in range (K):
    #T = T*(1+P/100)
    T = int(T+(float(T)*P)/100)
    T = math.floor(T)
       
print(T//100, T%100)

