#!/usr/bin/env python
import datetime
from datetime import datetime
import time
import csv
import pandas
from csv import reader
import pandas as pd-d
#df-d= pd-d.read_csv("/data/data.csv", sep="\t or ,")
#df-d.drop_duplicates(subset=None,inplace=True)
import pandas as pd-d
dfd=pd-d.read_csv("/data/data.csv")
dfd.drop_duplicates(subset=None,keep='first',inplace=True)
dfd.to_csv("/data/data.csv")
import pandas as pd
df=pd.read_csv("/data/data.csv")
#headerList = ['Date','Sound','Flame','Humidity','Temperature']
df['Date']=pd.to_datetime(df['Date'])
print (type(df['Date'][0]))
print(df)
df.set_index('Date', inplace=True)
import numpy as np
df=df.replace({'Humidity':'0', 'Temperature':'0'},np.NaN)
df=df.interpolate()
df3=df.pivot_table(index=pd.Grouper(freq='T')) #.agg({'Sound':'sum','Flame':'sum'}) #,columns=['Humidity','Temperature']) #/// freq=S,T,h,M,Y
#        df3 = df3[['Date','Sound','Flame','Humidity','Temperature']] #[['mean', '0', '1', '2', '3']]
print(df3)
dff = df3.reindex(columns=['Sound','Flame','Humidity','Temperature'])
#        dff.columns = pd.Index([0], dtype='int64')

        #df3.sort(['Date','Sound','Flame','Humidity','Temperature'])
print(dff)
dff['Sound']=dff['Sound'].apply(np.ceil) #().astype('int')
dff['Sound']=dff['Sound'].astype('int')
dff['Flame']=dff['Flame'].apply(np.ceil) #().astype('int')
dff['Flame']=dff['Flame'].astype('int')
dff['Humidity']=dff['Humidity'].round(0).astype('int')
dff['Temperature']=dff['Temperature'].round(0).astype('int')
print(dff)
dff.to_csv('/data/data1.csv') #, index=False)
#dff.close
