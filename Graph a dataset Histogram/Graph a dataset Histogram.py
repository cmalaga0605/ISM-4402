#!/usr/bin/env python
# coding: utf-8

# In[9]:


import matplotlib.pyplot as plt
import pandas as pd 
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "datasets/gradedata2.csv"
df = pd.read_csv(Location)

df.head()


# In[10]:


df.hist()


# In[11]:


df.hist(column="age")


# In[12]:


df.hist(column="age", by="gender")


# In[ ]:




