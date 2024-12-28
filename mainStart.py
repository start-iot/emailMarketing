import gspread
from oauth2client.service_account import ServiceAccountCredentials
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

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
 
def FunelAction_Atraer():
    colCampaña = hojaFunel.col_values(9)  # Columna 9 de la hoja "Funel"
    colId= hojaFunel.col_values(4)  # Columna 4 de la hoja "Funel"

    atraer = []
    concientizar = []
    convertir = []
    educar = []
    venta = []
    pos_venta = []

    for i, valor in enumerate(colCampaña):
        if valor.strip() == "ATRAER":  # Comparación directa con "ATRAER"
            print(1)  # Imprime 1 si encuentra "ATRAER"
            atraer.append(1)
            id_cliente = colId[i]

            """try:
                clienteFile = hojaContactos.find(colId)
                if clienteFile:
                    nombre = hojaContactos.cell(clienteFile.row, 2).value
                    correo = hojaContactos.cell(clienteFile.row, 5).value
                    atraer.append({"ID": id_cliente, "Nombre": nombre, "Correo": correo})
            except Exception as e:
                print(f"No se puodo encontrar el ID {id_cliente}en la hoja de contacots. Error {e}" )"""

        elif valor.strip() == "CONCIENTIZAR":  # Comparación directa con "CONVERTIR"
            print(2)  # Imprime 2 si encuentra "CONVERTIR"
            concientizar.append(2)
        elif valor.strip() == "EDUCAR":  # Comparación directa con "CONVERTIR"
            print(3)  # Imprime 2 si encuentra "CONVERTIR"
            educar.append(2)
        elif valor.strip() == "CONVERTIR":  # Comparación directa con "CONVERTIR"
            print(4)  # Imprime 2 si encuentra "CONVERTIR"
            convertir.append(2)
        elif valor.strip() == "VENTA":  # Comparación directa con "CONVERTIR"
            print(5)  # Imprime 2 si encuentra "CONVERTIR"
            venta.append(2)
        elif valor.strip() == "POS-VENTA":  # Comparación directa con "CONVERTIR"
            print(6)  # Imprime 2 si encuentra "CONVERTIR"
            pos_venta.append(2)

    return atraer, concientizar, convertir, educar, venta, pos_venta  # Devuelve los resultados acumulados


resultados_atrae = FunelAction_Atraer()
print("Resultados de Atrae:", resultados_atrae)






""" Obtener los correos electrónicos desde la columna B
correos = sheet.col_values(9)  # Asegúrate de que la columna 2 tiene datos
nm_mail = len(sheet.col_values(9))
print(correos)
print(nm_mail)



def mailAtraer(){
    for i , sheet in enumerate(worksheets, start=1):

}

# Abrir la hoja de cálculo
#sheet = client.open("BACKUP ATLAS").sheet55



# Obtener todos los correos electrónicos desde la columna B (ajusta según corresponda)
correos = sheet.col_values(2)

# Configuración del correo
contrasena = "ximupxxjnetrtsik"
#for i , worksheets in enumerate(worksheets, start=1):
 #3   print(f"hoja {i}: {worksheets.title} columnas: {len(worksheets.row_values(1))},  Titulos : {worksheets.row_values(1)}" )

#print(worksheets)
#print(correos)
#print(numSheets)"""