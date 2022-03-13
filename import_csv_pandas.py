import pandas as pd
import requests

url = "https://raw.githubusercontent.com/Sandbird/covid19-Greece/master/cases.csv"

c = pd.read_csv(url)

print (c)
