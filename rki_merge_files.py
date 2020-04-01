#!/usr/bin/env python

import pandas as pd
import datetime
import numpy as np
import os

dir_path = os.path.dirname(os.path.abspath(__file__))

CSVLOC=os.path.join(dir_path, 'csv', 'archive')
CSVOUT = os.path.join(dir_path, 'csv', 'rki_data.csv')

# create empty data frame and fill with tables from archive:
df_data = pd.DataFrame()
for item in os.listdir(CSVLOC):
    if os.path.isfile(CSVLOC + '/' + item):
        df_data = pd.concat([df_data,pd.read_csv(CSVLOC + '/' + item,  parse_dates=True)])
        print("added "+ CSVLOC + "/" + item + " to data frame.")
    else:
        print(item + " is no file")
# further wrangling:
df_data.deaths.replace({np.nan:0}, inplace=True)
df_data['date'] =pd.to_datetime(df_data.date).dt.date
df_data = df_data.drop(df_data[df_data.Bundesland=='Gesamt'].index)
df_data = df_data.drop(df_data[df_data.confirmed=='Fälle'].index)
df_data.confirmed = df_data.confirmed.astype(int)

#fixing different spellings of SH and MV:
df_data.Bundesland = df_data.Bundesland.str.strip()
df_data.Bundesland = df_data.Bundesland.replace({'Schleswig Holstein':'Schleswig-Holstein'})
df_data.Bundesland = df_data.Bundesland.str.replace(r'[^A-Za-zÄÖÜäöüß-]', r'')
df_data.deaths = df_data.deaths.astype(int)



# grouping to prevent duplicate entries for one day:
df_data = df_data.groupby(['Bundesland','date']).agg({'confirmed':'max', 'deaths':'max'})


df_data.to_csv(CSVOUT)




print(df_data)

