#!/usr/bin/env python
# coding: utf-8

# In[10]:


def primary(n):
    res = "NO"
    for i in range (1, n):
        for j in range (1, n):
            if i * j == n:
                res = "YES"
    return res

