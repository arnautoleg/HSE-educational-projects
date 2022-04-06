#!/usr/bin/env python
# coding: utf-8

# In[ ]:


N = int(input())
a = "@gmail.com"
b = []

for i in range (N):
    mail = input()
    if a in mail:
        b += [mail]

for j in b:
    print(j)

