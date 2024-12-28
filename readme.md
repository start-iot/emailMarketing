# Proyecto de Mail Marketing Automatizado

Este proyecto tiene como objetivo construir un sistema modular que permita enviar correos de bienvenida y publicidad automática a los segmentos definidos en un embudo de ventas. El sistema se integrará con Google Sheets para gestionar los datos y utilizará el dominio de Hostinger para garantizar el cumplimiento de las políticas de envío y un correcto funcionamiento.

## Funcionalidades Principales
1. **Envío de correos automáticos**:
   - Bienvenida a nuevos clientes.
   - Publicidad y promociones segmentadas.
   - Seguimiento postventa.
   - Recordatorios de cartera y pagos pendientes.

2. **Segmentación del embudo de ventas**:
   - Etapas: Atraer, Concientizar, Educar, Convertir, Venta, Posventa.
   - Plantillas personalizadas para cada etapa.

3. **Cumplimiento con políticas de correo**:
   - Obtención de permisos de los usuarios.
   - Prevención de baneos mediante las mejores prácticas.

4. **Envío de correos desde el dominio de Hostinger**:
   - Configuración de servidor SMTP.
   - Uso de direcciones de correo personalizadas.

---

## Etapas del Embudo de Ventas
### 1. **Atraer**
   - **Objetivo**: Captar la atención de clientes potenciales.
   - **Acciones**:
     - Enviar un correo de bienvenida con información general.
     - Compartir un descuento especial o incentivo para registrarse.
   - **Plantilla**: “Gracias por tu interés en [nombre de la empresa]”.

### 2. **Concientizar**
   - **Objetivo**: Generar interés en los productos o servicios.
   - **Acciones**:
     - Enviar información educativa.
     - Presentar casos de éxito o testimonios de clientes.
   - **Plantilla**: “Descubre cómo podemos ayudarte”.

### 3. **Educar**
   - **Objetivo**: Proveer información detallada que fomente la decisión de compra.
   - **Acciones**:
     - Enviar guías, videos o tutoriales.
     - Ofrecer webinars o sesiones informativas.
   - **Plantilla**: “Todo lo que necesitas saber sobre [producto o servicio]”.

### 4. **Convertir**
   - **Objetivo**: Motivar la compra.
   - **Acciones**:
     - Enviar recordatorios de carrito abandonado.
     - Ofrecer descuentos limitados.
   - **Plantilla**: “¡No dejes pasar esta oferta especial!”.

### 5. **Venta**
   - **Objetivo**: Asegurar una experiencia de compra satisfactoria.
   - **Acciones**:
     - Confirmación de pedido y detalles del envío.
     - Proveer información de contacto para soporte.
   - **Plantilla**: “Gracias por tu compra”.

### 6. **Posventa**
   - **Objetivo**: Fortalecer la relación con el cliente.
   - **Acciones**:
     - Enviar encuestas de satisfacción.
     - Ofrecer soporte técnico o recomendaciones.
   - **Plantilla**: “Queremos escuchar tu opinión”.

---

## Tareas SMART
### **1. Configuración Inicial del Proyecto**
   - **Objetivo**: Preparar el entorno de desarrollo.
   - **Tareas**:
     1. Crear un repositorio en GitHub.
     2. Configurar un servidor en Hostinger con Node.js y Python.
     3. Instalar dependencias necesarias: `gspread`, `oauth2client`, `smtplib`.
     4. Configurar credenciales para Google Sheets.

### **2. Integración con Google Sheets**
   - **Objetivo**: Leer y gestionar datos del embudo de ventas.
   - **Tareas**:
     1. Conectar a Google Sheets usando una cuenta de servicio.
     2. Crear funciones para leer y actualizar datos en las hojas.
     3. Diseñar una estructura de datos para segmentar clientes.

### **3. Plantillas de Correo**
   - **Objetivo**: Diseñar correos atractivos y personalizados.
   - **Tareas**:
     1. Crear plantillas HTML para cada etapa del embudo.
     2. Probar compatibilidad con clientes de correo populares.
     3. Incorporar campos personalizables (nombre, etapa, oferta).

### **4. Configuración de Permisos del Usuario**
   - **Objetivo**: Garantizar el cumplimiento de políticas de envío de correo.
   - **Tareas**:
     1. Crear un formulario de suscripción con campos claros para obtener el consentimiento del usuario.
     2. Diseñar un sistema de doble opt-in.
     3. Almacenar registros de consentimiento en Google Sheets.

### **5. Configuración de SMTP en Hostinger**
   - **Objetivo**: Enviar correos desde el dominio de Hostinger.
   - **Tareas**:
     1. Configurar registros SPF, DKIM y DMARC en Hostinger.
     2. Crear direcciones de correo personalizadas para el dominio.
     3. Probar la conectividad con un servidor SMTP.

### **6. Automatización del Embudo**
   - **Objetivo**: Disparar acciones automáticas basadas en las etapas del cliente.
   - **Tareas**:
     1. Configurar triggers en Google Sheets para detectar nuevos registros.
     2. Implementar un sistema de colas para enviar correos según la etapa.
     3. Monitorear el rendimiento de las campañas y registrar resultados.

---

## Tecnologías Utilizadas
- **Python**: Para la integración con Google Sheets y automatización.
- **HTML**: Diseño de plantillas de correo.
- **JavaScript**: Formularios interactivos y validaciones en la página web.
- **Node.js**: Configuración del servidor SMTP y API REST.

---

## Instrucciones de Implementación
1. **Clonar el Repositorio**:
   ```bash
   git clone https://github.com/usuario/proyecto-mail-marketing.git
   ```

2. **Configurar Credenciales de Google**:
   - Generar un archivo JSON de cuenta de servicio.
   - Guardar el archivo como `credencialesgoogle.json`.

3. **Instalar Dependencias**:
   ```bash
   pip install gspread oauth2client
   ```

4. **Configurar SMTP en Hostinger**:
   - Acceder al panel de control de Hostinger.
   - Configurar registros SPF, DKIM y DMARC.
   - Crear direcciones de correo personalizadas.

5. **Ejecutar el Proyecto**:
   ```bash
   python app.py
   ```

6. **Probar las Funcionalidades**:
   - Registrar un cliente en Google Sheets.
   - Verificar el envío automático de correos.

---

## Buenas Prácticas
- Solicitar el consentimiento explícito del usuario antes de enviar correos.
- Respetar las políticas de privacidad y permitir que los usuarios se den de baja.
- Utilizar plantillas responsivas y probadas.
- Monitorear constantemente el rendimiento del sistema.

---

## Contacto
Para soporte o dudas, contacta a: [startiotpro@tudominio.com](mailto:startiotpro@tudominio.com)

