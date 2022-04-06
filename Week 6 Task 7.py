#!/usr/bin/env python
# coding: utf-8

# In[14]:


num = int(input())

def factorial(num):
    if num == 0: 
        return 1
    res = num * factorial(num-1)
    return res

print(factorial(num))

    

