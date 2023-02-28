from lxml import etree
import requests
import pandas as pd

query_params = {
    'ids': 'PABE', 
    'format': 'xml'
    }
endpoint = "https://beta.aviationweather.gov/cgi-bin/data/taf.php"
response = requests.get(endpoint, params=query_params)

print(response.status_code)
print(response.headers.get("Content-Type"))
cleanApi = etree.parse(response.content)
something = pd.read_xml(cleanApi)