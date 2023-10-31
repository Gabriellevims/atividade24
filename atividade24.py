# Exercício Python 24: Refaça a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.
print("Tabuada")
numero= int(input("Digite o número:"))
for i in range (11):
    print(f"{numero}x{i}={numero * i}")
