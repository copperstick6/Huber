
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

import numpy as np


# In[3]:

df_catalog = pd.read_csv('catalog.csv',encoding="ISO-8859-1")
df_catalog.head()


# In[7]:

df_transactions = pd.read_csv('10000_transactions.csv',encoding="ISO-8859-1")
df_transactions.head()


# In[14]:

len(set(df_transactions['product_id']))


# In[18]:

df_products = df_transactions['product_id']
df_products.head()


# In[70]:

cust_id = 135442
transactions = df_transactions[df_transactions['customer_id'] == cust_id]
transactions.head()
#use .item
# Go through all transactions and find most popular for 


# In[87]:

department = transactions['department_id'].value_counts().first_valid_index()
products = df_catalog[df_catalog['department_id'] == department]

rec_prod_list = products['prod_name'].head(1)
rec_prod = rec_prod_list.item()
print(rec_prod)


# In[ ]:



