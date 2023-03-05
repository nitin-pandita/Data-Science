import numpy as np 
import csv



file_obj = open('terrorismData.csv' )

data = csv.DictReader((file_obj), skipinitialspace = True)

killed = []
wounded = []
country = []

for row in data:
    killed.append(['Killed'])
    wounded.append(['Wounded'])
    country.append(['Country'])
    
    
killed = np.array(killed)
print(killed)

np_killed  =killed[killed == ''] = '0.0'
np_wounded  =wounded[wounded == ''] = '0.0'

killed_wounded = np_killed + np_wounded

print(killed_wounded)