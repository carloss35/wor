from tkinter import *

#Iniciar variables globales
operacion= ' '
numero1 = 0

#Función de ayuda
def operacion (op):
    global numero1
    global operacion
    numero1 = float(textbox.get())
    operacion = op
    textbox.delete(0, END)

#funciones de los botones
def add():
    operacion ('+')
def minus():
    operacion ('-')
def times():
    operacion('*')
def divide():
    operacion('/')
def clear():
    textbox.delete(0, END)
def evaluate():
    numero2 = float(textbox.get())

    #Crear cuadro de salida del texto
    textbox.delete(0, END)

    #Hacer el calculo y mostrar la solución
    if operacion == '+':
        textbox.insert(END, numero1 + numero2)
    elif operacion == '-':
        textbox.insert(END, numero1 - numero2)
    elif operacion == '*':
        textbox.insert(END, numero1 * numero2)
    elif operacion == '/':
        textbox.insert(END, numero1 / numero2)
    else:
        textbox.insert(END, 'Error')

#Crea la ventana principal
ventana = Tk()
ventana.title('Calculadora')

#Creación de un marco
textbox= Entry(ventana, width=20)
textbox.grid(row=0, column=0, columnspan=3)

#Crear las operaciones
Button_add = Button(ventana, text='+', width=3, command=add)
Button_add.grid(row=2, column=0)
Button_substract = Button(ventana, text='-', width=3, command=minus)
Button_substract.grid(row=2, column=1)
Button_multiply = Button(ventana, text='*', width=3, command=times)
Button_multiply.grid(row=3, column=0)
Button_divide = Button(ventana, text='/', width=3, command=divide)
Button_divide.grid(row=3, column=1)
Button_equals = Button(ventana, text='=', width=6, command=evaluate)
Button_equals.grid(row=0, column=2, columnspan=2)
Button_clear = Button(ventana, text='CLEAR', width=6, command=clear)
Button_clear.grid(row=4, column=2, sticky=E)

# Bucle evento principal
ventana.mainloop()