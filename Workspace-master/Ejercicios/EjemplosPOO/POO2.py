class cuenta():
    def __init__(self,titular,cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def mostrat (self):
        print(f'Titular: {self.titular}')
        print(f'Cantidad: {self.cantidad}')

cuenta1 = cuenta ()