#!/usr/bin/env python
# coding: utf-8

# In[2]:


x = int(input())
p = int(input())
y = int(input())
a = 0 
x = x * 100
y = y * 100


while x < y:
    x = int(x + x*(p/100))
    a += 1

else:
    print(a)

