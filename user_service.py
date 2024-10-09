import json
import os

# Ruta del archivo JSON para almacenar usuarios
USERS_FILE = "users.json"

# Cargar usuarios desde el archivo JSON
def cargar_usuarios():
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            # Si el archivo está vacío o corrupto, devolver un diccionario vacío
            return {}
    return {}

# Guardar usuarios en el archivo JSON
def guardar_usuarios(usuarios):
    with open(USERS_FILE, "w", encoding="utf-8") as file:
        json.dump(usuarios, file, indent=4, ensure_ascii=False)  # Asegurar que no haya problemas de codificación

# 1. Obtener todos los usuarios
def obtener_todos_los_usuarios():
    usuarios = cargar_usuarios()
    usuarios_sin_contraseña = {k: {"nombre": v["nombre"], "edad": v["edad"]} for k, v in usuarios.items()}  # No mostrar contraseña
    return usuarios_sin_contraseña

# 2. Obtener un usuario por ID con verificación de contraseña
def obtener_un_usuario(usuario_id, contraseña):
    usuarios = cargar_usuarios()
    usuario = usuarios.get(usuario_id)
    if usuario and usuario.get("contraseña") == contraseña:
        return {"nombre": usuario["nombre"], "edad": usuario["edad"]}  # No mostrar la contraseña
    return "Usuario no encontrado o contraseña incorrecta"

# 3. Crear un nuevo usuario
def crear_un_usuario(usuario_id, usuario_info):
    usuarios = cargar_usuarios()
    if usuario_id in usuarios:
        return "El usuario ya existe."
    usuarios[usuario_id] = usuario_info
    guardar_usuarios(usuarios)
    return f"Usuario {usuario_id} creado exitosamente."

# 4. Actualizar información del usuario
def actualizar_informacion_usuario(usuario_id, nueva_info):
    usuarios = cargar_usuarios()
    if usuario_id not in usuarios:
        return "Usuario no encontrado."
    usuarios[usuario_id].update(nueva_info)
    guardar_usuarios(usuarios)
    return f"Información de usuario {usuario_id} actualizada."
