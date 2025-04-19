# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Por favor, ingresa tu peso en kilogramos: "))
altura = float(input("Por favor, ingresa tu altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")