import csv

class Vehiculo:
    def __init__(self, marca, modelo, numero_de_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.numero_de_ruedas = numero_de_ruedas


    def descripcion(self):
        info = f"Marca {self.marca.title()}, Modelo {self.modelo.title()}, {self.numero_de_ruedas} ruedas"
        return print(info)
    
    def guardar_datos_csv(self):
        archivo = open("vehiculos.csv", "a", newline='')
        datos = [(self.__class__, self.__dict__)]
        archivo_csv = csv.writer(archivo)
        archivo_csv.writerows(datos)
        archivo.close()

    def leer_datos_csv(self):
        #Funcion para imprimir las listas de todos los vehiculos guardados, segun clases
        vehiculos_particular = []
        vehiculos_carga = []
        vehiculos_bicicleta = []
        vehiculos_motocicleta = []
        vehiculos_automovil = []

        with open("vehiculos.csv", 'r') as archivo:
            archivo_csv = csv.reader(archivo)
            for row in archivo_csv:
                if len(row) >=2:
                    vehiculo_class = row[0]
                    vehiculo_data = row[1]
                    
                    if vehiculo_class == "<class 'particular.Particular'>":
                        vehiculos_particular.append(eval(vehiculo_data))
                    elif vehiculo_class == "<class 'carga.Carga'>":
                        vehiculos_carga.append(eval(vehiculo_data))
                    elif vehiculo_class == "<class 'bicicleta.Bicicleta'>":
                        vehiculos_bicicleta.append(eval(vehiculo_data))
                    elif vehiculo_class == "<class 'motocicleta.Motocicleta'>":
                        vehiculos_motocicleta.append(eval(vehiculo_data))
                    elif vehiculo_class == "<class 'automovil.Automovil'>":
                        vehiculos_automovil.append(eval(vehiculo_data))  
    
        if len(vehiculos_particular) == 0:
            pass
        else:
            print("\nLista de Vehículos Particular:")
            for vehiculo in vehiculos_particular:
                print(vehiculo)

        if len(vehiculos_carga) == 0:
            pass
        else:
            print("\nLista de Vehículos Carga:")
            for vehiculo in vehiculos_carga:
                print(vehiculo)

        if len(vehiculos_bicicleta) == 0:
            pass
        else:
            print("\nLista de Vehículos Bicicleta:")
            for vehiculo in vehiculos_bicicleta:
                print(vehiculo)

        if len(vehiculos_motocicleta) == 0:
            pass
        else:
            print("\nLista de Vehículos Motocicleta:")
            for vehiculo in vehiculos_motocicleta:
                print(vehiculo)

        if len(vehiculos_automovil) == 0:
            pass
        else:
            print("\nLista de Vehículos Automovil:")
            for vehiculo in vehiculos_automovil:
                print(vehiculo)
  



    

