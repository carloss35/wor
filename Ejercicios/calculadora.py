valor1 = int(input('Introduce el primer numero: '))
valor2 = int(input('Introduce el segundo numero: '))
operacion = (input('Introduce la operación aritmética (+, -, * o /): '))
resultado_final = 0

if operacion == "+":
    resultado_final = valor1 + valor2 
elif operacion == "-":
    resultado_final = valor1 - valor2 
elif operacion == "*":
    resultado_final = valor1 * valor2 
else:
    resultado_final = valor1 / valor2 

print(f'El resultado de la operación aritmética de {valor1} {operacion} {valor2} es: {resultado_final}')