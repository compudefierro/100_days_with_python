# Printing
print('Hola mundo')
print('Hola mundo\n'*3)

# Commenting
print('Hola mundo', '!'*3) # Imprime el mensaje 'Hola mundo!!!' utilizando repetición de caracteres para agregar tres signos de exclamación.

# String Manipulation
# Concatenación (+)
print('Conca' + 'tenación')
# Repetición (*)
print('Repetición ' * 3)
# División (split())
print('hola todos'.split())
# Búsqueda (find(), in)
print('hola todos'.find('todos'))
# Reemplazo (replace())
print('Hola algunos'.replace('algunos', 'todos'))
# Cambiar mayúsculas/minúsculas (upper(), lower())
print('hola todos'.upper())
print('hola todos'.upper().lower())
# Recorte de espacios (strip()), entre otros.
print('  hola   todos  ,  yo  soy   '.strip())
# todo lo anterior en un ejemplo (menos repetición)
print(' '.join('  hola   todos  ,  yo  soy   '.strip().split()).replace(' ,', ','))

# Variables
nombre = 'pan jamon queso lechuga tomate'
lista = nombre.split()
print(f'Ingredientes de un sanguche: {lista}')

# Debugging
# Debugging: proceso de encontrar y corregir errores en el código.
# Debug: mostramos el valor de la variable para verificar que sea el esperado.
nombre = 'John Connor'
print(nombre)

# input y variables
nombre = input('Ingrese su nombre: ')
print(f'Hola {nombre}, ¿cómo estás?')
print(f'Hola {nombre}, tu nombre tiene {len(nombre.replace(" ",""))} letras.')