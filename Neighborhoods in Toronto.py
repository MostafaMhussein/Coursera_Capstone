#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import the required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


# In[3]:


wiki_url = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'


# In[6]:


#  Get the requested page
page = requests.get(wiki_url)


# In[7]:


# Get the text data from the response object
data = page.text


# In[8]:


soup = BeautifulSoup(data)


# In[9]:


wiki_table = soup.find('table')
wiki_table


# In[11]:


# Extract the table rows
table_row = wiki_table.find_all('tr')


# In[13]:


# Get the data from each table row

dataframe = []
for row in table_row:
    table_data = row.find_all('td')
    data = [i.text.rstrip() for i in table_data]
#     print(data)
    dataframe.append(data)

dataframe 
del dataframe[0]


# In[14]:


# Declare labels to assign to the dataframe
labels = ['Postcode', 'Borough', 'Neighborhood']


# In[15]:


# Create pandas dataframe and load it with data
wiki_table_df = pd.DataFrame.from_records(dataframe, columns=labels)


# In[16]:


# Remove the data cells with 'Not assigned' value in Borough
wiki_table_df = wiki_table_df[wiki_table_df.Borough != 'Not assigned']


# In[17]:


# Replace the 'Not assigned' in Neighborhood with the respective Borough values.
wiki_table_df.Neighborhood = wiki_table_df.Neighborhood.replace('Not assigned', wiki_table_df.Borough)  


# In[18]:


# Group Neighborhoods with same Postalcodes
wiki_table_df = wiki_table_df.groupby(("Postcode", "Borough")).agg(','.join)
    


# In[19]:


wiki_table_df


# In[ ]:




