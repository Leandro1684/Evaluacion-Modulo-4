from bicicleta import Bicicleta
import csv

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, numero_de_ruedas, tipo, nro_radios, cuadro, motor):
        super().__init__(marca, modelo, numero_de_ruedas, tipo)
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor

    def descripcion(self):
            info = f"Marca {self.marca.title()}, Modelo {self.modelo.title()}, {self.numero_de_ruedas} ruedas, Tipo: {self.tipo.title()}, Motor: {self.motor}, Cuadro: {self.cuadro.title()}, Nro Radios: {self.nro_radios}"
            return print(info)

    def leer_datos_lista_csv(self):
            #Se van a imprimir solo los 'motocicleta' guardados en 'vehiculos.csv'
            vehiculos_motocicleta = []
            with open("vehiculos.csv", 'r') as archivo:
                archivo_csv = csv.reader(archivo)
                for row in archivo_csv:
                    if len(row) >=2:
                        vehiculo_class = row[0]
                        vehiculo_data = row[1]
                        if vehiculo_class == "<class 'motocicleta.Motocicleta'>":
                            vehiculos_motocicleta.append(eval(vehiculo_data))
            if len(vehiculos_motocicleta) == 0:
                pass
            else:
                print("\nLista de Vehículos Motocicleta:")
                for vehiculo in vehiculos_motocicleta:
                    print(vehiculo)


