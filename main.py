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

# Abrir la hoja de cálculo
sheet = client.open("prueba_marketing").sheet1

# Obtener todos los correos electrónicos desde la columna B (ajusta según corresponda)
correos = sheet.col_values(2)

# Configuración del correo
contrasena = "ximupxxjnetrtsik"

# Enviar correos a cada dirección en la lista
for correo in correos:
    MSG = MIMEMultipart()
    MSG['From'] = "startiotpro@gmail.com"
    MSG['To'] = correo
    MSG['Subject'] = "BIENVENIDA"

    # Cargar la plantilla HTML que deseas usar
    mensaje_html = cargar_plantilla('PlanStart.html')  # Cambia a 'oferta.html' según necesites

    # Agregar el cuerpo del correo al objeto
    MSG.attach(MIMEText(mensaje_html, 'html'))

    # Agregar encabezados para marcar como importante
    MSG.add_header("X-Priority", "1")  # Urgente
    MSG.add_header("X-MSMail-Priority", "High")
    MSG.add_header("Importance", "High")

    try:
        # Establecer la conexión con el servidor de Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Ingresar al servicio
        server.login(MSG['From'], contrasena)
        # Enviar el mensaje
        server.sendmail(MSG['From'], MSG['To'], MSG.as_string())
        server.quit()
        print(f"Mensaje enviado a {correo}")
    except Exception as e:
        print(f"Error al enviar correo a {correo}: {e}")