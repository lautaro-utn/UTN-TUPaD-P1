# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
def verificar_mayoria_edad():
    edad = int(input("Por favor, ingrese su edad: "))

    if edad > 18:
        print("Es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”
def verificar_aprobacion():
    nota = float(input("Por favor, ingrese su nota: "))

    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par".
def verificar_numero_par():
    numero = int(input("Por favor, ingrese un número: "))

    if numero % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.
def categorizar_edad():
    edad = int(input("Por favor, ingrese su edad: "))

    if edad < 12:
        print("Niño/a")
    elif 12 <= edad < 18:
        print("Adolescente")
    elif 18 <= edad < 30:
        print("Adulto/a joven")
    else:
        print("Adulto/a")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
def verificar_contrasena():
    contrasena = input("Por favor, ingrese una contraseña: ")

    if 8 <= len(contrasena) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media 
# y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")

print(f"Moda: {moda}, Mediana: {mediana}, Media: {media}")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
def verificar_terminacion_vocal():
    texto = input("Por favor, ingrese una frase o palabra: ")
    if texto[-1].lower() in 'aeiou':
        texto += '!'
    print(texto)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla.
def transformar_nombre():
    nombre = input("Por favor, ingrese su nombre: ")
    print("Seleccione una opción:")
    print("1. Nombre en mayúsculas")
    print("2. Nombre en minúsculas")
    print("3. Nombre con la primera letra mayúscula")
    
    opcion = int(input("Ingrese el número de la opción deseada (1, 2 o 3): "))
    
    if opcion == 1:
        print(nombre.upper())
    elif opcion == 2:
        print(nombre.lower())
    elif opcion == 3:
        print(nombre.title())
    else:
        print("Opción no válida")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla.
def clasificar_terremoto():
    magnitud = float(input("Por favor, ingrese la magnitud del terremoto: "))

    if magnitud < 3:
        print("Muy leve (imperceptible)")
    elif 3 <= magnitud < 4:
        print("Leve (ligeramente perceptible)")
    elif 4 <= magnitud < 5:
        print("Moderado (sentido por personas, pero generalmente no causa daños)")
    elif 5 <= magnitud < 6:
        print("Fuerte (puede causar daños en estructuras débiles)")
    elif 6 <= magnitud < 7:
        print("Muy Fuerte (puede causar daños significativos)")
    else:
        print("Extremo (puede causar graves daños a gran escala)")

# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano
def determinar_estacion():
    hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").strip().upper()
    mes = int(input("Por favor, ingrese el mes del año (1-12): "))
    dia = int(input("Por favor, ingrese el día del mes: "))

    if hemisferio not in ['N', 'S']:
        print("Hemisferio no válido. Por favor, ingrese 'N' para norte o 'S' para sur.")
        return

    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "Invierno" if hemisferio == 'N' else "Verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion = "Primavera" if hemisferio == 'N' else "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion = "Verano" if hemisferio == 'N' else "Invierno"
    elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <= 20):
        estacion = "Otoño" if hemisferio == 'N' else "Primavera"
    else:
        print("Fecha no válida.")
        return

    print(f"Usted se encuentra en {estacion}.")