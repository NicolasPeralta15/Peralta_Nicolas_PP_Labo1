import json

def cargar_archivo(nombre_archivo):
    """
    parametro: recibe como parametro la ruta al archivo que se quiere cargar
    
    que hace: abre un archivo JSON especificado por nombre_archivo y carga su contenido 
    
    retorna: devuelve los datos cargados desde el archivo json
    """
    try:
        with open(nombre_archivo, "r", encoding='utf-8') as archivo:
            data = json.load(archivo)
        return data
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
        return []


def imprimir_lista(data):
    """
    parametro: recibe comoo parametro una lista con diccionarios dentro
    
    que hace: imprime de manera  la información de cada servicio en la lista 
    
    retorna: no retorna nada, solo imprime
    """
    if data:
        for serv in data:
            print(f"""
            ID: {serv['id_servicio']}                         Descripción: {serv['descripcion']}         Tipo: {serv['tipo']}
            Precio unitario: {serv['precioUnitario']}         Cantidad: {serv['cantidad']}               Total servicio: {serv['totalServicio']}
                  """)



def filtrar_por_tipo(data, tipo, nombre_archivo):
    """
    parametro: recibe lista de diccionarios, tipo de servicio, nombre del archivo donde se va a guardar los servicios filtrados
    
    que hace:  filtra los servicios en data por el campo tipo. Solo los servicios que coinciden con el tipo especificado son seleccionados. 
        Los servicios filtrados se guardan en un archivo nuevo pasado por parametro
    
    retorna: no devuelve nada, solo guarda los datos filtrados en un archivo json
    """
    filtracion = [servicio for servicio in data if servicio["tipo"] == tipo]
    with open(nombre_archivo, "w", encoding='utf-8') as archivo:
        json.dump(filtracion, archivo, indent=4, ensure_ascii=False)

def mostrar_servicios(data):
    """
    parametro: recibe lista de diccionarios
    
    que hace:  ordena los servicios en la lista por 'descripcion' de manera ascendente e imprime el id y la descricion de cada servicio
    
    retorna: no devuelve nada, solo imprime
    """
    datos_ordenados = sorted(data, key=lambda servicio: servicio["descripcion"])
    if datos_ordenados:
        for servicio in datos_ordenados:
            print(f"ID: {servicio['id_servicio']}    Descripción: {servicio['descripcion']}")
    else:
        print("No hay servicios para mostrar.")

def guardar_servicio(data, nombre_archivo):
    """
    parametro: recibe lista de diccionarios y el nombre del archivo en donde se van a guardar los datos
    
    que hace: guarda la lista  data en un archivo json con el nombre especificado en nombre_archivo. 
        
    
    retorna: no devuelve nada, solo guarda los datos en un archivo json
    """
    with open(nombre_archivo, "w", encoding='utf-8') as archivo:
        json.dump(data, archivo, indent=4, ensure_ascii=False)

def menu():
    """
    parametro: no recibe nada
    
    que hace: imprime el menu de opciones
    
    retorna: no devuelve nada, solo imprime el menu de opciones
    """
    print("""
          MENU DE OPCIONES
    1 - Cargar el archivo
    2 - Imprimir lista
    3 - Asignar totales
    4 - Filtrar por tipo
    5 - Mostrar servicios
    6 - Guardar servicios
    7 - Salir
          """)

def menu_principal_parcial():
    datos = []
    nombre_archivo = r"C:\Users\rosal\Desktop\Programacion 2024\PP_LAB\data.json"

    while True:
        menu()
        try:
            opcion = int(input("Ingrese la opción que desea ver: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if opcion == 1:
            datos = cargar_archivo(nombre_archivo)
            print("Datos cargados")
        elif opcion == 2:
            imprimir_lista(datos)
        elif opcion == 3:
            print("SIN HACER")
            
        elif opcion == 4:
            if datos:
                tipo = input("Ingrese el tipo de servicio 1 (MINORISTA) -  2 (MAYORISTA) - 3 (EXPORTAR)): ")
                archivo_filtrado = input("Ingrese el nombre del archivo para guardar la filtración: ") + ".json"
                filtrar_por_tipo(datos, tipo, archivo_filtrado)
            else:
                print("Primero debe cargar un archivo.")
        elif opcion == 5:
            mostrar_servicios(datos)
        elif opcion == 6:
            if datos:
                archivo_guardado = input("Ingrese el nombre del archivo para guardar: ") + ".json"
                guardar_servicio(datos, archivo_guardado)
            else:
                print("Primero debe cargar un archivo.")
        elif opcion == 7:
            print("Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
