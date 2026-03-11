import os 

os.system 


morango = float(input("Kg de morango : "))
maça = float(input("Kg de maça"))

if morango <= 5:
    preco_morango = morango * 2,50 
else:
    preco_maça = maça * 2,50 

if morango <= 5:
    preco_morango = morango * 1,80
else:
    preco_maça = maça * 1,80 
    
total = preco_morango + preco_maça
peso_total = morango + maça 

if peso_total >= 10 or total > 15:
    total = total * 0.90


print("Total a pagar: R$, TOTAL ")
