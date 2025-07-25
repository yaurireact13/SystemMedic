# para buscar un paciente 
def buscar_paciente_por_nombre(lista, nombre, i=0):
    if i >= len(lista):
        return None
    if lista[i].nombre == nombre:
        return lista[i]
    return buscar_paciente_por_nombre(lista, nombre, i + 1)

#busqueda de paciente por dni 
def buscar_paciente_por_dni(lista, dni, i=0):
    if i >= len(lista):
        return None
    if lista[i].dni == dni:
        return lista[i]
    return buscar_paciente_por_dni(lista, dni, i + 1)


