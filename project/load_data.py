
import requests
import sqlite3
import pandas as pd

def get_request(url,output):
    response = requests.get(url)
    if response.status_code == 200:
        with open(output,'wb') as file:
            file.write(response.content)
    else:
        print("error")

url = 'https://api.worldbank.org/v2/en/indicator/GB.XPD.RSDV.GD.ZS?downloadformat=excel'
url2 = 'https://hdr.undp.org/sites/default/files/2021-22_HDR/HDR21-22_Statistical_Annex_HDI_Trends_Table.xlsx'

output = '../data/world_bank.xlsx'
output2 = '../data/HDR.xlsx'

def worlbank_Data(file):
    dt = pd.read_excel(file,header = 3)
    dt.dropna(axis=1,how='all')
    dt.fillna(0,inplace=True)
    conn = sqlite3.connect('../data/DatasetDB.db')
    dt.to_sql('worldbank', conn, index=False, if_exists='replace')
    conn.close()

def HDR(file):
    dt = pd.read_excel(file,header = 4)
    dt.dropna(axis=1,how='all',inplace=True)
    dt=dt[~dt['HDI rank'].isna()]
    dt.drop('Unnamed: 3',axis=1,inplace=True)
    conn = sqlite3.connect('../data/DatasetDB.db')
    dt.to_sql('HDR', conn, index=False, if_exists='replace')
    conn.close()

get_request(url,output)
get_request(url2,output2)
worlbank_Data(output)
HDR(output2)