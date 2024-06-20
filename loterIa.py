import random # importa uma bibliotera para gerar números randômicos

def numeros_loteria():
    numeros = random.sample(range(1, 61), 6) # .sample serve para falar que nos queremos números inteiros e range para dar um range de numeração
    return numeros # return retorna o resultado da variável para a igualdade da função , sendo assim você pode tirar o resutado obtido durante a função interna 

numeros_aleatorios = numeros_loteria() # Realocando o valor obtido de uma função para uma variável
print("Esses são os números aléatorios para você pode jogar na loteria:", numeros_aleatorios)