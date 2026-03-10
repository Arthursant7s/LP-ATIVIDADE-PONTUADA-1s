import os 

os.system

nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo: ")
estado_civil = input("Digite seu estado civil: ")
tempo_de_casamento = int(input("Digite o seu tempo de casamento: "))


if sexo == "F" and estado_civil == "CASADA":
    tempo = int(input("Digite o tempo de casada (em anos): "))

print("\n--- DADOS DO USUÁRIO ---")
print("Nome:", nome)
print("Sexo:", sexo)
print("Estado civil:", estado_civil)

if sexo == "F" and estado_civil == "CASADA":
    print("Tempo de casada:", tempo, "anos")