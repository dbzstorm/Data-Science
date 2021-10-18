#!/usr/bin/env python
# coding: utf-8

# In[22]:


url="https://www.sportskeeda.com/sports/tokyo-olympics-medal-tally"


# In[23]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize


# In[26]:


#df=pd.read_html(url,header=0)
MN = pd.read_html(url,header=0)
MN[0]#first table


# In[27]:


len(MN[0])


# In[28]:


MN[1]


# In[32]:




   
# Converting Pandas DataFrame
# into CSV file
MN[0].to_csv('Meek.csv')


# In[ ]:




