#!/usr/bin/env python
# coding: utf-8

# In[2]:


A = int(input())
B = int(input())

if A < B:
    for i in range (A, B+1):
        print(i, end = " ")
else:
    for i in range (A, B-1, -1):
        print(i, end = " ")

