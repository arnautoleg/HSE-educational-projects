#!/usr/bin/env python
# coding: utf-8

# In[14]:


IP = str(input())
block = IP.split('.') 
l = len(block)
sum = 0

result = True

if IP[-1] != ".":
    for i in range(l):
        sum += int(block[i])

if l != 4 or sum == 0:
    result = False

    else:
    for  i  in  range(l):
        if 0 <= int(block[i]) < 255:
            continue
        else:
            result = False
            break

if result:
    print("YES")
else:
    print("NO")

