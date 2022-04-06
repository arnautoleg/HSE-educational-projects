#!/usr/bin/env python
# coding: utf-8

# In[2]:


n = int(input())
factorial = 1
sum = 0

for i in range (1, n+1):
    factorial *= i
    sum += factorial
    
print(sum)

