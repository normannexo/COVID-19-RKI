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

csv_file = os.path.join(dir_path, 'csv', 'archive', 'rki_' + now.strftime('%Y-%m-%d_%H_%M') + '.csv')
print(curr_minute)
url = 'https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html'
soupurl = requests.get(url).text
soup = BeautifulSoup(soupurl, 'html.parser')
main = soup.find('div', {'id':'main'})
table = main.find('table')

# first row of table contains header "Bundesland", "Elektronisch übermittelte Fälle"
row = table.select_one('tr')
row.decompose()

# 01.04.2020: deletetd extra column Extra2
columns = ['Bundesland', 'confirmed', 'confirmed_diff','extra',  'deaths']
df = pd.read_html(str(table), thousands= '.',decimal=',')[0]
#print(df)
df.columns = columns
df['date'] = pd.to_datetime(curr_minute)
df['confirmed']= df.confirmed.astype(str).str.replace(r'\.','').astype(int)
#remove soft hyphen from Bundesland:
df.Bundesland = df.Bundesland.str.replace(r'[^A-Za-zÄÖÜäöüß-]', r'')


print(df)
df = df[['Bundesland','date', 'confirmed', 'deaths']]
df.to_csv(csv_file)

