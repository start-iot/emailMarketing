import gspread
from oauth2client.service_account import ServiceAccountCredentials
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

atraer = []
concientizar = []
convertir = []
educar = []
venta = []
pos_venta = []


# Función para cargar una plantilla HTML desde un archivo
def cargar_plantilla(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as file:
        return file.read()

# Configurar el acceso a Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credencialesgoogle.json', scope)
client = gspread.authorize(creds)

workBook = client.open("BACKUP ATLAS")
worksheets= workBook.worksheets() # estas son todas las hojas
hojaFunel = workBook.worksheet("Funel")  # Abre la hoja llamada "Funel"
hojaContactos = workBook.worksheet("Contactos")  # Abre la hoja llamada "contactos"
 
def FiltroCliente():

    colCampaña = hojaFunel.col_values(9)  # Columna Estado de la hoja "Funel"
    colId= hojaFunel.col_values(4)  # Columna cliente de la hoja "Funel"

    for i, valor in enumerate(colCampaña):
        if valor.strip() == "ATRAER":  # Comparación directa con "ATRAER"
            if i < len(colId) and colId[i].strip():
                atraer.append(colId[i].strip())
            else:
                atraer.append("Pendiente por dato cliente")
        elif valor.strip() == "CONCIENTIZAR":  # Comparación directa con "CONVERTIR"
            if i < len(colId) and colId[i].strip():
                concientizar.append(colId[i].strip())
            else:
                concientizar.append("Pendiente por dato cliente")
        elif valor.strip() == "EDUCAR":  # Comparación directa con "CONVERTIR"
            if i < len(colId) and colId[i].strip():
                educar.append(colId[i].strip())
            else:
                educar.append("Pendiente por dato cliente")
        elif valor.strip() == "CONVERTIR":  # Comparación directa con "CONVERTIR"
            if i < len(colId) and colId[i].strip():
                convertir.append(colId[i].strip())
            else:
                convertir.append("Pendiente por dato cliente")
        elif valor.strip() == "VENTA":  # Comparación directa con "CONVERTIR"
            if i < len(colId) and colId[i].strip():
                venta.append(colId[i].strip())
            else:
                venta.append("Pendiente por dato cliente")
        elif valor.strip() == "POS-VENTA":  # Comparación directa con "CONVERTIR"
            if i < len(colId) and colId[i].strip():
                pos_venta.append(colId[i].strip())
            else:
                pos_venta.append("Pendiente por dato cliente")
                
    return atraer, concientizar, convertir, educar, venta, pos_venta  # Devuelve los resultados acumulados
resultados_atrae = FiltroCliente()
print("Resultados de Atrae:", resultados_atrae)
print("Resultados de Atraer:", atraer)
print("Resultados de Concientizar:", concientizar)
print("Resultados de Convertir:", convertir)
print("Resultados de Educar:", educar)
print("Resultados de Venta:", venta)
print("Resultados de Pos-Venta:", pos_venta)


def otenerDatos ():
    colIdContactos = hojaContactos.col_values(1)
    colNombres = hojaContactos.col_values(2)
    colCorreos = hojaContactos.col_values(5)
    colTelefonos = hojaContactos.col_values(4)
    colSegmento = hojaContactos.col_values(10)
    
    