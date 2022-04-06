#!/usr/bin/env python
# coding: utf-8

# In[5]:


list_1 = input().split()
list_1 = [int(i) for i in list_1]
k = int(input())

list_1.pop(k)

for i in range(len(list_1)):
    print(list_1[i], end = " ")

