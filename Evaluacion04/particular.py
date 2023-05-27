from automovil import Automovil
import csv

class Particular(Automovil):
        def __init__(self, marca, modelo, numero_de_ruedas, velocidad, cilindrada, nro_asientos):
            super().__init__(marca, modelo, numero_de_ruedas, velocidad, cilindrada)
            self.nro_asientos = nro_asientos

        def descripcion(self):
              info = f"Marca {self.marca.title()}, Modelo {self.modelo.title()}, {self.numero_de_ruedas} ruedas, {self.velocidad} km/h, {self.cilindrada} cc, Puestos: {self.nro_asientos}"
              return print(info)
        
        def leer_datos_lista_csv(self):
            #Se van a imprimir solo los 'particular' guardados en 'vehiculos.csv'
            vehiculos_particular = []
            with open("vehiculos.csv", 'r') as archivo:
                archivo_csv = csv.reader(archivo)
                for row in archivo_csv:
                    if len(row) >=2:
                        vehiculo_class = row[0]
                        vehiculo_data = row[1]
                        if vehiculo_class == "<class 'particular.Particular'>":
                            vehiculos_particular.append(eval(vehiculo_data))
            if len(vehiculos_particular) == 0:
                pass
            else:
                print("\nLista de Vehículos Particular:")
                for vehiculo in vehiculos_particular:
                    print(vehiculo)
          
                        
                          
            
            
            
