import os 

os.system("cls")

produto = input("Digite um produto: ")
quantidade = int(input("Digite a quantiadade desejada: "))
preco_unitario = int(input("digite um preço: "))


if quantidade <= 5: 
    print("o desconto será de 2% ")
elif quantidade >= 5 and quantidade <= 10: 
    print("o desconto será de 3% ")
elif quantidade >= 10:
    print("o desconto será de 5%.")


preco_final = quantidade * preco_unitario

print(f"Preço do produto : R$ {preco_unitario:2f}")
print(f"Preço final: R$ {preco_final:2f}")