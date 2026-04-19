import requests  # Importa la librería para enviar solicitudes al servidor
from bs4 import BeautifulSoup # Importa la librería para analizar la página web
import pandas as pd

URL = 'https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html'

re = requests.get(URL) # solicitud GET
soup = BeautifulSoup(re.text, 'html.parser')
weather_table = soup.find(attrs={"id": "weather_records"})   # obtenemos tabla con atributo especificado
heading_table = []   # lista vacia para los encabezados
for row in weather_table.find_all('th'):
    heading_table.append(row.text)
content = []   # lista vacia para almacenar los datos de las columnas
for row in weather_table.find_all('tr'):
    td_datos = []    # lista vacia para los datos de cada fila
    if not row.find_all('th'):
        for td in row.find_all('td'):
            td_datos.append(td.text)
        content.append(td_datos)
weather_records = pd.DataFrame(content, columns=heading_table)  # creamos dataframe
print(weather_records)