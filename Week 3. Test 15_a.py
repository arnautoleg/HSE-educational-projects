#!/usr/bin/env python
# coding: utf-8

# In[8]:


A = int(input())
B = int(input())
a = []

for i in range (A, B+1):
    if i // 1000 == i % 10 and (i % 100) // 10 == (i % 1000) // 100:
        a += [i]
for j in a:
    print(j)

