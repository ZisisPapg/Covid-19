import pandas as pd
import requests
import tkinter as tk
import sys
zisis
url = "https://raw.githubusercontent.com/Sandbird/covid19-Greece/master/cases.csv"

c = pd.read_csv(url)

print (c)


root = tk.Tk()
root.geometry('600x600')


dframe = c

print(' COVID 2019 DATA DASHBOARD')

print(dframe)
