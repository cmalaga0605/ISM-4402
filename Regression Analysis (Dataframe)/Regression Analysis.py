#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd 
Location = 'datasets/gradedata.csv'
df = pd.read_csv(Location)

df.head()


# In[16]:


def gender_(x):
    if x == 'female':
        return 1 
    if x == 'male':
        return 0


# In[17]:


df ['gender_val'] = df['gender'].apply(gender_)
df.tail()


# In[22]:


import statsmodels.formula.api as sm
result = sm.ols(formula='grade ~ age + exercise + hours + gender_val', data=df).fit()
result.summary()


# In[25]:


import statsmodels.formula.api as sm
result = sm.ols(formula='grade ~ exercise + hours + gender_val', data=df).fit()
result.summary()


# In[ ]:




