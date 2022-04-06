#!/usr/bin/env python
# coding: utf-8

# In[12]:


b = str(input())

k = b.split('.') # 

if len(k) != 4:
    result = "NO"
else:
    for i in k:
        while 0 < int(i) < 255:
            result = "YES"
        else:
            result = "NO"

print(result)
    

