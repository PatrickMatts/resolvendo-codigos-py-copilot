# Como entrada, receba um número inteiro e verifique se ele é par ou ímpar.

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")

#   Exemplo de entrada: 5
#   Saída esperada: O número 5 é ímpar.
