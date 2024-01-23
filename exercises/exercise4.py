import urllib.request
import zipfile
import csv
import os
import pandas as pd
import sqlite3

def download_file(url):
	zip_file_path, _ = urllib.request.urlretrieve(url)

	with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
	    zip_ref.extractall('./exercise4')
	os.remove(zip_file_path)


def load_data(file):
    data = []

    with open(file, 'r') as f:
        csv_reader = csv.reader(f, delimiter=';')
        header = next(csv_reader)

        for row in csv_reader:
            row_dict = {}
            for col_name, col_value in zip(header, row):
                if '°' in col_value or ',' in col_value:
                    col_value = col_value.replace(',', '.')
                row_dict[col_name] = col_value
            data.append(row_dict)
    return data

def transform_save(data):
	dt = pd.DataFrame(data)

	dt = dt[["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"]].copy()
	dt.rename(columns={'Temperatur in °C (DWD)':'Temperatur',"Batterietemperatur in °C": "Batterietemperatur"},inplace=True)
	dt['Temperatur']=dt['Temperatur'].astype('float')
	dt['Batterietemperatur'] = dt['Batterietemperatur'].astype(float)
	dt['Geraet'] = dt['Geraet'].astype(int)
	dt['Temperatur'] = dt['Temperatur']*(9/5)+32
	dt['Batterietemperatur'] = dt['Batterietemperatur']*(9/5)+32

	conn = sqlite3.connect('temperatures.sqlite')
	dt.to_sql('temperatures',conn,index=False,if_exists = 'replace')
	conn.commit()
	conn.close()


def main():
	url = 'https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip'
	file = './exercise4/data.csv'

	download_file(url)

	data = load_data(file)
	transform_save(data)


if __name__=='__main__':
	main()



