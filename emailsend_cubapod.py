#IMPORTANTE: codificar el script en UTF-8 para poder utilizar vocales acentuadas, etc, ...
import smtplib, getpass, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64

### Para autenticarse en el smtp Server
user = "androctonus1402@gmail.com"
password = "1234567890"

### Para las cabeceras del email
remitente = "androctonus1402@gmail.com"
destinatario = "androctonus@nauta.cu"
asunto = "Asunto del mensaje"

### Vista para el correo que viene de Cubapod
mensaje = open('index_email.html', "rb").read()

### Archivo de audio en cualquier fomato
archivo = "audio.wav"

### Host y puerto SMTP de Gmail
gmail = smtplib.SMTP('smtp.gmail.com', 587)

### Protocolo de cifrado de datos utilizado por gmail
gmail.starttls()

### Credenciales
gmail.login(user, password)

### Muestra la depuración de la operacion de envío 1=true
gmail.set_debuglevel(1)

header = MIMEMultipart()
header['Subject'] = asunto
header['From'] = remitente
header['To'] = destinatario

mensaje = MIMEText(mensaje, 'html') #Content-type:text/html
header.attach(mensaje)

if (os.path.isfile(archivo)):
 adjunto = MIMEBase('application', 'octet-stream')
 adjunto.set_payload(open(archivo, "rb").read())
 encode_base64(adjunto)
 adjunto.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(archivo))
 header.attach(adjunto)

### Enviar email
gmail.sendmail(remitente, destinatario, header.as_string())

### Cerrar la conexión SMTP
gmail.quit()
