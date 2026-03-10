import os 

os.system

valor1 = int(input("Digite um valor: "))
caractere = input("+ - * / : ")
valor2 = int(input("Digite um valor: "))

operacao = input("Digite a operação (+, -, * ou /): ")

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

if operacao == "+":
    resultado = A + B
elif operacao == "-":
    resultado = A - B
elif operacao == "*":
    resultado = A * B
elif operacao == "/":
    resultado = A / B
else:
    print("Operação inválida!")
    resultado = None

if resultado is not None:
    print("Resultado:", resultado)