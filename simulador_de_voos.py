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
# from operator import ne as sao_diferentes

class Aviao:
    numero_de_voos = 0
    passageiros_fora_de_seus_lugares = []
    ultimos_passageiros_fora_de_seus_lugares = 0
    
    def __init__(self, capacidade):
        self.capacidade = capacidade
    
    def novo_voo(self):
        #print self.numero_de_voos,
        self.numero_de_voos += 1
        self.passageiros_fora_de_seus_lugares.append(0)
        self.assentos = range(self.capacidade)
        
        self.passageiro_e_assento = []
        
    def embarca_ultimo(self, passageiro):
        assento = self.embarca(passageiro)
        if assento != passageiro:
            self.ultimos_passageiros_fora_de_seus_lugares += 1

    def embarca(self, passageiro):
        try:
            assento = self.assentos.pop(self.assentos.index(passageiro))
        except ValueError:
            assento = self.assentos.pop(self.assentos.index(choice(self.assentos)))
            # contabiliza este passageiro fora de seu assento:
            self.passageiros_fora_de_seus_lugares[-1] += 1
            
        self.passageiro_e_assento.append((passageiro, assento))
        return assento
        
    def verifica_ultimo_passageiro(self, passageiro, assento):
        pass

    def relatorio_de_voos(self):
        passageiros_transportados = self.numero_de_voos * self.capacidade
        print "total de voos:",
        print self.numero_de_voos
        print "total de passageiros transportados:", 
        print passageiros_transportados
        print "total de passageiros transportados fora de seus lugares:", 
        print sum(self.passageiros_fora_de_seus_lugares)
        print "total de ultimos passageiros transportados fora de seus lugares:", 
        print self.ultimos_passageiros_fora_de_seus_lugares


voos = 1000
passageiros_por_voo = 100

aviao = Aviao(passageiros_por_voo)

# PASSAGEIROS_FORA_DE_SEUS_LUGARES = 0
# ULTIMOS_PASSAGEIROS_FORA_DE_SEUS_LUGARES = 0
while voos > aviao.numero_de_voos:  # quantidade de simulacoes

    passageiros = range(passageiros_por_voo)
    # renomear primeiro passageiro forca escolha aleatoria do assento:
    passageiros[0] = -1

    aviao.novo_voo()
    
    for passageiro in passageiros[:-1]:
        aviao.embarca(passageiro)
        
    aviao.embarca_ultimo(passageiros.pop())
    
    #este_voo = aviao.passageiro_e_assento
    #print este_voo
    # passageiros_fora_de_seus_lugares = len([par for par in este_voo if sao_diferentes(*par)])
    # print passageiros_fora_de_seus_lugares, 'fora de seus assentos'
    # PASSAGEIROS_FORA_DE_SEUS_LUGARES += passageiros_fora_de_seus_lugares
    # if sao_diferentes(*este_voo[-1]):
        # ULTIMOS_PASSAGEIROS_FORA_DE_SEUS_LUGARES += 1
    
# print ULTIMOS_PASSAGEIROS_FORA_DE_SEUS_LUGARES
# print PASSAGEIROS_FORA_DE_SEUS_LUGARES

aviao.relatorio_de_voos()
# print aviao.passageiros_fora_de_seus_lugares
print
print 'passageiros fora de seus assentos:'
print 'media:', mean(aviao.passageiros_fora_de_seus_lugares)
print 'desvio padrao:', std(aviao.passageiros_fora_de_seus_lugares)
print 'mediana:', median(aviao.passageiros_fora_de_seus_lugares)