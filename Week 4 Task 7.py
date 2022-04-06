#!/usr/bin/env python
# coding: utf-8

# In[8]:


list_1 = input().split()
list_1 = [int(i) for i in list_1]
X = int(input())
   
list_1.append(X)
list_1.sort()

for i in range (0, len(list_1)-1):
    if list_1[i] == X and list_1[i] <= list_1[i+1]:
        a = i
        break
result = len(list_1) - a

print(result)

