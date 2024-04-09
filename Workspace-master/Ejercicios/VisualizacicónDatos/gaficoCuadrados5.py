import matplotlib.pyplot as plt

#cuadrados=[1,4,9,16,25]
valores= [n for n in range (1,5001)]
cubos = [n**3 for n in valores]
fig, ax = plt.subplots()
ax.plot(valores, cubos)

ax.set_title("Cubos de los números", fontsize=18)
ax.set_xlabel("Valor", fontsize=12)
ax.set_ylabel("Cubo del valor", fontsize=12)

ax.tick_params(axis='both', labelsize=12)

plt.show()
fig.savefig('graficoCubos.png')
#reto: Crear una list comprehension de los cuadrados de los 100 primeros números en lugar de introducirlos a mano.

# Informacion de la libreria: https://matplotlib.org/cheatsheets/
# Documentación: https://matplotlib.org/stable/index.html
# Tipos de gráficos: https://matplotlib.org/stable/plot_types/index.html
# Ejemplos: https://matplotlib.org/stable/gallery/index.html