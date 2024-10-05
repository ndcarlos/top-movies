#!/usr/bin/env python
# coding: utf-8

# # Get a project up!

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


# In[2]:


# install chunk


# In[4]:


dat = pd.read_csv('/Users/noahcarlos/Documents/Projects/Python/Top Rated Movie 10.24/movie.csv')
dat


# In[5]:


print(dat.info())


# In[6]:


dat['popularity'].describe()


# ###### not sure about the histogram below. need a better understanding of what the meta data is. definitions

# In[7]:


# Popularity Histogram

pop_filter = dat[(dat['popularity'] >= 0) & (dat['popularity'] <= 200)]
plt.hist(pop_filter['popularity'], bins = 50)
plt.show()


# In[8]:


dat['vote_average'].describe()


# In[38]:


sns.histplot(dat, x = 'vote_average', bins = 10)
plt.show()


# In[41]:


# Ratings Histogram

mu, std = norm.fit(dat['vote_average'])

plt.hist(dat['vote_average'], bins = 10, density = True)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth = 2)



# ##### no bins! maybe something to mention in analysis

# ### Most popular _____

# In[47]:


# 10 most popular movies


mp_movies = dat.sort_values(by = 'vote_average', ascending = False)

mp_movies.head(10)


# In[ ]:


# bar graph of release_date v popularity


sbn.histplot



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




