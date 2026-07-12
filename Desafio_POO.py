#Suscripcion Base
class Suscripcion:
    def __init__(self, usuario, precio_base, codigo_tarjeta):
        self.usuario = usuario
        self.precio_base = precio_base
        self.__codigo_tarjeta = codigo_tarjeta

    def ver_tarjeta(self):
        return f"XXXX-{self.__codigo_tarjeta[-4:]}"

    def reproducir_contenido(self):
        print(f"El usuario {self.usuario} está viendo contenido estándar.")

#Herencia
class SuscripcionPremium(Suscripcion):
    def __init__(self, usuario, precio_base, codigo_tarjeta, calidad_video):
        super().__init__(usuario, precio_base, codigo_tarjeta)
        self.calidad_video = calidad_video
#Polimorfismo
    def reproducir_contenido(self):
        print(f"El usuario {self.usuario} está viendo contenido en máxima definición {self.calidad_video}.")

# Pruebas
#if __name__ == "__main__":
  #  s = Suscripcion("Marcos", 9.99, "12345678")
  #  print(s.ver_tarjeta())
  #  s.reproducir_contenido()
#if __name__ == "__main__":
   # p = SuscripcionPremium("Marcos", 15.99, "87654321", "4K")
   # print(p.ver_tarjeta())        # XXXX-4321
   # p.reproducir_contenido()      # hereda el método del padre
    #print(p.calidad_video)        # 4K
#Prueba funcional con Polimorfismo
if __name__ == "__main__":
    s = Suscripcion("Marcos", 9.99, "12345678")
    p = SuscripcionPremium("Jennifer", 15.99, "87654321", "8K")

    for cuenta in (s, p):
        cuenta.reproducir_contenido()