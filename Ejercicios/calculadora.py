def calculadora(num1,num2, oper):
    if operacion == "+":
        resultado = num1 + num2 
    elif operacion == "-":
        resultado = num1 - num2 
    elif operacion == "*":
        resultado = num1 * num2 
    else:
        resultado = num1 / num2 
    return resultado

valor1 = int(input('Introduce el primer numero: '))
valor2 = int(input('Introduce el segundo numero: '))
operacion = (input('Introduce la operación aritmética (+, -, * o /): '))
while operacion not in  ("+" , "-" , "*", "/"):
    print("Debes introducir una operación correcta, vuelve a intentarlo")
    operacion = input("Introduce la operación aritmética (+, -, * o /): ")

print(f'El resultado de la operación aritmética de {valor1} {operacion} {valor2} es: {calculadora(valor1,valor2,operacion)}')