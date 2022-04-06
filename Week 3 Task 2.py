#!/usr/bin/env python
# coding: utf-8

# In[9]:


N = int(input())
n = 0

while 2**n <= N:
    print(2**n, end = " ")
    n += 1

