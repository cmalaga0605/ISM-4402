#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
Location = 'datasets/gradedata2.csv'

df = pd.read_csv(Location)
df.head()


# In[3]:


plt.scatter(df['hours'], df['grade'])


# In[ ]:




