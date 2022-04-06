#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input())
print("+___ "*n)
for i in range (1, n+1):
    print(f"|{i} / ", end = "")
print()
print( "|__\\ "*n)
print("|    "*n)

