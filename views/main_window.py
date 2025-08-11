from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QStackedWidget
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from views.lista_pacientes import ListaPacientes
from views.lista_doctores import ListaDoctores
from views.lista_citas import ListaCitas
from views.historial_medico import HistorialMedico
from forms.form_consulta import FormConsulta
from forms.form_paciente import FormPaciente
from forms.form_doctor import FormDoctor
from forms.form_cita import FormCita
from views.notificaciones import Notificaciones
from views.configuracion import Configuracion

# Definición de la ventana principal del sistema médico
class MainWindow(QWidget):
    # Método constructor, inicializa la ventana principal y los componentes.
    def __init__(self, on_logout=None):
        super().__init__()
        self.on_logout = on_logout
        self.setWindowTitle("Sistema Médico")
        self.setGeometry(100, 100, 1000, 600)

        # Estilo general de la ventana
        self.setStyleSheet("""
            QWidget {
                font-family: 'Segoe UI', 'Arial';
                font-size: 16px;
                background-color: #f4f6f8;
                color: #2c3e50;
            }
            QLabel {
                font-size: 18px;
                font-weight: bold;
            }
        """)

        # Layout principal horizontal que contiene el panel lateral y el contenido principal
        self.layout_principal = QHBoxLayout(self)
        self.crear_panel_lateral()
        self.crear_contenido()

        self.layout_principal.addLayout(self.panel_lateral, 1)  # Panel lateral ocupa 1 parte
        self.layout_principal.addWidget(self.stack, 4)          # Contenido principal ocupa 4 partes
        self.stack.setCurrentIndex(0)                            # Mostrar pantalla inicial

    # Crea el panel lateral con botones para navegar entre secciones
    def crear_panel_lateral(self):
        self.panel_lateral = QVBoxLayout()
        self.panel_lateral.setSpacing(10)

        # Lista de botones con texto y función asociada
        botones = [
            ("Inicio", self.mostrar_inicio),
            ("Registrar Paciente", self.mostrar_form_paciente),
            ("Registrar Doctor", self.mostrar_form_doctor),
            ("Lista de Pacientes", self.mostrar_lista_pacientes),
            ("Lista de Doctores", self.mostrar_lista_doctores),
            ("Agendar Cita Médica", self.mostrar_form_cita),
            ("Lista de Citas Agendadas", self.mostrar_lista_citas),
            ("Crear Consulta Médica", self.mostrar_form_consulta),
            ("Ver Historial Médico", self.mostrar_historial),
            ("Notificaciones", self.mostrar_notificaciones),
            ("Configuración", self.mostrar_configuracion),
        ]

        # Crear y configurar cada botón
        for texto, funcion in botones:
            btn = QPushButton(texto)
            btn.clicked.connect(funcion)
            if texto == "Inicio":
                btn.setStyleSheet("""
                    QPushButton {
                        padding: 12px 20px;
                        font-size: 16px;
                        font-weight: bold;
                        font-family: 'Segoe UI', 'Arial';
                        background-color: #27ae60;
                        color: white;
                        border: none;
                        border-radius: 6px;
                        text-align: center;
                    }
                    QPushButton:hover {
                        background-color: #219150;
                    }
                    QPushButton:pressed {
                        background-color: #1e7e44;
                    }
                """)
            else:
                btn.setStyleSheet("""
                    QPushButton {
                        padding: 12px 20px;
                        font-size: 16px;
                        font-weight: bold;
                        font-family: 'Segoe UI', 'Arial';
                        background-color: #0078D7;
                        color: white;
                        border: none;
                        border-radius: 6px;
                        text-align: center;
                    }
                    QPushButton:hover {
                        background-color: #005fa3;
                    }
                    QPushButton:pressed {
                        background-color: #004080;
                    }
                """)
            self.panel_lateral.addWidget(btn)

        self.panel_lateral.addStretch()  # Añade espacio flexible

        # Botón para cerrar sesión
        btn_logout = QPushButton("Cerrar Sesión")
        btn_logout.setStyleSheet("""
            QPushButton {
                padding: 12px 20px;
                font-size: 16px;
                font-family: 'Segoe UI', 'Arial', 'bold';
                background-color: #e74c3c;
                color: white;
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        btn_logout.clicked.connect(self.logout)
        self.panel_lateral.addWidget(btn_logout)

    # Crea el área principal que cambia entre distintas páginas usando QStackedWidget
    def crear_contenido(self):
        self.stack = QStackedWidget()
        self.notificaciones_widget = Notificaciones()

        # Página inicial con imagen y mensaje de bienvenida
        inicio_widget = QWidget()
        inicio_layout = QVBoxLayout(inicio_widget)

        label_imagen = QLabel()
        label_imagen.setAlignment(Qt.AlignCenter)
        label_bienvenida = QLabel("Bienvenido al Sistema Médico")
        label_bienvenida.setAlignment(Qt.AlignCenter)
        label_bienvenida.setStyleSheet("""
            QLabel {
                font-size: 32px;
                font-weight: bold;
                font-family: 'Segoe UI', 'Arial';
                color: #2c3e50;
                margin-top: 30px;
            }
        """)

        pixmap = QPixmap("resources/principal.jpg")
        pixmap = pixmap.scaled(700, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label_imagen.setPixmap(pixmap)
        label_imagen.setStyleSheet("""
            QLabel {
                border-radius: 32px;
                border: 3px solid #1976d2;
                background-color: #f5f5f5;
                padding: 12px;
                box-shadow: 0px 4px 24px rgba(0,0,0,0.12);
            }
        """)

        inicio_layout.addStretch()
        inicio_layout.addWidget(label_bienvenida)
        inicio_layout.addWidget(label_imagen)
        inicio_layout.addStretch()

        self.stack.addWidget(inicio_widget)

        # Instanciación de los widgets de las diferentes secciones una sola vez
        self.form_paciente = FormPaciente(notificaciones_widget=self.notificaciones_widget)
        self.form_doctor = FormDoctor(notificaciones_widget=self.notificaciones_widget)
        self.lista_pacientes_widget = ListaPacientes()
        self.lista_doctores_widget = ListaDoctores()
        self.form_cita = FormCita(notificaciones_widget=self.notificaciones_widget)
        self.lista_citas_widget = ListaCitas()
        self.form_consulta = FormConsulta()
        self.historial_widget = HistorialMedico()
        self.configuracion_widget = Configuracion()

        # Agrega cada widget al stack en orden fijo para poder cambiar entre ellos fácilmente
        self.stack.addWidget(self.form_paciente)          # índice 1
        self.stack.addWidget(self.form_doctor)            # índice 2
        self.stack.addWidget(self.lista_pacientes_widget) # índice 3
        self.stack.addWidget(self.lista_doctores_widget)  # índice 4
        self.stack.addWidget(self.form_cita)              # índice 5
        self.stack.addWidget(self.lista_citas_widget)     # índice 6
        self.stack.addWidget(self.form_consulta)          # índice 7
        self.stack.addWidget(self.historial_widget)       # índice 8
        self.stack.addWidget(self.notificaciones_widget)  # índice 9
        self.stack.addWidget(self.configuracion_widget)   # índice 10

    # Métodos para mostrar cada sección (actualiza la página visible)
    def mostrar_inicio(self):
        self.stack.setCurrentIndex(0)

    def mostrar_form_paciente(self):
        self.stack.setCurrentIndex(1)

    def mostrar_form_doctor(self):
        self.stack.setCurrentIndex(2)

    def mostrar_lista_pacientes(self):
        # Recarga la lista para reflejar posibles cambios y muestra la página
        self.stack.removeWidget(self.lista_pacientes_widget)
        self.lista_pacientes_widget = ListaPacientes()
        self.stack.insertWidget(3, self.lista_pacientes_widget)
        self.stack.setCurrentIndex(3)

    def mostrar_lista_doctores(self):
        # Recarga la lista para reflejar posibles cambios y muestra la página
        self.stack.removeWidget(self.lista_doctores_widget)
        self.lista_doctores_widget = ListaDoctores()
        self.stack.insertWidget(4, self.lista_doctores_widget)
        self.stack.setCurrentIndex(4)

    def mostrar_form_cita(self):
        self.stack.setCurrentIndex(5)

    def mostrar_lista_citas(self):
        # Recarga la lista para reflejar posibles cambios y muestra la página
        self.stack.removeWidget(self.lista_citas_widget)
        self.lista_citas_widget = ListaCitas()
        self.stack.insertWidget(6, self.lista_citas_widget)
        self.stack.setCurrentIndex(6)

    def mostrar_form_consulta(self):
        self.stack.setCurrentIndex(7)

    def mostrar_historial(self):
        self.stack.setCurrentIndex(8)

    def mostrar_notificaciones(self):
        self.stack.setCurrentIndex(9)

    def mostrar_configuracion(self):
        self.stack.setCurrentIndex(10)

    # Cierra la ventana y ejecuta función opcional para cerrar sesión
    def logout(self):
        self.close()
        if self.on_logout:
            self.on_logout()
