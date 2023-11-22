
import requests
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

get_request(url,output)
get_request(url2,output2)