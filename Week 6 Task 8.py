#!/usr/bin/env python
# coding: utf-8

# In[6]:


d = int(input())

def sumb(num):
    if num == 0: 
        return 0
    return num%10 + sumb(num//10)
    
print(sumb(d))

