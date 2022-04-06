#!/usr/bin/env python
# coding: utf-8

# In[11]:


n = int(input())

def primary(n):
    res = "YES"
    for i in range (1, n):
        for j in range (1, n):
            if i * j == n:
                res = "NO"
    if n <= 0: res = "NO"
    return res
print(primary(n))


# In[ ]:




