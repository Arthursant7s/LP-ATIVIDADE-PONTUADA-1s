import os 

os.system

quantidade_a = int(input("Digite a quantidade de alcool desejado: "))
quantidade_g = int(input("Digite a quantidade de gasolina desejada: "))
valores =""

print("""
      
ALCOOL      ATÉ 25 LITROS, DESCONTO DE 2% POR LITRO
            ACIMA DE 25 LITROS, DESCONTO DE 4% POR LITRO
            PREÇO:  R$ 3,79

GASOLINA     ATÉ 25 LITROS, DESCONTO DE 3% POR LITRO           
              ACIMA DE 25 LITROS, DESCONTO DE 5% POR LITRO
            PREÇO: R$ 6,59 
""")


if quantidade_a == 25: 
    print("o desconto será de 2% ")
elif quantidade_a >= 25: 
    print("o desconto será de 4% ")
elif quantidade_g == 25:
    print("o desconto será de 3%.")
elif quantidade_g >= 25:
    print("o desconto será de 5%.")





