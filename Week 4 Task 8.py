#!/usr/bin/env python
# coding: utf-8

# In[12]:


list_1 = input().split()
list_1 = [int(i) for i in list_1]
list_2 = input().split()
list_2 = [int(i) for i in list_2]
list_3 = input().split()
list_3 = [int(i) for i in list_3]
list_4 = input().split()
list_4 = [int(i) for i in list_4]
list_5 = input().split()
list_5 = [int(i) for i in list_5]
list_6 = input().split()
list_6 = [int(i) for i in list_6]
list_7 = input().split()
list_7 = [int(i) for i in list_7]
list_8 = input().split()
list_8 = [int(i) for i in list_8]

list_total = list_1 + list_2 + list_3 + list_4 + list_5 + list_6 + list_7 + list_8

hor = [list_total[i] for i in range (len(list_total)) if i%2 == 1]
vert = [list_total[i] for i in range (len(list_total)) if i%2 == 0]
total = [(list_total[i] + list_total[i-1]) for i in range (16) if i%2 == 1]
a = 0

if sorted(hor) == [1, 2, 3, 4, 5, 6, 7, 8] and sorted(vert) == [1, 2, 3, 4, 5, 6, 7, 8]:
    for i in range (8):
        if i == 0 and total[i] in total[1:]: a = 1
        elif 0 < i < len(total) and (total[i] in total[:i] and total[i] in total[(i+1):]): a = 1
        elif i == len(total) and total[i] in total[:i]: a = 1
else: a = 1
    
if a == 0: print("NO")
else: print("YES")


# In[5]:


sum_1

