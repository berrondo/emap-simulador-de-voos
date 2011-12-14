# -*- coding: utf-8 -*-
"""
Created on Fri Dez 09 21:34:08 2011

@authors: Claudio, Debora, Gerson, Diego, Andre Almeida
"""
"""
    PI Lista 4:
    5. Cem passageiros, numerados de 1 a 100(*), embarcam nesta ordem em um vôo com 100
    lugares. O primeiro ignora o lugar reservado para ele e escolhe seu assento ao acaso.
    Cada um dos demais senta-se em seu próprio lugar, a menos que ele já esteja
    ocupado; se isto ocorrer, o passageiro escolhe seu lugar ao acaso, entre os assentos
    ainda livres.
    a) Faça uma simulação para estimar a probabilidade de que o passageiro de número 100(**)
    sente-se em seu próprio lugar e o número esperado de passageiros que se sentam fora de
    seus lugares. Envie um pequeno relatório com os métodos e resultados encontrados.
    b) Tente fazer os cálculos da parte a) analiticamente.

    (*) no codigo seguinte eles foram numerados de 0 a 99.
    (**) 99
  """

from random import choice
from numpy import mean, std, median

class Aviao:
    numero_de_voos = 0
    passageiros_fora_de_seus_assentos = []
    ultimos_passageiros_no_assento_correto = 0
    
    def __init__(self, capacidade):
        self.capacidade = capacidade
    
    def novo_voo(self):
        #print self.numero_de_voos,
        self.numero_de_voos += 1
        self.passageiros_fora_de_seus_assentos.append(0)
        self.assentos = range(self.capacidade)
        
        self.passageiro_e_assento = []
        
    def embarca(self, passageiro):
        try:
            assento = self.assentos.pop(self.assentos.index(passageiro))
        except ValueError:
            assento = self.assentos.pop(self.assentos.index(choice(self.assentos)))
            # contabiliza este passageiro fora de seu assento:
            self.passageiros_fora_de_seus_assentos[-1] += 1
            
        self.passageiro_e_assento.append((passageiro, assento))
        return assento
        
    def verifica_o_ultimo(self, passageiro_esta, em_seu_assento):
        if passageiro_esta == em_seu_assento:
            self.ultimos_passageiros_no_assento_correto += 1

    def relatorio_de_voos(self):
        numero_de_voos = self.numero_de_voos
        passageiros_transportados = self.numero_de_voos * self.capacidade
        passageiros_fora_de_seus_assentos = sum(self.passageiros_fora_de_seus_assentos)
        ultimos_passageiros_no_assento_correto = self.ultimos_passageiros_no_assento_correto
        print "total de voos:",
        print numero_de_voos
        print "total de passageiros transportados:", 
        print passageiros_transportados
        print "total de passageiros fora de seus assentos:", 
        print passageiros_fora_de_seus_assentos,
        print "(%.2f%%)" % ((1.0*passageiros_fora_de_seus_assentos / passageiros_transportados) * 100)
        print "total de ultimos passageiros no assento correto:", 
        print ultimos_passageiros_no_assento_correto,
        print "em", self.numero_de_voos,
        print "(%.2f%%)" % ((1.0*ultimos_passageiros_no_assento_correto / numero_de_voos) * 100)


voos = 1000
passageiros_por_voo = 100

aviao = Aviao(passageiros_por_voo)

while voos > aviao.numero_de_voos:  # quantidade de simulacoes

    passageiros = range(passageiros_por_voo)
    # renomear primeiro passageiro forca assento aleatorio:
    passageiros[0] = -1

    aviao.novo_voo()
    
    for passageiro in passageiros:
        em_seu_assento = aviao.embarca(passageiro)
        
    aviao.verifica_o_ultimo(passageiro, em_seu_assento)
    
aviao.relatorio_de_voos()
# print aviao.passageiros_fora_de_seus_assentos
print
print 'passageiros fora de seus assentos:'
print 'media:', mean(aviao.passageiros_fora_de_seus_assentos)
print 'desvio padrao:', std(aviao.passageiros_fora_de_seus_assentos)
print 'mediana:', median(aviao.passageiros_fora_de_seus_assentos)