#!/usr/bin/env python
# coding: utf-8

# In[70]:


def sum_of_two_numbers(a, b):
    if b == 0:
        return a
    else:
        return sum_of_two_numbers(a + 1, b - 1)

a = int(input())
b = int(input())

print(sum_of_two_numbers(a, b))

