# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea
def print_numbers():
    for i in range(101):
        print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
def count_digits() -> int:
    number = int(input("Enter a number): "))
    return len(str(number))

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
def sum_numbers() -> int:
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
    sum = 0
    for i in range(start + 1, end):
        sum += i
    return sum

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
def sum_sequence() -> int:
    sum = 0
    while True:
        number = int(input("Enter a number (0 to exit): "))
        if number == 0:
            break
        sum +=  number
    return sum

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número
import random

def guess_number():
    number = random.randint(0, 9)
    attempts = 0
    while True:
        guess = int(input("Guess a number between 0 and 9: "))
        attempts += 1
        if guess == number:
            break
        print("Wrong guess. Try again.")
    print(f"Congratulations! You guessed the number in {attempts} attempts.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente
def print_even_numbers():
    for i in range(100, -1, -2):
        print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario
def sum_numbers_positive() -> int:
    number = int(input("Enter a positive number: "))
    sum = 0
    for i in range(number + 1):
        sum += i
    return sum

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
def count_numbers(numOfNumbers: int) -> tuple:
    even = 0
    odd = 0
    positive = 0
    negative = 0
    for i in range(numOfNumbers):
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
        if number > 0:
            positive += 1
        elif number < 0:
            negative += 1
    return even, odd, positive, negative

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
def calculate_average(numOfNumbers: int) -> float:
    sum = 0
    for i in range(numOfNumbers):
        number = int(input("Enter a number: "))
        sum += number
    return sum / numOfNumbers   

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
def reverse_number() -> int:
    number = input("Enter a number: ")
    reversed_number = ""
    for digit in number:
        reversed_number = digit + reversed_number
    return int(reversed_number)
