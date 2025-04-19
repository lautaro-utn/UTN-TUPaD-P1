# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre_usuario = input("Por favor, ingresa tu nombre: ")
print(saludar_usuario(nombre_usuario))
