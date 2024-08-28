# Solicita ao usuário para digitar os números
num1 = float(input("Digite o primeiro número: "))
operador = input("Escolha a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

# Realiza a operação baseada no operador fornecido
if operador == '+':
    resultado = num1 + num2
elif operador == '-':
    resultado = num1 - num2
elif operador == '*':
    resultado = num1 * num2
elif operador == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro! Divisão por zero."
else:
    resultado = "Operação inválida."

# Exibe o resultado
print("Resultado:", resultado)
