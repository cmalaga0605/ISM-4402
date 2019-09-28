#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
location = 'datasets\gradedata.csv'
df = pd.read_csv(location)
df.head()


# In[5]:


import numpy as np
df['timemgmt'] = np.where((df['exercise'] > 3) & (df['hours'] > 17) , 'busy', 'normal')
df.tail(20)


# In[6]:


pd.value_counts (df['timemgmt'])


# In[ ]:




