Numero = int(input("introduce el numero: "))
suma_actual = 0
mult_3_actual = 0
print(f'M={mult_3_actual:2d}: S={suma_actual:2d}')

while suma_actual < Numero:
    mult_3_actual += 3
    suma_actual += mult_3_actual
    print(f'M={mult_3_actual:2d}: S={suma_actual:2d}')