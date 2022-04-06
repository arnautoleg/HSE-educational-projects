#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = int(input())
n = int(input())

def power(a, n):
    rez = a
    for i in range(2, n+1):
        rez *= a
    return rez

print(power(a, n))

