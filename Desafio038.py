num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if num1>num2:
    print("{} é maior que {}".format(num1,num2))
elif num2>num1:
    print("{} é maior que {}".format(num2,num1))
elif num1==num2:
    print("{} e {} são iguais".format(num1,num2))
