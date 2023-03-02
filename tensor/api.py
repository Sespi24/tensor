import requests
import numpy as np
import pandas as pd
from pandas import json_normalize
import json

database = {}
url = "https://api.thedogapi.com/v1/breeds"

try:
    r = requests.get(url)
    print (r)
    data = json.loads()
    json_normalize(data['results'])
except:
    print("You done messed up, son")


try:
    j = r.content.pop(0)
    j = pd.DataFrame(r)
    print(j) 
except:
    print("You done messed up son")