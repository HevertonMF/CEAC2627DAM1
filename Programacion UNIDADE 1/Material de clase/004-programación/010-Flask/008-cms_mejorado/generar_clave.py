# Genera el hash de tu contraseña de administrador
# Ejecuta:  python generar_clave.py
# y copia el resultado en CLAVE_ADMIN dentro de app.py
from getpass import getpass
from werkzeug.security import generate_password_hash

clave = getpass("Escribe la contraseña del admin: ")
print()
print(generate_password_hash(clave))
