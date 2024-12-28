# Tareas SMART para el Proyecto de Mail Marketing

## 1. Integración con Google Sheets

### Objetivo:
Leer y gestionar datos del embudo de ventas desde Google Sheets.

### Tareas:
1. **Crear credenciales del servicio:**
   - Accede a la consola de Google Cloud Platform.
   - Crea un proyecto y habilita la API de Google Sheets.
   - Genera una clave de servicio en formato JSON y descárgala.
   - Guarda el archivo como `credencialesgoogle.json` en tu proyecto.

2. **Configurar conexión con Google Sheets:**
   - Usa la biblioteca `gspread` para autorizar el acceso.
   - Implementa una función que cargue las credenciales JSON.
   - Prueba la conexión listando todas las hojas del archivo objetivo.

3. **Diseñar funciones específicas:**
   - Implementa funciones para leer, actualizar y buscar datos en las hojas:
     - `leer_hoja(nombre_hoja)`: Devuelve los datos como lista de listas.
     - `actualizar_celda(nombre_hoja, fila, columna, valor)`: Actualiza una celda específica.
     - `buscar_en_columna(nombre_hoja, columna, valor)`: Busca valores en una columna específica.

---

## 2. Integración con AppSheet

### Objetivo:
Garantizar que los datos gestionados desde Google Sheets se sincronicen automáticamente con AppSheet.

### Tareas:
1. **Crear una aplicación en AppSheet conectada al archivo de Google Sheets:**
   - Ve a AppSheet y crea una nueva app desde tu archivo de Google Sheets.
   - Configura las vistas y tablas necesarias para reflejar las etapas del embudo.

2. **Habilitar un webhook de AppSheet para acciones automatizadas:**
   - Configura un evento en AppSheet que desencadene un webhook al actualizar datos.
   - Asegúrate de que el webhook envíe los datos necesarios para su procesamiento en tu servidor.

3. **Configurar el procesamiento de datos recibidos:**
   - Diseña una función en tu servidor para recibir los datos del webhook y procesarlos según la etapa del embudo.

---

## 3. Diseño del Funel de Marketing

### Objetivo:
Definir las etapas y las acciones asociadas para cada cliente en el embudo.

### Tareas:
1. **Estructurar las etapas del embudo:**
   - Asegúrate de que las columnas necesarias en Google Sheets sean:
     - `ID Cliente`
     - `Nombre`
     - `Correo Electrónico`
     - `Etapa del Embudo` (`Atraer`, `Concientizar`, etc.).
   - Define plantillas específicas para cada etapa.

2. **Crear una hoja separada para los correos enviados:**
   - Agrega una hoja en Google Sheets llamada `Historial Correos`.
   - Define columnas: `ID Cliente`, `Etapa`, `Plantilla Enviada`, `Fecha de Envío`.

3. **Configurar reglas para mover clientes entre etapas:**
   - Diseña un flujo en AppSheet que actualice la columna `Etapa del Embudo` con base en interacciones registradas.

---

## 4. Gestión de Permisos de Usuario

### Objetivo:
Cumplir con las políticas de consentimiento para mail marketing y evitar ser marcado como spam.

### Tareas:
1. **Agregar una columna para permisos de marketing:**
   - En la hoja de contactos, agrega una columna `Consentimiento Marketing`.
   - Usa valores `Sí` o `No`.

2. **Implementar una validación antes del envío:**
   - Diseña una función que filtre solo los contactos con `Consentimiento Marketing = Sí` antes de enviar correos.

3. **Diseñar un formulario de consentimiento:**
   - Usa AppSheet para crear un formulario accesible desde cualquier dispositivo.
   - Asegúrate de que los datos del formulario se guarden automáticamente en Google Sheets.

---

## 5. Configuración del Servidor para Enviar Correos

### Objetivo:
Enviar correos electrónicos desde el dominio de Hostinger, asegurando una configuración gratuita y efectiva.

### Tareas:
1. **Configurar cuentas de correo en Hostinger:**
   - Ve al panel de control de Hostinger y crea una cuenta de correo personalizada (por ejemplo, `notificaciones@tudominio.com`).

2. **Obtener credenciales SMTP:**
   - Desde el panel de Hostinger, anota el servidor SMTP, puerto, usuario y contraseña para la cuenta creada.

3. **Configurar una función de envío:**
   - Usa bibliotecas como `smtplib` en Python para establecer la conexión SMTP.
   - Asegúrate de incluir encabezados como `X-Priority` para mejorar la entregabilidad.

---

## 6. Creación de Plantillas de Correo

### Objetivo:
Diseñar y organizar plantillas de correo personalizadas para cada etapa del embudo.

### Tareas:
1. **Diseñar las plantillas HTML:**
   - Crea archivos `.html` separados para cada etapa (`Atraer.html`, `Concientizar.html`, etc.).
   - Usa herramientas como Google Docs o un editor HTML para diseñar contenido atractivo.

2. **Almacenar las plantillas en una carpeta organizada:**
   - Crea una carpeta `templates` en tu proyecto.
   - Asegúrate de que cada archivo tenga un nombre claro y representativo.

3. **Implementar una función para cargar plantillas dinámicamente:**
   - Diseña una función que reciba el nombre de la etapa y devuelva la plantilla correspondiente.
   - Asegúrate de manejar errores si una plantilla no está disponible.

---

## 7. Construcción Modular de la Arquitectura

### Objetivo:
Desarrollar una arquitectura escalable que permita organizar y enviar correos de manera eficiente, manteniendo una separación clara entre los módulos.

### Tareas:
1. **Diseñar el módulo `index`:**
   - Este módulo será el punto de entrada del sistema y se encargará de recibir solicitudes de envío de correos.
   - Implementa funciones para:
     - Recibir datos de usuarios, como nombre, correo y segmento.
     - Validar datos antes de pasarlos al módulo principal (`main`).
     - Registrar solicitudes en un archivo de log para auditoría.

2. **Implementar el módulo `main`:**
   - Este módulo manejará la lógica central del sistema, incluyendo:
     - Seleccionar las plantillas adecuadas en función del segmento y la etapa del embudo.
     - Conectarse al servidor SMTP configurado en Hostinger para enviar correos.
     - Actualizar la base de datos en Google Sheets con el estado de los correos enviados.

3. **Establecer comunicación entre `index` y `main`:**
   - Utiliza una estructura de mensajes clara para pasar datos del módulo `index` al módulo `main`.
   - Diseña un protocolo de errores para que `index` maneje cualquier fallo reportado por `main`.

4. **Crear un módulo para segmentación:**
   - Este módulo deberá:
     - Recibir listas de usuarios y clasificarlos en segmentos definidos previamente (por ejemplo, edad, preferencias, región).
     - Integrarse con Google Sheets para obtener datos actualizados.

5. **Configurar pruebas unitarias para cada módulo:**
   - Diseña casos de prueba para validar que:
     - `index` reciba y registre correctamente las solicitudes.
     - `main` envíe correos y maneje errores según lo esperado.
     - El módulo de segmentación clasifique correctamente los usuarios.

Con estas tareas SMART, tu equipo tendrá una guía clara y detallada para desarrollar cada aspecto del proyecto de mail marketing. Cada paso está diseñado para ser medible, alcanzable y alineado con los objetivos del proyecto.

