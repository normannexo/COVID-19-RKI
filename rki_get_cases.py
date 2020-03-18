import pandas as pd
import datetime
import numpy as np
import os
import requests
from bs4 import BeautifulSoup

now = datetime.datetime.now()
curr_minute = now.strftime("%Y-%m-%d %H:%M")
dir_path = os.path.dirname(os.path.abspath(__file__))
print(dir_path)

csv_file = os.path.join(dir_path, 'csv', 'archiv', 'rki_' + now.strftime('%Y-%m-%d_%H_%M') + '.csv')
print(curr_minute)
url = 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html'
soupurl = requests.get(url).text
soup = BeautifulSoup(soupurl, 'html.parser')
main = soup.find('div', {'id':'main'})
table = main.find('table')
columns = ['Bundesland', 'confirmed', 'confirmed_diff','extra',  'deaths', 'extra2']
df = pd.read_html(str(table))[0]
print(df)
df.columns = columns
df['date'] = pd.to_datetime(curr_minute)
print(df)
df.to_csv(csv_file)

