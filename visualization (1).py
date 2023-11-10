#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd  #Inputing file (eg, pd.read_csv), Data-processing
import numpy as np  #Linear Algebra
import matplotlib.pyplot as plt  #Visualisation   
import warnings  #Supress warnings 
import seaborn as sns
from sklearn.linear_model import LinearRegression


# In[3]:


data = pd.read_csv("tuberculosis.csv",index_col = 0)


# In[4]:


data_frame = data.drop(['Country Code'],axis = 'columns')


# In[5]:


data_frame


# In[6]:


df = data_frame.reset_index(drop=True)
df


# In[7]:


df_t = data_frame.transpose()
df_t
df2 = df_t.reset_index(drop=True)
df2 = df2.shift(-1)
df2


# In[8]:


year = pd.Series([2013,2014,2015,
                   2016,2017,2018,2019,2020,2021], dtype = object)


# In[9]:


df2['year'] = year 
df2.columns = pd.Series(["Algeria", "Egypt,Arab Rep.","Iran,Islamic Rep.","Iraq","Israel","Kuwait","Saudi Arabia","year"],dtype = object)
df2


# In[10]:


final_Data_frame = df2.dropna()


# In[11]:



df_final = pd.concat([final_Data_frame.iloc[:, -1:], final_Data_frame.iloc[:, :-1]], axis=1)


# In[12]:


df_final.columns
df_final


# In[13]:


def linePlot(linePlotData):
    sns.set_style("whitegrid")  # seaborn style
    plt.figure(figsize=(20, 10))

    # Listing countries to plot
    countries = ["Algeria", "Egypt,Arab Rep.", "Iran,Islamic Rep.", "Iraq", "Israel", "Kuwait", "Saudi Arabia"]
    
    # Create DataFrame for plotting
    plot_df = linePlotData[['year'] + countries]

    # Visualizing through line plot
    plot_df.set_index('year').plot(marker='o')

    plt.title('Tuberculosis case detection rate of Middle east and south africa')
    plt.xlabel('Years')
    plt.ylabel('Tuberculosis case detection rate')
    plt.legend(countries, loc='best', fontsize= 'small')

# plotting for df_final
linePlot(df_final)
plt.show()


# In[14]:


def barPlot(barData):
    
    barData.plot(x = 'year', y = ['Algeria', 'Israel'],kind = 'bar',title= 'Comparison of Algeria and Israel Case Detection',
                 xlabel= 'Years', ylabel= 'Cases Detected', color = ('red', 'green'),legend = True, width=0.65)
    plt.figure(figsize=(16,6))
    plt.show()
    
    
barPlot(df_final)


# In[15]:


def boxPlot(df):
    # Melt the DataFrame to create a suitable format for the box plot
    melted_df = pd.melt(df, id_vars='year', var_name='Country', value_name='Case Detection')

    # Set seaborn style
    sns.set(style="whitegrid")

    # Create a box plot using seaborn
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Country', y='Case Detection', data=melted_df, showfliers=False)
    plt.title('Box Plot of Case Detection by Country')
    plt.xlabel('Country')
    plt.ylabel('Case Detection')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
    plt.show()
boxPlot(df_final)


# In[ ]:




