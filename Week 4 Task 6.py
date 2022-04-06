#!/usr/bin/env python
# coding: utf-8

# In[33]:


list_1 = input().split()
list_1 = [int(i) for i in list_1]


for i in range (len(list_1)):
    if i == 0 and list_1[i] not in list_1[1:]: print(list_1[i], end = " ")
    elif 0 < i < len(list_1) and (list_1[i] not in list_1[:i] and list_1[i] not in list_1[(i+1):]): print(list_1[i], end = " ")
    elif i == len(list_1) and list_1[i] not in list_1[:i]: print(list_1[i], end = " ")

