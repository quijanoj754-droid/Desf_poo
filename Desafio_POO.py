class Suscripcion:
    def __init__(self, usuario, precio_base, codigo_tarjeta):
        self.usuario = usuario
        self.precio_base = precio_base
        self.__codigo_tarjeta = codigo_tarjeta

    def ver_tarjeta(self):
        return f"XXXX-{self.__codigo_tarjeta[-4:]}"

    def reproducir_contenido(self):
        print(f"El usuario {self.usuario} está viendo contenido estándar.")


# --- Pruebas ---
if __name__ == "__main__":
    s = Suscripcion("Marcos", 9.99, "12345678")
    print(s.ver_tarjeta())
    s.reproducir_contenido()