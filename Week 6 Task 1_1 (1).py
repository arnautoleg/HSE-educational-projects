#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = float(input())
b = float(input())
operator = str(input())

def calc(a, b):
    if operator == "+": rez = a+b
    elif operator == "-": rez = a-b
    elif operator == "/": rez = a/b
    elif operator == "*": rez = a*b
    return rez

print(calc(a,b))

