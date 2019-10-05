#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd 
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99] 
bsdegrees = [1,1,0,0,1] 
msdegrees = [2,1,0,0,0] 
phddegrees = [0,1,0,0,0]

GradeList = zip(names,grades,bsdegrees,msdegrees,phddegrees)
df = pd.DataFrame(data=GradeList, columns = ['Name' ,'Grades','BS Degree','MS Degree', 'PHD Degree'])
df


# In[13]:


df.count()


# In[14]:


df.mean()


# In[15]:


df.std()


# In[7]:


df.min()


# In[8]:


df.max()


# In[16]:


df.quantile(.25)


# In[17]:


df.quantile(.5)


# In[18]:


df.quantile(.75)

