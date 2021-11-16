print("-------------------------------------")
print("|                                   |")
print("|           CALCULADORA             |")
print("|                                   |")
print("-------------------------------------")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
res = 0
print("Digite o tipo de operação que deseja, sendo: ")
print("ADIÇÃO = 1")
print("SUBTRAÇÃO = 2")
print("MULTIPLICAÇÃO = 3")
print("DIVISÃO = 4")
c = int(input("Operação: "))
if c == 1:
    res = n1 + n2
    print("O resultado do cálculo é: {}".format(res))
elif c == 2:
    res = n1 - n2
    print("O resultado do cálculo é: {}".format(res))
elif c == 3:
    res = n1 * n2
    print("O resultado do cálculo é: {}".format(res))
elif c == 4:
    res = n1 / n2
    print("O resultado do cálculo é: {}".format(res))
else:
    print("Operação inválida")