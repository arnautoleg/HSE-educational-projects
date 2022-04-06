#!/usr/bin/env python
# coding: utf-8

# In[7]:


A = int(input())
B = int(input())
C = int(input())

if A > B and A > C or A == B and A == C:
    print(A)
elif B > A and B > C:
    print(B)
else:
    print(C)
    
    

