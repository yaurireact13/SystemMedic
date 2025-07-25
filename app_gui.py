import os
import sys
import json
from config.temas import TEMA_OSCURO, TEMA_CLARO
from PyQt5.QtWidgets import QApplication
from data_manager import cargar_datos
from forms.login_window import LoginWindow
from views.main_window import MainWindow

# Variables globales para los datos
pacientes, doctores, citas = cargar_datos()

# Referencias globales para mantener vivas las ventanas
app = None
ventana_principal = None
ventana_login = None

def iniciar_principal():
    global ventana_principal
    ventana_principal = MainWindow(on_logout=iniciar_login)
    ventana_principal.show()

def iniciar_login():
    global ventana_login
    ventana_login = LoginWindow(on_login_success=iniciar_principal)
    ventana_login.show()
    
CONFIG_FILE = "config/config.json"

def cargar_tema():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
            if config.get("tema") == "Oscuro":
                return TEMA_OSCURO
    return TEMA_CLARO

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(cargar_tema())
    iniciar_login()
    sys.exit(app.exec_())
