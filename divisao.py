# Solicita ao usuário para digitar os números
numerador = float(input("Digite o numerador: "))
denominador = float(input("Digite o denominador: "))

# Verifica se o denominador é diferente de zero
if denominador != 0:
    resultado = numerador / denominador
    print("Resultado:", resultado)
else:
    print("Erro! Divisão por zero.")
