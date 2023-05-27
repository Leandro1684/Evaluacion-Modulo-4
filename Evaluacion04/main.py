from automovil import Automovil
from bicicleta import Bicicleta
from carga import Carga
from motocicleta import Motocicleta
from particular import Particular
from vehiculos import Vehiculo


list_vehiculos = []

def ingresar_info():    
    while True:
        try:
            cantidad_vehiculos = int(input("¿Cuantos vehiculos desea ingresar?: "))
            break
        except ValueError:
            print("Ha ocurrido un error, debe ingresar un numero entero") 
    contador = 1
    while contador < cantidad_vehiculos+1:
        try:
            print(f"\nDatos del automovil {contador}")
            marca = input("Ingrese la marca del automovil: ")
            modelo = input("Ingrese el modelo: ") 
            numero_de_ruedas = int(input("Ingrese el numero de ruedas: "))
            velocidad = int(input("Ingrese la velocidad en km/h: "))
            cilindrada = int(input("Ingrese el cilindraje en cc: "))
            info_automovil = f"Datos del automovil {contador} : Marca {marca.title()}, Modelo {modelo.title()}, {numero_de_ruedas} ruedas, {velocidad} Km/h, {cilindrada} cc"
            list_vehiculos.append(info_automovil)
        except ValueError:
            print("Ha ocurrido un error, asegurese de ingresar los datos correctamente!")
            continue    
        contador += 1

def imprimir_vehiculos():
    if len(list_vehiculos) == 0:
        pass
    else:
        print("\nImprimiendo por pantalla los Vehículos:\n")
        for vehiculo in list_vehiculos:
            print(f"{vehiculo}")

ingresar_info()
imprimir_vehiculos()

print("\n---------------------- Instancias Solicitadas -------------------------\n")

particular = Particular("Ford", "Fiesta", 4, 180, 500, 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, 1000, 20000)
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)


particular.descripcion()
carga.descripcion()
bicicleta.descripcion()
motocicleta.descripcion()

print("\n------------------ Verificacion de relación de instancia ----------------\n")

resultados = []
def relacion_instancias(objeto, clase2):
    resultado = isinstance(objeto, clase2)
    relacion = f"{type(objeto).__name__} es instancia con relación a {clase2.__name__}: {resultado}"
    resultados.append(relacion)

def imprimir_relaciones():
    for relacion in resultados:
        print(relacion)


relacion_instancias(motocicleta, Vehiculo)
relacion_instancias(motocicleta, Automovil)
relacion_instancias(motocicleta, Particular)
relacion_instancias(motocicleta, Carga)
relacion_instancias(motocicleta, Bicicleta)
relacion_instancias(motocicleta, Motocicleta)
imprimir_relaciones()

print("\n----------------------- Guardar y Leer archivo .csv ------------------------\n")

particular.guardar_datos_csv()
carga.guardar_datos_csv()
bicicleta.guardar_datos_csv()
motocicleta.guardar_datos_csv()


particular.leer_datos_csv()



