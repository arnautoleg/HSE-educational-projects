#!/usr/bin/env python
# coding: utf-8

# In[40]:


list_1 = input().split()

for i in range(0, len(list_1)):
    list_1[i] = int(list_1[i])
max_value = max(list_1)


index = list_1.index(max_value)

max_value = int(max_value)
index = int(index)

print(max_value, index)


