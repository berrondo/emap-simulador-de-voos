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


def assento_aleatorio(a_partir_do_indice=0):
    return assentos.pop(assentos.index(choice(assentos[a_partir_do_indice:])))    

def escolhe_assento(p):
    try:
        return (p, assentos.pop(assentos.index(p)))
    except ValueError:
        return (p, assento_aleatorio())

n_repeticoes = 10
N = 20
for vez in range(n_repeticoes):
    passageiros = range(N)
    assentos = range(N)

    pares = [(passageiros.pop(0), assento_aleatorio(a_partir_do_indice=1))]

    while passageiros:
        pares.append(escolhe_assento(passageiros.pop(0)))
            
    print pares