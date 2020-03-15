# COVID-19 case numbers Germany from Robert-Koch-Institut

Python scripts for collecting historical case numbers of the spread of COVID-19 in Germany from Robert Koch Institut.
https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html

Data is updated on a daily basis and published in a csv file here: http://www.nexolin.de/data/covid-19/rki/rki_data.csv

included files:
- `rki_get_cases.py`: script for downloading current case numbers from the RKI server
- `rki_merge_cases.py`: combine cases to one single csv file with the following structure:

<table>
<tr>
<td>Bundesland</td><td>confirmed</td><td>deaths</td> 
</tr>
</table>
