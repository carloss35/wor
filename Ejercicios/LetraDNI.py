letraDNI = ('T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E')
dni = int(input('Dime tus numeros del DNI y yo te calcularé la letra: '))
print(f"PosicionLista: {dni%23}")
print(f'La letra para el DNI {dni} es : {letraDNI[dni%23]}')