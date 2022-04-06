#!/usr/bin/env python
# coding: utf-8

# In[4]:


string = input()

string.find(" ")

print(string[string.find(" ")+1:], string[:string.find(" ")])

