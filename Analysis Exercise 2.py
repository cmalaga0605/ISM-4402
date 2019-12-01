#!/usr/bin/env python
# coding: utf-8

# In[52]:


import pandas as pd                         #Use the pandas library 
Location = "datasets/axisdata.csv"          #Set Location variable equal to the dataset
df = pd.read_csv(Location)                  #declare the dataframe
df.head()                                   #print the dataframe and see the first 5 rows 


# In[40]:


df['Cars Sold'].mean()              # Get the average of the column Cars Sold


# In[41]:


df['Cars Sold'].max()              #Get the maximum value of the Cars Sold Column


# In[42]:


df['Cars Sold'].min()             #Get the minimum of the Cars Sold Column 


# In[43]:


pd.pivot_table(df,values = ['Cars Sold'] , index = ['Gender'])       #Create a pivot table to see the average cars sold by gender 


# In[44]:


df[df['Cars Sold']>3] ['Hours Worked'].mean()   #Average Hours worked by more then three cars sold per month


# In[46]:


df['Years Experience'].mean()                  #Average years of experience


# In[47]:


df[df['Cars Sold']>3]['Years Experience'].mean()       #Average Years of experience by more than three cars sold per month 


# In[397]:


pd.pivot_table(df,values = ['Cars Sold'] , index = ['SalesTraining']) #Created pivot table of Cars sold if they obtained sales training or not


# In[718]:


import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')
Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)

df.hist(column = 'Cars Sold')
plt.xlabel("Cars Sold Per Month")
plt.ylabel("# Sales Representitives")
df.hist(column = 'Cars Sold' , by = 'SalesTraining' , color = 'skyblue')





# In[36]:


import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib 
Location = 'datasets/axisdata.csv'
df = pd.read_csv(Location)

get_ipython().run_line_magic('matplotlib', 'inline')
df2 = df[df['Cars Sold']>=3] 
values = df2['Cars Sold']
index = df2['Hours Worked']

plt.figure(figsize=(10,10))
plt.ylabel("Hours")
plt.yaxis = index
matplotlib.rc('xtick', labelsize=10) 
matplotlib.rc('ytick', labelsize=10) 
plt.xlabel("Cars Sold")
plt.title("How Many Hours To Sell Seven Cars ? ")
plt.xaxis = values
plt.scatter(values, index)


displayText = "You have to atleast work more than 30 hr to sell seven cars"
xloc = 0.955
yloc = df['Hours Worked'].mean()
xtext = 8
ytext = -150  
plt.annotate(displayText, 
            xy=(xloc, yloc), 
            arrowprops=dict(facecolor='black', shrink=0.05),   
            xytext=(xtext,ytext),
            xycoords=('axes fraction', 'data'),
            textcoords='offset points')

plt.show()


# In[37]:


import pandas as pd 
Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)

df.corr()


# In[51]:


pd.pivot_table(df,index=['Cars Sold'], values = ['Years Experience'], aggfunc= 'min')

