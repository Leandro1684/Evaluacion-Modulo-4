from automovil import Automovil
import csv

class Carga(Automovil):
        def __init__(self, marca, modelo, numero_de_ruedas, velocidad, cilindrada, carga_kg):
            super().__init__(marca, modelo, numero_de_ruedas, velocidad, cilindrada)
            self.carga_kg = carga_kg

        def descripcion(self):
              info = f"Marca {self.marca.title()}, Modelo {self.modelo.title()}, {self.numero_de_ruedas} ruedas, {self.velocidad} km/h, {self.cilindrada} cc, Carga: {self.carga_kg} Kg"
              return print(info)
        
        def leer_datos_lista_csv(self):
                #Se van a imprimir solo los 'carga' guardados en 'vehiculos.csv'
                vehiculos_carga = []
                with open("vehiculos.csv", 'r') as archivo:
                    archivo_csv = csv.reader(archivo)
                    for row in archivo_csv:
                        if len(row) >=2:
                            vehiculo_class = row[0]
                            vehiculo_data = row[1]
                            if vehiculo_class == "<class 'carga.Carga'>":
                                vehiculos_carga.append(eval(vehiculo_data))
                if len(vehiculos_carga) == 0:
                    pass
                else:
                    print("\nLista de Vehículos Carga:")
                    for vehiculo in vehiculos_carga:
                        print(vehiculo)