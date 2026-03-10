import os

os.system 

renda = float(input("Digite a renda mensal: "))
emprestimo = float(input("Digite o valor total do empréstimo: "))
prestacoes = int(input("Digite o número de prestações: "))

# cálculo do valor de cada prestação
valor_prestacao = emprestimo / prestacoes

# verificação das regras
if emprestimo <= renda * 10 and valor_prestacao <= renda * 0.30:
    print("Empréstimo pode ser concedido.")
else:
    print("Empréstimo não pode ser concedido.")

print("Valor da prestação:", valor_prestacao)