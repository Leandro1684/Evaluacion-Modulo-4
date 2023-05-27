from vehiculos import Vehiculo
import csv

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, numero_de_ruedas, tipo):
        super().__init__(marca, modelo, numero_de_ruedas)
        self.tipo = tipo

    def descripcion(self):
            info = f"Marca {self.marca.title()}, Modelo {self.modelo.title()}, {self.numero_de_ruedas} ruedas, Tipo: {self.tipo.title()}"
            return print(info)

    def leer_datos_lista_csv(self):
            #Se van a imprimir solo las 'bicicleta' guardados en 'vehiculos.csv'
            vehiculos_bicicleta = []
            with open("vehiculos.csv", 'r') as archivo:
                archivo_csv = csv.reader(archivo)
                for row in archivo_csv:
                    if len(row) >=2:
                        vehiculo_class = row[0]
                        vehiculo_data = row[1]
                        if vehiculo_class == "<class 'bicicleta.Bicicleta'>":
                            vehiculos_bicicleta.append(eval(vehiculo_data))
            if len(vehiculos_bicicleta) == 0:
                pass
            else:
                print("\nLista de Vehículos Bicicleta:")
                for vehiculo in vehiculos_bicicleta:
                    print(vehiculo)

