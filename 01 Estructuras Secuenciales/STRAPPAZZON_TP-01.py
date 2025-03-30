
# 1)Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
def hello_world():
  print("Hola mundo!")

hello_world()

# 2)Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”
def greet():
  name = input("Ingresa tu nombre: ")
  print(f"Hola {name}!")

greet()

# 3)Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”
def introduce():
  name = input("Ingresa tu nombre: ")
  last_name = input("Ingresa tu apellido: ")
  age = input("Ingresa tu edad: ")
  address = input("Ingresa tu país de residencia: ")
  print(f"Soy {name} {last_name}, tengo {age} años y vivo en {address}")

introduce()

# 4)Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.
import math

def calcular_circulo():
  radio = int(input("Ingresa el radio de tu círculo: "))
  area = math.pi*radio**2
  perimetro = 2*math.pi*radio
  print(f"Un círculo con radio {radio} tiene un perímetro de {perimetro} y un área de {area}")

calcular_circulo()

# 5)Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

def seconds_to_hours():
  seconds = int(input("Ingrese una cantidad de segundos: "))
  print(f"{seconds} segundos equivalen a {seconds/60/60} horas")

seconds_to_hours()

# 6)Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.
def tabla_multiplicar():
  num = int(input("Ingrese un número: "))
  print(f"{num} * 0 = {num*0}")
  print(f"{num} * 1 = {num*1}")
  print(f"{num} * 2 = {num*2}")
  print(f"{num} * 3 = {num*3}")
  print(f"{num} * 4 = {num*4}")
  print(f"{num} * 5 = {num*5}")
  print(f"{num} * 6 = {num*6}")
  print(f"{num} * 7 = {num*7}")
  print(f"{num} * 8 = {num*8}")
  print(f"{num} * 9 = {num*9}")
  print(f"{num} * 10 = {num*10}")

tabla_multiplicar()

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
def get_int_from_user():
  try:
    num = input("Ingrese un número entero distinto de 0: ")
    num = int(num)
  except ValueError:
    raise ValueError("Debe ingresar un número")
  return num

def operaciones():
  num1 = get_int_from_user()
  num2 = get_int_from_user()
  if num1 == 0 or num2 == 0:
    print("Ambos números deben ser distintos de 0")
    return
  print(f"{num1} + {num2} = {num1+num2}")
  print(f"{num1} - {num2} = {num1-num2}")
  print(f"{num1} * {num2} = {num1*num2}")
  print(f"{num1} / {num2} = {num1/num2}")

operaciones()

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal

def calcular_masa_corporal():
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    print(f"su masa corporal es {peso/altura**2}")

calcular_masa_corporal()

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit
def celsius_to_fahrenheit():
    celsius = float(input("Ingrese una temperatura en celsius: "))
    print(f"{celsius} grados Celsius equivalen a {9/5*celsius+32} grados Fahrenheit")

celsius_to_fahrenheit()

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.
def promedio():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercero número: "))
    print(f"El promedio de los tres números es {(num1+num2+num3)/3}")

promedio()