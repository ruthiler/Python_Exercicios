num = int(input("Digite um nnúmero inteiro: "))
print("Quer converter para:\n1 - Binário;\n2 - Octal;\n3 - Hexadecimal;")
conversao = int(input("Escolha: "))

if conversao == 1:
    print("{} em bínario é {}".format(num,bin(num)))
elif conversao == 2:
    print("{} em Octal é {}".format(num,oct(num)))
elif conversao == 3:
    print("{} em Hexadecimal é {}".format(num,hex(num)))





