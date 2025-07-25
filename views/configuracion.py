import os
import json
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QComboBox, QCheckBox, QPushButton, QMessageBox, qApp
from PyQt5.QtCore import Qt

CONFIG_FILE = "config/config.json"

class Configuracion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Configuración del sistema")

        layout = QVBoxLayout()

        label = QLabel("Configuración del sistema")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("""
            font-size: 22px;
            font-weight: bold;
            color: #1976d2;
            padding: 12px;
            border-bottom: 2px solid #1976d2;
        """)
        layout.addWidget(label)

        # Cuadro de configuración
        from PyQt5.QtWidgets import QGroupBox, QFormLayout
        group = QGroupBox("Opciones de configuración")
        group_layout = QFormLayout()

        self.temaCombo = QComboBox()
        self.temaCombo.addItems(["Claro", "Oscuro"])
        self.temaCombo.currentTextChanged.connect(self.cambiar_tema_en_tiempo_real)
        group_layout.addRow(QLabel("Tema"), self.temaCombo)

        self.notificacionesCheck = QCheckBox("Activar notificaciones")
        group_layout.addRow(QLabel("Notificaciones"), self.notificacionesCheck)

        guardarBtn = QPushButton("Guardar configuración")
        guardarBtn.clicked.connect(self.guardar_configuracion)
        group_layout.addRow(guardarBtn)

        group.setLayout(group_layout)
        layout.addWidget(group)

        self.setLayout(layout)
        self.cargar_configuracion()

    def aplicar_tema(self, tema):
        if tema == "Oscuro":
            qApp.setStyleSheet("""
                QWidget {
                    background-color: #2e2e2e;
                    color: #ffffff;
                }
                QComboBox, QCheckBox, QPushButton {
                    background-color: #444;
                    color: white;
                    border-radius: 5px;
                    padding: 5px;
                }
            """)
        else:
            qApp.setStyleSheet("")

    def cambiar_tema_en_tiempo_real(self, nuevo_tema):
        self.aplicar_tema(nuevo_tema)

    def cargar_configuracion(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as f:
                config = json.load(f)
                self.temaCombo.setCurrentText(config.get("tema", "Claro"))
                self.notificacionesCheck.setChecked(config.get("notificaciones", True))
                self.aplicar_tema(self.temaCombo.currentText())

    def guardar_configuracion(self):
        config = {
            "tema": self.temaCombo.currentText(),
            "notificaciones": self.notificacionesCheck.isChecked()
        }
        os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=4)

        # Aplicar el tema globalmente al guardar
        from config.temas import TEMA_OSCURO, TEMA_CLARO
        from PyQt5.QtWidgets import qApp
        if config["tema"] == "Oscuro":
            qApp.setStyleSheet(TEMA_OSCURO)
        else:
            qApp.setStyleSheet(TEMA_CLARO)

        QMessageBox.information(self, "Guardado", "Configuración guardada y tema aplicado.")
