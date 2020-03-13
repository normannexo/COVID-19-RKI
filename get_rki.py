import pandas as pd
import datetime
import numpy as np
import os

now = datetime.datetime.now()
curr_minute = now.strftime("%Y-%m-%d %H:%M")
dir_path = os.path.dirname(os.path.abspath(__file__))
print(dir_path)

csv_file = dir_path + '/csv/rki_' + now.strftime('%Y-%m-%d_%H_%M') + '.csv'
print(curr_minute)
url = 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html'
columns = ['Bundesland', 'confirmed', 'confirmed_el', 'extra']
df = pd.read_html(url)[0]
df.columns = columns
df['date'] = pd.to_datetime(curr_minute)
print(df)
df.to_csv(csv_file)

