#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Load the following libraries : Pandas
import pandas as pd


# In[2]:


pd


# In[3]:


# Read the data file
df = pd.read_excel('HollywoodsMostProfitableStories.xlsx')
df


# In[4]:


#Inspect the data frame using frequently used functions
df.head()


# In[5]:


df.tail()


# In[12]:


df.describe()


# In[14]:


df.shape


# In[15]:


df.info()


# In[17]:


df.columns


# In[6]:


df.drop_duplicates()


# In[7]:


df.dropna()
df


# In[8]:


df_cleaned=df.dropna()
df_cleaned


# In[10]:


df_cleaned.to_csv(r'C:\Users\rizwa\OneDrive\Desktop\Assignment-Python\HollywoodsMostProfitableStoriesCleaned.csv')


# In[11]:


df_cleaned.to_excel(r'C:\Users\rizwa\OneDrive\Desktop\Assignment-Python\HollywoodsMostProfitableStoriesCleaned.xlsx')

