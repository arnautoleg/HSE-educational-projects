#!/usr/bin/env python
# coding: utf-8

# In[5]:


col = int(input())
row = int(input())
col_1 = int(input())
row_1 = int(input())

if abs(row - row_1) == abs(col - col_1):
  print ("YES")
else:
  print ("NO")

