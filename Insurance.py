#!/usr/bin/env python
# coding: utf-8

# In[7]:


from numpy.random import binomial

def insurance(n):
    sample = binomial(1, 0.9, size = n)
    
    def count_frequences(data, relative=False):
        counter = {}
        for element in data:
            if element not in counter:
                counter[element] = 1
            else:
                counter[element] += 1
        if relative:
            for element in counter:
                counter[element] /= len(data)
        return counter
    
    count = count_frequences(sample)
    
    
    def without_insurance(count):
        exp_x = count.get(1)*100 + count.get(0, 0)*(-200)
        return exp_x
    
    def with_insurance(count):
        exp_y = count.get(1)*70 + count.get(0, 0)*(-30)
        return exp_y
                
    res_x, res_y = without_insurance(count), with_insurance(count)     
    
    var_x = (0.9*((100 - res_x)**2)+0.1*((-200-res_x)**2))**0.5
    var_y = (0.9*((100 - res_y)**2)+0.1*((-30-res_y)**2))**0.5
    
    if res_x > res_y:
        print("Insurance is cost-efficient!")
    elif res_x < res_y:
        print("Insurance is NOT cost-efficient!")
    else:
        print("Insurance does't inluence")
    
    case_x = res_x / n
    case_y = res_y / n
    
    print("Without insurance 1 launch costs", case_x, '\n' "Standart dev", var_x)
    print("With insurance 1 launch costs ", case_y, '\n' "Srandart dev", var_y)


# In[12]:


insurance(90)


# In[ ]:




