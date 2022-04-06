#!/usr/bin/env python
# coding: utf-8

# In[4]:


list_1 = input().split()
list_1 = [int(i) for i in list_1]
list_2 = []
a = 0
for i in range(len(list_1)):
    if list_1[i] not in list_2: 
        a += 1
        list_2.append(list_1[i])       
print(a)
    

