# data_manager.py
import json
import os

DATA_FILE = "datos.json"

def guardar_datos(pacientes, doctores, citas):
    data = {
        "pacientes": [
            {
                "nombre": p.nombre,
                "dni": p._Paciente__dni,
                "fecha_nacimiento": p._Paciente__fecha_nacimiento,
                "historial": [
                    {
                        "fecha": c.fecha,
                        "doctor": c.doctor.get_nombre(),
                        "sintomas": c.sintomas,
                        "tratamiento": c.tratamiento
                    } for c in p._Paciente__historial
                ]
            } for p in pacientes
        ],
        "doctores": [
            {
                "nombre": d.get_nombre(),
                "especialidad": d._Doctor__especialidad
            } for d in doctores
        ],
        "citas": [
            {
                "paciente": c.paciente.nombre,
                "fecha": c.fecha,
                "hora": c.hora,
                "motivo": c.motivo
            } for c in citas
        ]
    }

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def cargar_datos():
    if not os.path.exists(DATA_FILE):
        return [], [], []

    from models.paciente import Paciente
    from models.doctor import Doctor
    from models.cita import CitaMedica
    from models.consulta import ConsultaMedica

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    pacientes = []
    doctores = []
    citas = []

    doctores_dict = {}

    # Doctores
    for d in data.get("doctores", []):
        doctor = Doctor(d["nombre"], d["especialidad"])
        doctores.append(doctor)
        doctores_dict[doctor.get_nombre()] = doctor

    # Pacientes
    for p in data.get("pacientes", []):
        paciente = Paciente(p["nombre"], p["dni"], p["fecha_nacimiento"])
        for c in p.get("historial", []):
            doctor = doctores_dict.get(c["doctor"])
            if doctor:
                consulta = ConsultaMedica(
                    c["fecha"], doctor, c["sintomas"], c["tratamiento"]
                )
                paciente.agregar_consulta(consulta)
        pacientes.append(paciente)

    # Citas
    for c in data.get("citas", []):
        paciente = next((p for p in pacientes if p.nombre == c["paciente"]), None)
        if paciente:
            cita = CitaMedica(paciente, c["fecha"], c["hora"], c["motivo"])
            citas.append(cita)

    return pacientes, doctores, citas
