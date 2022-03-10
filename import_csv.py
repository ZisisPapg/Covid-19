import io
import csv
import requests
#παραθετω το link απο οπου περνουμε τα δεδομένα
csv_url = 'https://raw.githubusercontent.com/Sandbird/covid19-Greece/master/cases.csv'
print(csv_url)
#διαβάζω το αρχειο csv με την συναρτιση requests.Response.content
#μετα απο συμβουλη του link https://www.adamsmith.haus/python/answers/how-to-download-a-csv-file-from-a-url-in-python
req = requests.get(csv_url)
url_content = req.content
print(url_content)


#δημιουργουμε ενα αρχειο με ονομα covid1.csv
csv_file = open('covid1.csv', 'wb')
csv_file.write(url_content)

#φτιαχνω μια λιστα με τις τιμές του csv 
with open('covid.csv', newline='\n') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)
