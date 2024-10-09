import user_service

def mostrar_menu():
    print("1. Obtener todos los usuarios")
    print("2. Obtener un usuario")
    print("3. Crear un nuevo usuario")
    print("4. Actualizar información de un usuario")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            usuarios = user_service.obtener_todos_los_usuarios()
            print("Usuarios:", usuarios)
        
        elif opcion == "2":
            usuario_id = input("Introduce el ID del usuario: ")
            contraseña = input("Introduce la contraseña del usuario: ")  # Añadir verificación de contraseña
            usuario = user_service.obtener_un_usuario(usuario_id, contraseña)
            print("Usuario:", usuario)
        
        elif opcion == "3":
            usuario_id = input("Introduce el ID del nuevo usuario: ")
            nombre = input("Introduce el nombre: ")
            edad = input("Introduce la edad: ")
            contraseña = input("Introduce la contraseña: ")  # Solicitar contraseña para nuevo usuario
            usuario_info = {"nombre": nombre, "edad": edad, "contraseña": contraseña}
            mensaje = user_service.crear_un_usuario(usuario_id, usuario_info)
            print(mensaje)
        
        elif opcion == "4":
            usuario_id = input("Introduce el ID del usuario a actualizar: ")
            nuevo_nombre = input("Introduce el nuevo nombre (deja en blanco para no cambiar): ")
            nueva_edad = input("Introduce la nueva edad (deja en blanco para no cambiar): ")
            nueva_contraseña = input("Introduce la nueva contraseña (deja en blanco para no cambiar): ")  # Posibilidad de actualizar contraseña
            nueva_info = {}
            if nuevo_nombre:
                nueva_info["nombre"] = nuevo_nombre
            if nueva_edad:
                nueva_info["edad"] = nueva_edad
            if nueva_contraseña:
                nueva_info["contraseña"] = nueva_contraseña  # Actualizar contraseña si es necesario
            mensaje = user_service.actualizar_informacion_usuario(usuario_id, nueva_info)
            print(mensaje)
        
        elif opcion == "5":
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
