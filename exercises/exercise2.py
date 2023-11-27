import pandas as pd
import sqlite3

def data_pipeline(url):
	dt = pd.read_csv(url,delimiter = ';')
	dt.drop('Status',axis=1,inplace =True)
	dt['Breite'] = pd.to_numeric(dt['Breite'].replace(',','.',regex = True))
	dt['Laenge'] = pd.to_numeric(dt['Laenge'].replace(',','.',regex = True))
	dt = dt[dt['Verkehr'].isin(("FV", "RV", "nur DPN")) & dt['Laenge'].between(-90,90,inclusive='both') & dt['Breite'].between(-90,90,inclusive='both')]
	pattern = r'^[A-Za-z]{2}:\d+:\d+(:\d+)?$'
	dt = dt[dt['IFOPT'].str.match(pattern,na=False)]
	dt.dropna(axis=0,inplace=True)
	dt_object = dt.select_dtypes(include=['object']).columns
	dt[dt_object] = dt[dt_object].astype(str)
	return dt

def save_sql(dt):

	conn = sqlite3.connect('trainstops.sqlite')
	dt.to_sql('trainstops',conn,index=False,if_exists = 'replace')
	conn.commit()
	conn.close()


def main():
	url = "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"
	dt = data_pipeline(url)
	save_sql(dt)

if __name__ == "__main__":
	main()