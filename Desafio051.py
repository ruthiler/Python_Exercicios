#Desafio 051: Desenvolva um programa que leia o primeiro termo 
#e a razao de uma PA. No final, mostre os 10 primeiros termos dessa progressao.

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
for c in range(termo, (razao*10)+10, razao):
    print(c)

