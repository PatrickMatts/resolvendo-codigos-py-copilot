# Vamos testar se uma palavra é um palíndromo?!

def palindromo(palavra):
    palavra = palavra.lower()
    return palavra == palavra[::-1]

if __name__ == '__main__':

    palavra = input('Digite uma palavra: ')
    if palindromo(palavra):
        print('É um palíndromo!')
    else:
        print('Não é um palíndromo!')

# Exemplo de execução
# Digite uma palavra: arara
# É um palíndromo!

# Digite uma palavra: python
# Não é um palíndromo!
