import math
import random
from spellchecker import SpellChecker
from itertools import permutations
    
spell = SpellChecker(language='pt')

def verify_word(word, spell=spell):

    return word in spell

def get_permutations(s):
    permutacoes = permutations(s)
    resultado = [''.join(p) for p in permutacoes]

    return resultado

def make_possibilities_list(letters_string):
    letters_list = list(letters_string)
    words = get_permutations(letters_string)
    total_words_number = math.factorial(len(letters_list))

    result_words = []
    for i in range(3, len(letters_list)+1):
        for word in words:
            if verify_word(word[:i]):
                if word[:i].upper() not in result_words:
                    result_words.append(word[:i].upper())

    return result_words

def filter_by_letters(words, n):
    result_words = []    
    for word in words:
        if len(word)==n:
            result_words.append(word)
    
    return result_words

def filter_by_letter_position(words, letter, n):
    result_words = []    
    for word in words:
        if word[n:n+1]==letter.upper():
            result_words.append(word)
    
    return result_words
    
# COLOCAR LETRAS
letras = 'esoatrin'
lista_poss = make_possibilities_list(letras)
# COLOCAR TAMANHO DA PALAVRA
filtro_tamanho = False
if filtro_tamanho:
    tamanho = 7
    lista_poss = filter_by_letters(lista_poss, tamanho)
# COLOCAR POSIÇÕES DAS LETRAS
filtro_posicao = False
if filtro_posicao:
    posicoes = [('s', 6)]
    for posicao in posicoes:
        lista_poss = filter_by_letter_position(lista_poss, posicao[0], posicao[1])

dicionario_resultado = dict()
for i in range(3, len(letras)+1):
    lword = []
    for word in lista_poss:
        if len(word)==i:
            lword.append(word)
    dicionario_resultado[i] = lword

for key in dicionario_resultado.keys():
    print(f"\nPalavras com {key} letras:")
    print(dicionario_resultado[key])