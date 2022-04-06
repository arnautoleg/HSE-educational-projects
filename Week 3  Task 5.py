#!/usr/bin/env python
# coding: utf-8

# In[18]:


A = int(input())
f = 0
F = 1
a = 1


while A - F >= 0:
    if F != A:
        f, F = F, F+f
        a += 1
    else:
        print(a)
        break


else:
    if A == 0:
        print(a-1)
    else:
        print(-1)

