from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QHBoxLayout, QMessageBox, QFrame
)
from PyQt5.QtGui import QFont

class LoginWindow(QWidget):
    def __init__(self, on_login_success=None):
        super().__init__()
        self.setWindowTitle("Iniciar Sesión")
        self.resize(400, 250)
        self.centrar_ventana()
        self.on_login_success = on_login_success

    def centrar_ventana(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # Fondo gris claro general
        self.setStyleSheet("""
            QWidget {
                background-color: #ecf0f1;
                font-family: 'Segoe UI', Arial;
            }
        """)

        layout_exterior = QVBoxLayout()
        layout_exterior.setAlignment(Qt.AlignCenter)

        # Tarjeta blanca
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

        # Título
        titulo = QLabel("🔐 Sistema Médico")
        titulo.setFont(QFont("Segoe UI", 18, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("color: #0078D7; margin-bottom: 20px;")
        tarjeta_layout.addWidget(titulo)

        # Campos
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Usuario")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Contraseña")
        self.password_input.setEchoMode(QLineEdit.Password)

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

        tarjeta_layout.addWidget(self.user_input)
        tarjeta_layout.addWidget(self.password_input)

        # Botón Ingresar
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
        self.login_button.clicked.connect(self.verificar_login)
        tarjeta_layout.addWidget(self.login_button)

        # Layout final
        layout_exterior.addStretch()
        layout_exterior.addWidget(tarjeta)
        layout_exterior.addStretch()
        self.setLayout(layout_exterior)

    def verificar_login(self):
        usuario = self.user_input.text()
        clave = self.password_input.text()

        # Centro de credenciales 
        if usuario == "yauri" and clave == "admin123":
            QMessageBox.information(self, "Éxito", "Inicio de sesión exitoso.")
            self.close()
            if self.on_login_success:
                self.on_login_success()
        else:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos.")
