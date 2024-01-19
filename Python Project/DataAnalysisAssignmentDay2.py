#!/usr/bin/env python
# coding: utf-8

# •	Load the following libraries :
# 1.	Pandas
# 2.	Matplotlib
# 3.	Seaborn
# 

# In[1]:


import pandas as pd # for exploring data and basic plotting
import seaborn as sns # for data visualization and plotting importing seaborn & matplotlib
import matplotlib.pyplot as plt


# In[2]:


pd


# •	Read the data file and give it suitable name

# In[3]:


cl = pd.read_csv('cereal.csv')


# •	Inspect the data frame using frequently used functions. 

# In[4]:


cl.head()


# In[5]:


cl.tail()


# In[6]:


cl.describe()


# In[7]:


cl.shape


# In[8]:


cl.info()


# In[9]:


cl.columns


# In[10]:


cl.isna().sum()

# •	Create a Histogram for the distribution of calories
# In[11]:


cl.calories.hist()


# •	Visualize the distribution of 'vitamins' content in cereals. You can use a histogram for this

# In[12]:


cl.vitamins.hist()


# •	Find the correlation between Calories vs Protein.
# •	Visualize this using scatter plot.
# 

# In[27]:


cl.plot(x='calories',y='protein',kind='scatter')


# Create Boxplot for the following columns:
# 1.	Calories
# 2.	Fiber
# 3.	Sugars
# 4.	Carbohydrates
# 

# In[30]:


sns.boxplot(cl['calories'], orient = 'h')


# In[47]:


round(calories.describe(),2)


# In[31]:


sns.boxplot(cl['fiber'], orient = 'h')


# In[32]:


sns.boxplot(cl['sugars'], orient = 'h')


# In[33]:


sns.boxplot(cl['carbo'], orient = 'h')


# In[37]:


exclude_name = cl.iloc[0:77,4:15]
correlation = exclude_name.corr()
correlation


# In[40]:


exclude_name = cl.iloc[0:77,3:15]
correlation = exclude_name.corr()
correlation


# In[50]:


cal_no_out = cl[(cl["calories"]>80) & (cl["calories"]<130)]
cal_no_out_ = cal_no_out.iloc[0:77,3]
plt.boxplot(cal_no_out_, vert=False)


# In[42]:


cl["calories"].corr(cl["protein"])

