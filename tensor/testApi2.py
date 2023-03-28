import requests
import numpy as np
import pandas as pd
from pandas import json_normalize
import json

url = "https://api.thecatapi.com/v1/breeds"
target_path = "cat_breeds.csv"


r = requests.get(url)
r.raise_for_status()    # Check that the request was successful

try:
    cat = r.json()
    cats = pd.read_json(cat)
    
    '''data = json.loads()
    json_normalize(data['results'])'''
except:
    print("You done messed up, son")