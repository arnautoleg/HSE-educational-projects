#!/usr/bin/env python
# coding: utf-8

# In[5]:


string = input()

new_string = string.upper()

if len(new_string)%2 == 0:
    if new_string[:int(len(new_string)/2)] == new_string[:int(len(new_string)/2)-1:-1]: print("YES")
    else: print("NO")
else: 
    if new_string[:int(len(new_string)//2)] == new_string[:int(len(new_string)//2):-1]: print("YES")
    else: print("NO")

