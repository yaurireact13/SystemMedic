from models.paciente import Paciente
from models.doctor import Doctor
from models.cita import CitaMedica
from models.consulta import ConsultaMedica
from models.utils import buscar_paciente_por_nombre

import time


pacientes = []
doctores = []
citas = []

def registrar_paciente():
    nombre = input("Nombre del paciente: ")
    dni = input("DNI: ")
    nacimiento = input("Fecha de nacimiento (dd-mm-aaaa): ")
    paciente = Paciente(nombre, dni, nacimiento)
    pacientes.append(paciente)
    time.sleep(1.5)
    print("Paciente registrado con éxito.\n")
    

def registrar_doctor():
    nombre = input("Nombre del doctor: ")
    especialidad = input("Especialidad: ")
    doctor = Doctor(nombre, especialidad)
    doctores.append(doctor)
    print("Doctor registrado con éxito.\n")
    time.sleep(1.5)

def crear_consulta():
    if not pacientes or not doctores:
        print("Debe haber al menos un paciente y un doctor registrados.\n")
        return
    nombre_paciente = input("Nombre del paciente para la consulta: ")
    paciente = buscar_paciente_por_nombre(pacientes, nombre_paciente)
    if paciente:
        doctor_nombre = input("Nombre del doctor: ")
        doctor = next((d for d in doctores if d.get_nombre() == doctor_nombre), None)
        if doctor:
            fecha = input("Fecha de consulta: ")
            sintomas = input("Síntomas: ")
            tratamiento = input("Tratamiento: ")
            consulta = ConsultaMedica(fecha, doctor, sintomas, tratamiento)
            paciente.agregar_consulta(consulta)
            print("Consulta agregada con éxito.\n")
            time.sleep(1.5)
        else:
            print("Doctor no encontrado.\n")
            time.sleep(1.5)
    else:
        print("Paciente no encontrado.\n")
        time.sleep(1.5)

def agendar_cita():
    if not pacientes:
        print("Debe haber al menos un paciente registrado.\n")
        return
    nombre_paciente = input("Nombre del paciente para la cita: ")
    paciente = buscar_paciente_por_nombre(pacientes, nombre_paciente)
    if paciente:
        fecha = input("Fecha de cita: ")
        hora = input("Hora de cita: ")
        motivo = input("Motivo de cita: ")
        cita = CitaMedica(paciente, fecha, hora, motivo)
        citas.append(cita)
        print("Cita agendada con éxito.\n")
        time.sleep(1.5)
    else:
        print("Paciente no encontrado.\n")
        time.sleep(1.5)

def reprogramar_cita():
    if not citas:
        print("No hay citas registradas.\n")
        return
    nombre_paciente = input("Nombre del paciente para reprogramar cita: ")
    for cita in citas:
        if cita.paciente.nombre == nombre_paciente:
            nueva_fecha = input("Nueva fecha: ")
            nueva_hora = input("Nueva hora: ")
            cita.cambiar_fecha(nueva_fecha, nueva_hora)
            print("Cita reprogramada.\n")
            time.sleep(1.5)
            return
    print("Cita no encontrada para ese paciente.\n")
    time.sleep(1.5)

def mostrar_historial():
    nombre_paciente = input("Nombre del paciente: ")
    paciente = buscar_paciente_por_nombre(pacientes, nombre_paciente)
    if paciente:
        paciente.mostrar_historial()
    else:
        print("Paciente no encontrado.\n")
        time.sleep(1.5)

def listar_pacientes():
    if not pacientes:
        print("No hay pacientes registrados.\n")
        time.sleep(1.5)
        return
    for p in pacientes:
        p.mostrar_datos()

def listar_citas():
    if not citas:
        print("No hay citas registradas.\n")
        time.sleep(1.5)
        return
    for c in citas:
        c.mostrar_cita()

def menu():
    while True:
        print("\n--- Sistema Médico Basico ---")
        print("1. Registrar paciente")
        print("2. Registrar doctor")
        print("3. Crear consulta médica")
        print("4. Agendar cita médica")
        print("5. Reprogramar cita")
        print("6. Mostrar historial de un paciente")
        print("7. Buscar paciente por nombre")
        print("8. Listar todos los pacientes")
        print("9. Listar todas las citas")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")
        print("\n")

        if opcion == '1':
            registrar_paciente()
        elif opcion == '2':
            registrar_doctor()
        elif opcion == '3':
            crear_consulta()
        elif opcion == '4':
            agendar_cita()
        elif opcion == '5':
            reprogramar_cita()
        elif opcion == '6':
            mostrar_historial()
        elif opcion == '7':
            nombre = input("Nombre del paciente a buscar: ")
            paciente = buscar_paciente_por_nombre(pacientes, nombre)
            if paciente:
                print("Paciente encontrado:")
                paciente.mostrar_datos()
            else:
                print("Paciente no encontrado.")
        elif opcion == '8':
            listar_pacientes()
        elif opcion == '9':
            listar_citas()
        elif opcion == '0':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    menu()