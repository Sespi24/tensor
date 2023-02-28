import requests
import pandas as pd

response = requests.get("https://beta.aviationweather.gov//cgi-bin/data/taf.php?ids=PABE&format=xml")

response.status_code
