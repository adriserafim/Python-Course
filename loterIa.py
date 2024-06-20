import random # importa uma bibliotera para gerar números randômicos

# Com a alteração dos requisitos fazendo com que hája números com um aumento de probabilidade de ser escolhido, a ferramenta .sample fica sendo inviável utilizala
# Isso porque essa feramente gera numeros simples e inteiros sem repetições do jeito que quermos, porem não oferece uma opção de verificar pesos 
#def numeros_loteria():
#    numeros = random.sample(range(1, 61), 6) # .sample Serve para falar que nos queremos números inteiros e range para dar um range de numeração, e o número 6 serve para ele repetir essa ação 6 vezes antes de ira para próxima etapa
#    return numeros # Retorna o resultado da variável para a igualdade da função , sendo assim você pode tirar o resutado obtido durante a função interna 

# Como a alteração dos requisitos foram alteradas para que os número não possam serem repitidos teremos que adicionar cofigurações funão e como eu nao quero perder os comentarios de explicação e o proprio código base eu irei comentar
# esse e irei colocar a nova linha de código com as linha adicionadas
#def numeros_loteria(pesos, n=6): # (pesos, n6) Faz com que a váriavel peso e a váriavel n "número de numeros que seram feitos" entre na função
#    numeros = range(1, 61)
#    numeros_ponderados = random.choices(numeros, weights=pesos, k=n) # .choices Ira retornar um números aleatório, essa feramenta tem a opição de colocar peso na escolha colocando a codificação de weights 
#    return numeros_ponderados

def numeros_loteria(pesos, n=6):
    numeros = list(range(1, 61))
    numeros_selecionados = [] # Isso esta criando uma matriz em branco que nos iremos utilizar como lista

    for _ in range(n):
        numero = random.choices(numeros, weights=pesos, k=1)[0] # [0] Indica a locação que você quer coloar o valor desejado, lembrando que a matriz começa em 0 (Zero)
        numeros_selecionados.append(numero)
        
        # Remover o número selecionado para evitar repetição
        index = numeros.index(numero) # Serve para encontra o índice do numero na lista numeros.
        del numeros[index] # Serve para remove o número selecionado da lista numeros para garantir que não será selecionado novamente.
        del pesos[index] # Remove o peso correspondente da lista pesos para manter as listas sincronizadas.
        
    return numeros_selecionados

# Defina os pesos para cada número de 1 a 60
# Neste exemplo, o peso padrão é 1 para todos os números
pesos = [1] * 60

# Aumente a probabilidade de certos números:
# Dar peso 10 para o número 7, 20 para o número 13 e 15 para o número 42
pesos[6] = 10 # PRESTE ATENÇÂO: A pesar de estar pesos[6] o numero que esta sendo favorecido é o numero 7
pesos[12] = 20
pesos[41] = 15
# LEMBRETE: O valor dessa igualdade não é igual a porcentagem de escolha mas sim um recutado de uma conta de chance

# CALCULO MATEMATICO DA PROBABILIDADE
# Soma dos Pesos: A soma total dos pesos é (1*59 + 10 = 69)
# Probabilidade do Número 7: A probabilidade de o número 7 ser escolhido é (10/69), enquanto a probabilidade de qualquer
# outro número (com peso '1') ser escolhido é (1/69)

numeros_aleatorios = numeros_loteria(pesos) # Realocando o valor obtido de uma função para uma variável
print("Esses são os números aléatorios para você pode jogar na loteria:", numeros_aleatorios)