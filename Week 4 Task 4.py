#!/usr/bin/env python
# coding: utf-8

# In[6]:


list_1 = input().split()
list_1 = [int(i) for i in list_1]
k, C = input().split()

list_1.insert(int(k), int(C))

for i in range(len(list_1)):
    print(list_1[i], end = " ")

