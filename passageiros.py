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
from operator import eq

class Aviao:
    numero_de_voos = 0
    historico_de_passageiros_fora_de_seus_lugares = []
    historico_de_ultimos_passageiros_fora_de_seus_lugares = []
    passageiros_fora_de_seus_lugares_no_voo = 0
    ultimo_assento = -1
    
    def novo_voo(self, numero_de_assentos):
        self.numero_de_voos += 1
        self.historico_de_passageiros_fora_de_seus_lugares.append(self.passageiros_fora_de_seus_lugares_no_voo)
        self.passageiros_fora_de_seus_lugares_no_voo = 0
        self.assentos = range(numero_de_assentos)
    
    def escolhe_assento_aleatorio(self, a_partir_do=0):
        self.passageiros_fora_de_seus_lugares_no_voo += 1
        return self.assentos.pop(self.assentos.index(choice(self.assentos[a_partir_do:])))    

    def escolhe_assento(self, passageiro):
        try:
            return (passageiro, self.assentos.pop(self.assentos.index(passageiro)))
        except ValueError:
            return (passageiro, self.escolhe_assento_aleatorio())
            
    def ultimo_passageiro_esta_em_seu_assento(self):
        return eq(*passageiro_e_assento[self.ultimo_assento])


n_repeticoes = 3000
N = 100
do_ultimo_assento = -1
ULTIMOS_PASSAGEIROS_FORA_DE_SEUS_LUGARES = 0

aviao = Aviao()

for vez in range(n_repeticoes):
    passageiros = range(N)
    
    aviao.novo_voo(N)

    passageiro_e_assento = [(passageiros.pop(0), aviao.escolhe_assento_aleatorio(a_partir_do=1))]

    while passageiros:
        passageiro_e_assento.append(aviao.escolhe_assento(passageiros.pop(0)))
    
    if not eq(*passageiro_e_assento[do_ultimo_assento]):
        ULTIMOS_PASSAGEIROS_FORA_DE_SEUS_LUGARES += 1

print "total de passageiros transportados:", aviao.numero_de_voos * N
print "total de passageiros transportados fora de seus lugares:", sum(aviao.historico_de_passageiros_fora_de_seus_lugares)
print "total de ultimos passageiros transportados fora de seus lugares:", ULTIMOS_PASSAGEIROS_FORA_DE_SEUS_LUGARES, aviao.numero_de_voos * N