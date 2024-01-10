
import requests
import sqlite3
import pandas as pd

def get_request(url,output):
    response = requests.get(url)
    if response.status_code == 200:
        with open(output,'wb') as file:
            file.write(response.content)
        return True
    else:
        print(response.status_code)
        return False


url = 'https://api.worldbank.org/v2/en/indicator/GB.XPD.RSDV.GD.ZS?downloadformat=excel'
url2 = 'https://hdr.undp.org/sites/default/files/2021-22_HDR/HDR21-22_Statistical_Annex_HDI_Trends_Table.xlsx'

output = '../data/world_bank.xlsx'
output2 = '../data/HDR.xlsx'

DATABASE_PATH = '../data/DatasetDB.db'

def worldbank_Data(file):
    data = pd.read_excel(file,sheet_name='Data',header = 3)
    metadata = pd.read_excel(file,sheet_name='Metadata - Countries')
    data.dropna(axis=1,how='all')
    data.fillna(0,inplace=True)
    conn = sqlite3.connect(DATABASE_PATH)
    data.to_sql('worldbank', conn, index=False, if_exists='replace')
    metadata.to_sql('metadata_countries',conn, index=False, if_exists='replace')
    conn.close()

def HDR(file):
    dt = pd.read_excel(file,header = 4)
    dt.dropna(axis=1,how='all',inplace=True)
    dt=dt[~dt['HDI rank'].isna()]
    dt.drop('Unnamed: 3',axis=1,inplace=True)
    conn = sqlite3.connect(DATABASE_PATH)
    dt.to_sql('HDR', conn, index=False, if_exists='replace')
    conn.close()

get_request(url,output)
get_request(url2,output2)
worldbank_Data(output)
HDR(output2)