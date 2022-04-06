#!/usr/bin/env python
# coding: utf-8

# In[16]:


n = int(input())

#Write a function phib(n) that returns the n-th Fibonacci number for a given non-negative integer n. 
#Do not use loops in this task, use recursion instead.


def phib(n):
    if n == 0: ans  = 0
    elif n == 1: ans = 1
    elif n == 2: ans = 1
    else: ans = phib(n-1) + phib(n-2)
    return ans

print(phib(n))


#0 1 1 2 3 5 8 13 21 34 55

