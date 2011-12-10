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
from operator import ne as sao_diferentes

def escolhe_assento_aleatorio(a_partir_do=0):
    return assentos.pop(assentos.index(choice(assentos[a_partir_do:])))    

def escolhe_assento(passageiro):
    try:
        return (passageiro, assentos.pop(assentos.index(passageiro)))
    except ValueError:
        return (passageiro, escolhe_assento_aleatorio())

n_repeticoes = 30000
N = 1000
total_de_passageiros_em_todas_as_repeticoes = N * n_repeticoes
do_ultimo_assento = -1
ULTIMOS_PASSAGEIROS_FORA_DE_SEUS_LUGARES = 0
PASSAGEIROS_FORA_DE_SEUS_LUGARES = []

for vez in range(n_repeticoes):
    passageiros = range(N)
    assentos = range(N)

    passageiro_e_assento = [(passageiros.pop(0), escolhe_assento_aleatorio(a_partir_do=1))]
    total_fora_do_lugar = 1

    while passageiros:
        passageiro_e_assento.append(escolhe_assento(passageiros.pop(0)))
        
        if sao_diferentes(*passageiro_e_assento[do_ultimo_assento]):
            total_fora_do_lugar += 1
            
    # print passageiro_e_assento
    PASSAGEIROS_FORA_DE_SEUS_LUGARES.append(total_fora_do_lugar)
    
    if sao_diferentes(*passageiro_e_assento[do_ultimo_assento]):
        ULTIMOS_PASSAGEIROS_FORA_DE_SEUS_LUGARES += 1

print PASSAGEIROS_FORA_DE_SEUS_LUGARES
print sum(PASSAGEIROS_FORA_DE_SEUS_LUGARES), total_de_passageiros_em_todas_as_repeticoes
print ULTIMOS_PASSAGEIROS_FORA_DE_SEUS_LUGARES, total_de_passageiros_em_todas_as_repeticoes