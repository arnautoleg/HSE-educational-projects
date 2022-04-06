#!/usr/bin/env python
# coding: utf-8

# Click-Through Rate (CTR) is calculated as “CTR = [Total Measured Clicks / Total Measured Ad Impressions] X 100”, 
# where “total measured clicks” is the total amount of clicks on an ad; 
# “total measured ad impressions” is the number of times an ad was loaded on a page. 
# Click-through rates measure how successful an ad has been in capturing users' attention. 
# The higher the click-through rate, the more successful the ad has been in generating interest.

# In[11]:


def CTR_determination(a, b):  
    if b == 0: return """Total Measured Ad Impressions = 0. 
Click-Through Rate can not be calculated"""
    elif a == 0: return "Click-Through Rate = 0%"
    return f'Click-Through Rate = {(a*100)/b:.3f} %'
    
# TMC - Total Measured Clicks
# TMAI = Total Measured Ad Impressions

TMC = int(input())
TMAI = int(input())

print(CTR_determination(TMC, TMAI))


# Return on Investment (ROI) is calculated as “[(Amount Gained – Amount Spent) / Amount Spent] X 100”, where “amount gained” is the amount of income that has been generated by an investment; “amount spent” is the total amount spent on an investment. ROI stands for Return on Investment and means the amount of money you get back relative to the amount of money you put into something. It is different to profit, which is simply the amount spent subtracted from the amount earned. ROI goes a step further and works out profit per the amount spent. This answers the question – how much profit can I earn per pound/dollar/euro etc spent.

# In[21]:


def ROI_determination(a, b):
    if b == 0: return "Amount Spent = 0, Return on Investment can not be calculated"
    elif a < b: return f'Return on Investment (Investment Loss){(a-b)*100/b:.1f} %'
    return f'Return on Investment (Investment Gain){(a-b)*100/b:.1f} %'

# AG - Amount Gained 
# AS - Amount Spent

AG = float(input())
AS = float(input())

print(ROI_determination(AG, AS))


# Average Page Time is calculated as “Average Page Time = [Σ(Time Spent on a Page by a User) / Number of Users]”, where “time spent on a page by a user” is time measured for each user who visits a webpage; “number of users” is the number of users who visit a webpage. Keep in mind, that usually users who spend less than 5 seconds on a webpage are not included in the calculations. Hint! You might think about parameters passed to a function as one of Python series structures. 
# 

# In[23]:


def APT_determination(my_list):
    theSum = 0
    user= 0
    for i in my_list:
        if i > 4: 
            theSum  += i
            user += 1
    if user == 0: return """Average Page Time can not be estimated.
All users spend less than 5 s"""
    rez = theSum/user
    return f"Average Page Time = {int(rez//60)} min and {int(rez%60)} s"
    
# theSum - Σ(Time Spent on a Page by a User)
# user - Number of Users

a = [item for item in input().split()]
a = [int(i) for i in a]

print(APT_determination(a))


# Customer Lifetime Value (CLV) is calculated as “CLV = [(Average Purchase Value – Average Purchase Frequency) X Average Customer Lifespan]” and used to predict how much revenue a customer will drive over time. To get more information how this metric is calculated, follow this link.

# In[4]:


# APV - Average Purchase Value
# TR - Total Revenue 
# NP - number of Purchases
# APF - Average Purchase Frequency
# UC - Unique Customers
# ACL - Average Customer Lifespan

def CLV_determination(a, b, c, ACL):
    APV = a/b
    APF = b/c
    return f'Customer Lifetime Value = {(APV-APF)*ACL:.1f} $'

TR = float(input())
NP = int(input())
UC = float(input())
ACL = float(input())


print(CLV_determination(TR, NP, UC, ACL))


# Conversion Rate (CR) which is calculated as “CR = [Total Attributed Conversion / Total Measured Clicks] X 100”, where “total attributed conversion” is the total amount of conversion recorded which have been caused clicks; “total clicks” – number of times an ad was clicked on.

# In[11]:


def CR_determination(a, b):
    if b == 0: return """Conversion Rate = 0. 
Conversion Rate can not be calculated"""
    elif a == 0: return "Conversion Rate = 0%"
    return f'Conversion Rate = {(a*100)/b:.1f} %'

# TAC - Total Attributed Conversion
# TMC = Total Measured Clicks

TAC = int(input())
TMC = int(input())

print(CR_determination(TAC, TMC))


# Yearly Sales Growth Rate (TSGR) shows how your sales are increasing in terms of a yearly basis. This metric will show you a picture of how your business has grown over the years or experiencing a downward trend.
# 
# Yearly Sales Growth Rate = [(Current Year Sale - Last Year Sale)/Last Year Sale]*100

# In[1]:


def TSGR_determination(a, b):
    if b == 0: return """Last Year Sale = 0. 
TSGR can not be calculated"""
    return f'Yearly Sales Growth Rate = {((a-b)/b)*100:.1f} %'

# CYS - Current Year Sale 
# LYS - Last Year Sale

CYS = float(input())
LYS = float(input())

print(TSGR_determination(CYS, LYS))


# Sales Value (Average). This measure will let you know about the average deal size of your sales made to the customers and how much effort will be required to break even or meet the costs.
# 
# The best practice for using this measure is to segment your customers into large deals, medium deals and small deals (or as required by your business). This helps avoid skewness in the deal sizes and eliminating the effect of outliers.
# 
# Sales Value (Average) = [Total Sales value or Total Sales value in the segment/ Number of sales (units) or sales in the segment]

# In[18]:


def SV_determination(a, b):  
    if b == 0: return """Number of sales = 0. 
Sales Value can not be calculated"""
    elif a == 0: return "Sales Value = 0 $"
    return f'Sales Value = {a/b:.2f} $'
    
# TSV - Total Sales Value
# N = number of sales

TSV = int(input())
N = int(input())

print(SV_determination(TSV, N))


# Net Promoter Score (NPS) is the most important business metric for sales team. This is the measure of how likely your customers are willing to recommend your product or service to their others (friends and family).
# 
# There are different ways to calculate NPS but the most popular way to calculate it is with the help of a customer survey. The customer survey asks about how likely it is that they would refer your business, brand or product to their social circle.
# 
# NPS usually uses a scale of 0 to 10, with 10 being Extremely likely to recommend and 0 being extremely unlikely to recommend. You can measure the percentages of people from 0 to 6 as being the detractors and 7 to 10 as being the promoters. The difference among both percentages will give you the Net Promoter Score (NPS).
# 
# Net Promoter Score (NPS) = [Promoters % – Detractors %]
# 

# In[3]:


def NPS_determination(my_list):  
    det, pro = 0, 0
    for i in range (len(my_list)):
        if my_list[i]<7: det += 1
        else: pro += 1
    return f'Net Promoter Score = {((pro - det)*100)/(pro + det)} %'
    #return det, pro

a = [item for item in input().split()]
a = [int(i) for i in a]

print(NPS_determination(a))


# In[2]:


((60-40)*100)/100


# In[20]:


((20-10)*100)/100

