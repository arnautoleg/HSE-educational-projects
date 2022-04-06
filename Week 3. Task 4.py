#!/usr/bin/env python
# coding: utf-8

# In[16]:


n = int(input())
f = 1
F = 1
a = 2

while a < n:
    f, F = F, F+f
    a += 1
print(F)

