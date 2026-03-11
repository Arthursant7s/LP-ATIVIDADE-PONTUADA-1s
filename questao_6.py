import os 

os.system 

primeiro_num = float(input("Digite um valor: "))
segundo_num = float(input("Digite um valor: "))


media = (primeiro_num + segundo_num) / 2

if media >= 6:
    print("Parabéns aluno aprovado ")
else: 
    print("Que pena aluno reprovado")


print(f"Media: {media} do aluno.")
