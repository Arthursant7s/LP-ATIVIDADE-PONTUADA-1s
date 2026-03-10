import os 

os.system

print("Solicitando Dados")

primeiro_numA = int(input("Digite um valor: "))
segundo_numB = int(input("Digite um valor: "))
terceiro_numC = int(input("Digite um valor: "))

media = (primeiro_numA + segundo_numB + terceiro_numC)

if primeiro_numA + segundo_numB > terceiro_numC:
    print("A soma de A E B é maior que C")
else: 
    ("A + B é menor do que C")

print(f"Media: {media}")

