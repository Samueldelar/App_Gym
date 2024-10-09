import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import os
import json  # Importar para leer directamente el archivo JSON

# Ruta del archivo JSON
USERS_FILE = "users.json"

# Folder path with images
IMAGE_PATH = "C:/Users/Usuario/Desktop/Ejercicios"

# Clase para manejar el inicio de sesión
class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login - BodyBuilder App")
        self.geometry("400x300")
        self.config(bg="#e0f7fa")

        # Título de la ventana
        self.label_title = ttk.Label(self, text="Iniciar sesión", font=("Helvetica", 16), background="#e0f7fa")
        self.label_title.pack(pady=20)

        # Campo de usuario
        self.label_username = ttk.Label(self, text="Usuario:", background="#e0f7fa")
        self.label_username.pack(pady=5)
        self.entry_username = ttk.Entry(self)
        self.entry_username.pack(pady=5)

        # Campo de contraseña
        self.label_password = ttk.Label(self, text="Contraseña:", background="#e0f7fa")
        self.label_password.pack(pady=5)
        self.entry_password = ttk.Entry(self, show="*")
        self.entry_password.pack(pady=5)

        # Botón para iniciar sesión
        self.btn_login = ttk.Button(self, text="Iniciar sesión", command=self.verify_credentials)
        self.btn_login.pack(pady=20)

    def verify_credentials(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Cargar los usuarios directamente desde el archivo JSON
        try:
            with open(USERS_FILE, "r", encoding="utf-8") as file:
                usuarios = json.load(file)

            # Buscar coincidencia de usuario y contraseña
            for user_id, user_info in usuarios.items():
                if user_info["nombre"] == username and user_info["contraseña"] == password:
                    messagebox.showinfo("Acceso permitido", "Bienvenido, accediendo a la app de ejercicios...")
                    self.destroy()  # Cerrar la ventana de login
                    run_app()  # Iniciar la app de ejercicios
                    return
            
            # Si no se encuentra coincidencia
            messagebox.showerror("Error de credenciales", "Usuario o contraseña incorrectos.")
        
        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontró el archivo de usuarios.")
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Error al leer el archivo de usuarios.")

# Exercise data by body part
exercises = {
    "Brazos": [
        {"nombre": "Curl de Bíceps", "series": 3, "repeticiones": 12, "descripcion": "Levanta pesas lentamente hasta que los bíceps estén contraídos.", "imagen": "curl martillo.jpeg"},
        {"nombre": "Extensión de Tríceps", "series": 3, "repeticiones": 15, "descripcion": "Extiende los brazos hacia arriba sosteniendo la pesa y flexiona los codos.", "imagen": "extension de triceps.jpeg"},
        {"nombre": "Flexiones de Brazos", "series": 3, "repeticiones": 10, "descripcion": "Acuéstate boca abajo y empuja tu cuerpo hacia arriba usando los brazos.", "imagen": "flexion de pecho.jpeg"},
        {"nombre": "Fondos en Paralelas", "series": 3, "repeticiones": 8, "descripcion": "Bájate y súbete usando las barras paralelas, manteniendo el cuerpo recto.", "imagen": "fondos paralelas.jpeg"},
        {"nombre": "Curl de Martillo", "series": 3, "repeticiones": 12, "descripcion": "Sostén las pesas de lado y realiza el curl manteniendo la posición.", "imagen": "curl martillo.jpeg"}
    ],
    "Piernas": [
        {"nombre": "Sentadillas", "series": 4, "repeticiones": 10, "descripcion": "Baja lentamente el cuerpo hasta una posición de cuclillas y vuelve a subir.", "imagen": "sentadillas.jpeg"},
        {"nombre": "Zancadas", "series": 3, "repeticiones": 12, "descripcion": "Da un paso largo hacia adelante y baja la cadera, manteniendo la espalda recta.", "imagen": "zancadas.jpeg"},
        {"nombre": "Prensa de Piernas", "series": 3, "repeticiones": 10, "descripcion": "Usa la máquina de prensa para empujar el peso con las piernas.", "imagen": "prensa de piernas.jpeg"},
        {"nombre": "Elevación de Talones", "series": 4, "repeticiones": 15, "descripcion": "Párate sobre la punta de los pies y baja lentamente los talones.", "imagen": "elevacion de talones.jpeg"},
        {"nombre": "Peso Muerto", "series": 3, "repeticiones": 10, "descripcion": "Levanta una barra desde el suelo manteniendo la espalda recta.", "imagen": "peso muerto.jpeg"}
    ],
    "Pecho": [
        {"nombre": "Press de Banca", "series": 4, "repeticiones": 10, "descripcion": "Acostado en un banco, empuja la barra hacia arriba desde el pecho.", "imagen": "prensa de banca.jpeg"},
        {"nombre": "Flexiones de Pecho", "series": 3, "repeticiones": 12, "descripcion": "Realiza flexiones con las manos en el suelo y el cuerpo recto.", "imagen": "flexion de pecho.jpeg"},
        {"nombre": "Aperturas con Mancuernas", "series": 3, "repeticiones": 12, "descripcion": "Acuéstate en un banco y abre los brazos sosteniendo mancuernas.", "imagen": "apertura mancuernas.jpeg"},
        {"nombre": "Press de Pecho en Máquina", "series": 3, "repeticiones": 10, "descripcion": "Usa la máquina de press para trabajar el pecho.", "imagen": "press de pecho en maquina.jpeg"},
        {"nombre": "Dips de Pecho", "series": 3, "repeticiones": 8, "descripcion": "Bájate y súbete usando barras, inclinando el cuerpo hacia adelante.", "imagen": "dips de pecho.jpeg"}
    ],
    "Espalda": [
        {"nombre": "Dominadas", "series": 3, "repeticiones": 8, "descripcion": "Cuélgate de una barra y eleva tu cuerpo hacia arriba.", "imagen": "dominadas espalda.jpeg"},
        {"nombre": "Remo con Mancuernas", "series": 3, "repeticiones": 10, "descripcion": "Inclínate hacia adelante y jala las mancuernas hacia tu abdomen.", "imagen": "remo con mancuernas.jpeg"},
        {"nombre": "Peso Muerto", "series": 3, "repeticiones": 10, "descripcion": "Levanta una barra desde el suelo manteniendo la espalda recta.", "imagen": "peso muerto espalda.jpeg"},
        {"nombre": "Jalón al Pecho", "series": 3, "repeticiones": 10, "descripcion": "Usa la máquina de jalón para tirar hacia abajo con las manos.", "imagen": "jalon pecho.jpeg"},
        {"nombre": "Hiperextensiones", "series": 3, "repeticiones": 12, "descripcion": "Acostado boca abajo en un banco, eleva el torso hacia arriba.", "imagen": "hiperextrexiones.jpeg"}
    ]
}

# Main window for the exercise app
class AppBodyBuilder(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BodyBuilder - Ejercicios")
        self.geometry("700x600")
        self.config(bg="#e0f7fa")

        # Custom styles
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Helvetica', 12), padding=10)
        self.style.configure('TLabel', font=('Helvetica', 14), background="#e0f7fa")
        self.style.configure('TCombobox', font=('Helvetica', 12))

        # Title
        self.label = ttk.Label(self, text="Selecciona la parte del cuerpo a entrenar:", anchor="center")
        self.label.pack(pady=10)

        # Body part selection menu
        self.body_parts = ttk.Combobox(self, values=list(exercises.keys()), state="readonly", font=('Helvetica', 12))
        self.body_parts.set("Seleccionar parte del cuerpo")
        self.body_parts.pack(pady=10)

        # Button to view exercises
        self.btn_exercises = tk.Button(self, text="Ver ejercicios", bg="#00796b", fg="white", font=('Helvetica', 12),
                                       command=self.show_exercises)
        self.btn_exercises.pack(pady=10)

        self.label_exercises = ttk.Label(self, text="")
        self.label_exercises.pack(pady=10)

        # Image label for showing exercise images
        self.image_label = ttk.Label(self)
        self.image_label.pack(pady=10)

        self.current_exercise = None
        self.remaining_series = 0
        self.remaining_repeticiones = 0
        self.time_counter = 0
        self.clock = None
        self.paused = False

        # Variables to evitar crear botones múltiples veces
        self.btn_start_created = False
        self.btn_pause_created = False
        self.btn_resume_created = False
        self.exercise_menu = None

    def show_exercises(self):
        """Mostrar ejercicios para la parte seleccionada."""
        selection = self.body_parts.get()
        if selection:
            exercise_list = exercises[selection]
            self.label_exercises.config(text=f"Ejercicios para {selection}:")

            # Remove previous exercise menu if it exists
            if self.exercise_menu:
                self.exercise_menu.pack_forget()

            # Dropdown menu with exercises for the selected part
            self.exercise_menu = ttk.Combobox(self, values=[ej["nombre"] for ej in exercise_list], state="readonly", font=('Helvetica', 12))
            self.exercise_menu.set("Seleccionar ejercicio")
            self.exercise_menu.pack(pady=10)

            # Botón de iniciar ejercicio solo se crea una vez
            if not self.btn_start_created:
                self.btn_start = tk.Button(self, text="Iniciar ejercicio", bg="#00796b", fg="white", font=('Helvetica', 12),
                                           command=self.start_exercise)
                self.btn_start.pack(pady=10)
                self.btn_start_created = True

    def start_exercise(self):
        """Iniciar el ejercicio seleccionado."""
        selection = self.exercise_menu.get()
        if selection:
            for part in exercises.values():
                for ej in part:
                    if ej["nombre"] == selection:
                        self.current_exercise = ej
                        self.remaining_series = ej["series"]
                        self.remaining_repeticiones = ej["repeticiones"]
                        self.time_counter = 0
                        self.update_counter()
                        self.display_image(ej["imagen"])

                        # Asegurarse de que los botones de pausar y reanudar se creen solo una vez
                        if not self.btn_pause_created:
                            self.btn_pause = tk.Button(self, text="Pausar ejercicio", bg="#f57f17", fg="white", font=('Helvetica', 12),
                                                       command=self.pause_exercise)
                            self.btn_pause.pack(pady=10)
                            self.btn_pause_created = True

                        if not self.btn_resume_created:
                            self.btn_resume = tk.Button(self, text="Reanudar ejercicio", bg="#0288d1", fg="white", font=('Helvetica', 12),
                                                        command=self.resume_exercise)
                            self.btn_resume.pack(pady=10)
                            self.btn_resume_created = True

                        return  # Salir después de iniciar el ejercicio

    def update_counter(self):
        """Actualización del contador de series y repeticiones."""
        if not self.paused:
            if self.remaining_series > 0:
                if self.remaining_repeticiones > 0:
                    self.remaining_repeticiones -= 1
                    self.label_exercises.config(text=f"Serie: {self.remaining_series}, Repeticiones restantes: {self.remaining_repeticiones}")
                    self.clock = self.after(1000, self.update_counter)  # Simulate 1 second per repetition
                else:
                    self.remaining_series -= 1
                    self.remaining_repeticiones = self.current_exercise["repeticiones"]
                    self.update_counter()
            else:
                self.after_cancel(self.clock)
                messagebox.showinfo("¡Completado!", "Has completado el ejercicio.")

    def pause_exercise(self):
        """Pausar el ejercicio en curso."""
        self.paused = True
        if self.clock:
            self.after_cancel(self.clock)
            self.label_exercises.config(text="Ejercicio pausado.")

    def resume_exercise(self):
        """Reanudar el ejercicio pausado."""
        if self.remaining_series > 0 and self.paused:
            self.paused = False
            self.update_counter()

    def display_image(self, image_name):
        """Mostrar la imagen asociada con el ejercicio."""
        image_path = os.path.join(IMAGE_PATH, image_name)
        try:
            image = Image.open(image_path)
            image = image.resize((200, 200), Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=self.photo)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")

# Run the exercise app
def run_app():
    app = AppBodyBuilder()
    app.mainloop()

# Run the login window before starting the exercise app
if __name__ == "__main__":
    login_app = LoginApp()
    login_app.mainloop()
