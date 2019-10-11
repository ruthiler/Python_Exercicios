num = [2, 5, 9, 21]
print(num)
num[1] = 1
print(num)
num.append(10)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
num.insert(0, 5)
print(num)
num.pop(1)
print(num)
num.remove(1)
print(num)
if 6 in num:
    num.remove(6)
print(num)

valor = []
while True:
    n = int(input('Digite um valor: [999 para sair] '))
    if n == 999:
        break
    valor.append(n)
print(valor)