#!/usr/bin/env python
# coding: utf-8

# In[14]:


def primary(n):
    res = "YES"
    for i in range (1, n):
        for j in range (1, n):
            if i * j == n:
                res = "NO"
    return res

