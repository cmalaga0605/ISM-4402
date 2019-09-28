#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd 

location = "datasets/gradedata.csv"
df = pd.read_csv(location)

bins = [0 , 60 , 70 , 80 , 90 , 100]
group_names = ['F' , 'D' , 'C' , 'B' , 'A']
df['letter grade'] = pd.cut(df['grade'] , bins , labels = group_names)

df.head()
                            


# In[29]:


bins = [0,80,100]
status_names = ['Fail' , 'Pass']
df['status'] = pd.cut(df['grade'] , bins , labels = status_names)
df


# In[30]:


pd.value_counts (df['status'])


# In[ ]:




