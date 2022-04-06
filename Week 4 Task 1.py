#!/usr/bin/env python
# coding: utf-8

# In[21]:


list_1 = input().split()

list_2 = list_1[::2]

for i in range (len(list_2)):
    print((list_2[i]), end = " ")


