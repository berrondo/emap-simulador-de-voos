# -*- coding: utf-8 -*-
"""
Created on Fri Dez 09 21:34:08 2011

@authors: Claudio, Debora, Gerson

PI Lista 4:
5. Cem passageiros, numerados de 1 a 100, embarcam nesta ordem em um vôo com 100
lugares. O primeiro ignora o lugar reservado para ele e escolhe seu assento ao acaso.
Cada um dos demais senta-se em seu próprio lugar, a menos que ele já esteja
ocupado; se isto ocorrer, o passageiro escolhe seu lugar ao acaso, entre os assentos
ainda livres.
a) Faça uma simulação para estimar a probabilidade de que o passageiro de número 100
sente-se em seu próprio lugar e o número esperado de passageiros que se sentam fora de
seus lugares. Envie um pequeno relatório com os métodos e resultados encontrados.
b) Tente fazer os cálculos da parte a) analiticamente.
"""

from random import choice

n_repeticoes = 1

N = 100
passageiros = range(N)
assentos = range(N)

primeiro_passageiro = passageiros.pop(0)
primeiro_assento_aleatorio = choice(assentos[1:])
assentos.remove(primeiro_assento_aleatorio)
pares = [(primeiro_passageiro, primeiro_assento_aleatorio)]

#print (primeiro_passageiro,primeiro_assento_aleatorio,
#       assentos,passageiros,pares)
       
def assento_aleatorio():
    return assentos.pop(assentos.index(choice(assentos)))    

for vez in range(n_repeticoes):
    while passageiros:
        p = passageiros.pop(0)
        try:
            pares.append((p, assentos.pop(assentos.index(p))))
        except ValueError:
            pares.append((p, assento_aleatorio()))
            
    print pares