Tabla_multiplicar = int(input("dime el numero para calcular la tabla de multiplicar: "))
for mul_factor in range(1, 10):
    result = Tabla_multiplicar * mul_factor
    print(f'{Tabla_multiplicar} * {mul_factor} = {result}')