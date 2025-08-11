import os
import sys
import json
from config.temas import TEMA_OSCURO, TEMA_CLARO
from PyQt5.QtWidgets import QApplication
from data_manager import cargar_datos
from forms.login_window import LoginWindow
from views.main_window import MainWindow

# Variables globales para almacenar los datos cargados (pacientes, doctores, citas)
pacientes, doctores, citas = cargar_datos()

# Variables globales para mantener referencias a las ventanas abiertas
app = None
ventana_principal = None
ventana_login = None

def iniciar_principal():
    """
    Crea y muestra la ventana principal del sistema médico.
    Se le pasa un callback para que al cerrar sesión vuelva a la ventana de login.
    """
    global ventana_principal
    ventana_principal = MainWindow(on_logout=iniciar_login)
    ventana_principal.show()

def iniciar_login():
    """
    Crea y muestra la ventana de inicio de sesión (login).
    Se le pasa un callback para que, tras un login exitoso, se inicie la ventana principal.
    """
    global ventana_login
    ventana_login = LoginWindow(on_login_success=iniciar_principal)
    ventana_login.show()

# Ruta al archivo de configuración 
CONFIG_FILE = "config/config.json"

def cargar_tema():
    """
    Lee el archivo de configuración y devuelve el stylesheet correspondiente al tema seleccionado.
    Si no existe o hay error, devuelve el tema claro por defecto.
    """
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
            if config.get("tema") == "Oscuro":
                return TEMA_OSCURO
    return TEMA_CLARO

if __name__ == "__main__":
    # Inicializa la aplicación Qt
    app = QApplication(sys.argv)

    # Aplica el tema visual según la configuración
    app.setStyleSheet(cargar_tema())

    # Muestra la ventana de login
    iniciar_login()

    # Ejecuta el loop principal de eventos Qt
    sys.exit(app.exec_())
