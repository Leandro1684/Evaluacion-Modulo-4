from vehiculos import Vehiculo
import csv

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numero_de_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, numero_de_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def descripcion(self):
            info = f"Marca {self.marca.title()}, Modelo {self.modelo.title()}, {self.numero_de_ruedas} ruedas, {self.velocidad} km/h, {self.cilindrada} cc"
            return print(info)
    
    def leer_datos_lista_csv(self):
            #Se van a imprimir solo los 'automovil' guardados en 'vehiculos.csv'
            vehiculos_automovil = []
            with open("vehiculos.csv", 'r') as archivo:
                archivo_csv = csv.reader(archivo)
                for row in archivo_csv:
                    if len(row) >=2:
                        vehiculo_class = row[0]
                        vehiculo_data = row[1]
                        if vehiculo_class == "<class 'automovil.Automovil'>":
                            vehiculos_automovil.append(eval(vehiculo_data))
            if len(vehiculos_automovil) == 0:
                pass
            else:
                print("\nLista de Vehículos Automovil:")
                for vehiculo in vehiculos_automovil:
                    print(vehiculo)
    
