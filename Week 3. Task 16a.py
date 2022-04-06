#!/usr/bin/env python
# coding: utf-8

# In[1]:


b = str(input())
k = b.split('.') 
l = len(k)

ip = True

if l != 4:
    ip = False
else:
    for  i  in  range(l):
        if int(k[i])< 255 and int(k[i]) >= 0:
            continue
        else:
            ip = False
            break

if ip:
    print("YES")
else:
    print("NO")

