#!/usr/bin/env python
# coding: utf-8

# In[4]:


N = int(input())
sum = 0

for i in range (N):
    a = int(input())
    if a == 0:
        sum += 1
print(sum)

