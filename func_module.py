#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import numpy as np
import pycountry_convert as pc
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns


# In[ ]:


# Generat word cloud

def generate_word_cloud(column,colour):
    
    words = ''
    for i in column:
        try:
            a=i.split(';')
            for j in a:
                words+=' '+ j
        except:
            a=-999

    word_cloud = WordCloud(background_color=colour,max_font_size=300,width=2000, height=1080).generate(words)
    plt.figure(figsize=(30,8))
    return plt.imshow(word_cloud)


# In[ ]:



# Generate satisfaction data


def genrate_satisfaction_data(df,colname1,colname2):
    arr = ['Very satisfied', 'Slightly satisfied', 'Slightly dissatisfied',
            'Very dissatisfied', 'Neither satisfied nor dissatisfied']
    for i in arr:
        try:
            filt = (df[colname1] == i)
            satReport = df.loc[filt, colname2].value_counts().head()
            print(i +' developer with their '+ colname1.replace('Sat', '')+'\n', satReport)
        except:
            return []


# In[ ]:



# Generate a continent array with country

def get_continent(col):
    continent = []
    for i in col:
        try:
            cn_a2_code =  pc.country_name_to_country_alpha2(i)
        except:
            cn_a2_code = 'Unknown' 
        try:
            continent.append(pc.country_alpha2_to_continent_code(cn_a2_code))
        except:
            continent.append('Unknown')

    return continent

