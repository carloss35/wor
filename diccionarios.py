direcciones = {
    'juan': 'C/Moncofar, 5',
    'antonio': 'C/Enmedio, 15',
    'jose': 'C/Mayor, 30'
}

#print(direcciones.get('juan'))
for nombre, direccion in direcciones.items():
    print(f'{nombre}: {direccion}')


