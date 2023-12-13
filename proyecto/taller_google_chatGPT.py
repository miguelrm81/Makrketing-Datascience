
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials

# Configura las credenciales
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/diego/Documents/carpeta_trabajo_1/z_apuntes/proyecto/clave_API.json', scope)
client = gspread.authorize(creds)

spreadsheet = client.open('Ejemplo Taller Data/Marketing')
worksheet = spreadsheet.get_worksheet(0)
data = worksheet.row_values(2)

datos_dict = {
    "prompt": data[0],
    "prompt_2": data[1],
    "titulo": data[2],
    "imagen": data[3],
    "post_linkedin": data[4],
    "post_twitter": data[5]
}

# Convertir el diccionario a JSON
json_data = json.dumps(datos_dict, indent=2)

# Imprimir el JSON resultante
print(json_data)
