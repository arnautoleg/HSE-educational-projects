#!/usr/bin/env python
# coding: utf-8

# In[13]:


string = input()
a = 0 

if len(string)%2 == 0: a = int(len(string)/2 - 1)
else: a = int(len(string)//2)

new_string = string[a+1:] + string[:a+1]

print(new_string)
    

