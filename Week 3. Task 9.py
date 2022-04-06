#!/usr/bin/env python
# coding: utf-8

# In[3]:


n = int(input())
factorial = 1

for i in range (1, n+1):
    factorial *= i
    
print(factorial)

