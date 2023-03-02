import requests
from lxml import etree as et
import numpy as np
import pandas as pd
import json

url = "https://beta.aviationweather.gov/cgi-bin/data/taf.php?ids=KORD&format=xml"

try:
    r = requests.get(url)
    xml = r.content
    root = et.fromstring(xml)

    print("The following Tafs were generated in the last four hours:")
    for raw in root.iter("raw_text"):
        print(raw.text)
except:
  print("You done messed up son")