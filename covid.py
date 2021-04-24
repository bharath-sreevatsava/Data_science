import pandas as pd 
import numpy as np 
import psycopg2
import urllib
import scipy
import psutil
import time
from datetime import timedelta,datetime,date

from querying import Querying


query_pre = """Select  *
                From covid as c 
                where """+"c.\"" +str('Date')+"\"" +""" >= '"""+ str("2020-01-01") +""" '
                    and """+"c.\"" +str('Date')+"\"" +""" < '""" +str("2021-01-01")+ """' """

query_post = """Select  *
                From covid as c 
                where """+"c.\"" +str('Date')+"\"" +""" >= '"""+ str("2021-01-01") +""" '
                    and """+"c.\"" +str('Date')+"\"" +""" < '""" +str("2022-01-01")+ """' """

df_post = Querying(query_post)
df_pre  = Querying(query_pre)

df_post['month'] = [df_post['Date'][i].month for i in range(len(df_post))]
df_post['year'] = [df_post['Date'][i].year for i in range(len(df_post))]

df_pre['month'] = [df_pre['Date'][i].month for i in range(len(df_pre))]
df_pre['year'] = [df_pre['Date'][i].year for i in range(len(df_pre))]

df_pre_post =  df_pre.append(df_post).reset_index(drop = True)

df_pre_post['time_tag'] = np.where(df_pre_post['year'] == 2021,"Post","Pre")
df_pre_post = df_pre_post[['Date','State/UnionTerritory',
       'confirmedindiannational', 'confirmedforeignnational', 'cured',   
       'deaths', 'confirmed', 'month', 'year','time_tag']]
df_agg =  df_pre_post.groupby(['State/UnionTerritory','month', 'year','time_tag']).sum().reset_index()
df_agg.to_csv('C:/Users/bpeda/Downloads/Covid_19_analysis_Bharath.csv')
print(df_agg)