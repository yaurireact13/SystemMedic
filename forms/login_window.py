from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QHBoxLayout, QMessageBox, QFrame
)
from PyQt5.QtGui import QFont

class LoginWindow(QWidget):
    """
    Ventana de inicio de sesión para un sistema médico.

    Permite al usuario ingresar un nombre de usuario y una contraseña.
    Si las credenciales son correctas, ejecuta una función callback
    pasada como parámetro en la creación del objeto.
    """

    def __init__(self, on_login_success=None):
        """
        Constructor de la ventana de login.

        Parámetros:
        - on_login_success: función opcional que se ejecutará
          si el inicio de sesión es exitoso.
        """
        super().__init__()
        self.setWindowTitle("Iniciar Sesión")
        self.resize(400, 250)
        self.centrar_ventana()  # Centra la ventana en la pantalla
        self.on_login_success = on_login_success

    def centrar_ventana(self):
        """
        Configura la posición centrada de la ventana
        y crea todos los elementos gráficos (UI).
        """
        # Centrar ventana
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # Estilo general de fondo gris claro
        self.setStyleSheet("""
            QWidget {
                background-color: #ecf0f1;
                font-family: 'Segoe UI', Arial;
            }
        """)

        # Layout exterior que contiene todo
        layout_exterior = QVBoxLayout()
        layout_exterior.setAlignment(Qt.AlignCenter)

        # Contenedor tipo "tarjeta" blanca
        tarjeta = QFrame()
        tarjeta.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 12px;
                padding: 30px;
                border: 1px solid #ccc;
            }
        """)
        tarjeta_layout = QVBoxLayout(tarjeta)

        # Título de la ventana
        titulo = QLabel("🔐 Sistema Médico")
        titulo.setFont(QFont("Segoe UI", 18, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("color: #0078D7; margin-bottom: 20px;")
        tarjeta_layout.addWidget(titulo)

        # Campo para nombre de usuario
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Usuario")

        # Campo para contraseña
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Contraseña")
        self.password_input.setEchoMode(QLineEdit.Password)  # Oculta el texto

        # Estilo común para los campos de texto
        estilo_input = """
            QLineEdit {
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 6px;
                font-size: 14px;
            }
        """
        self.user_input.setStyleSheet(estilo_input)
        self.password_input.setStyleSheet(estilo_input)

        # Añadir campos a la tarjeta
        tarjeta_layout.addWidget(self.user_input)
        tarjeta_layout.addWidget(self.password_input)

        # Botón de inicio de sesión
        self.login_button = QPushButton("Ingresar")
        self.login_button.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                padding: 10px;
                font-weight: bold;
                font-size: 14px;
                border: none;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        self.login_button.clicked.connect(self.verificar_login)  # Acción al hacer clic
        tarjeta_layout.addWidget(self.login_button)

        # Añadir la tarjeta al layout principal
        layout_exterior.addStretch()
        layout_exterior.addWidget(tarjeta)
        layout_exterior.addStretch()
        self.setLayout(layout_exterior)

    def verificar_login(self):
        """
        Verifica si el usuario y la contraseña ingresados
        coinciden con las credenciales predefinidas.
        """
        usuario = self.user_input.text()
        clave = self.password_input.text()

        # Credenciales de acceso (hardcodeadas para ejemplo)
        if usuario == "yauri" and clave == "admin123":
            QMessageBox.information(self, "Éxito", "Inicio de sesión exitoso.")
            self.close()  
            if self.on_login_success:
                self.on_login_success() 
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos.")
