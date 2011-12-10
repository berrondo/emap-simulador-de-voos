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

class Aviao:
    numero_de_voos = 0
    historico_de_passageiros_fora_de_seus_lugares = []
    total_de_ultimos_passageiros_fora_de_seus_lugares = 0
    ultimo_assento = -1
    
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.passageiro_e_assento = [(0, 0)]
    
    def novo_voo(self):
        self.numero_de_voos += 1
        self.historico_de_passageiros_fora_de_seus_lugares.append(0)
        
        if self.ultimo_passageiro_nao_esta_em_seu_assento():
            self.total_de_ultimos_passageiros_fora_de_seus_lugares += 1
            
        self.passageiro_e_assento = []
        self.assentos = range(self.capacidade)
    
    def _escolhe_assento_aleatorio(self, a_partir_do=0):
        self.historico_de_passageiros_fora_de_seus_lugares[-1] += 1
        return self.assentos.pop(self.assentos.index(choice(self.assentos[a_partir_do:])))    

    def escolhe_assento(self, passageiro):
        try:
            return self.assentos.pop(self.assentos.index(passageiro))
        except ValueError:
            return self._escolhe_assento_aleatorio()
            
    def embarca(self, passageiro):
        if passageiro == 0:  # o primeiro passageiro escolhe qualquer assento exceto o seu:
            self.passageiro_e_assento.append((passageiro, self._escolhe_assento_aleatorio(a_partir_do=1)))
        else:
            self.passageiro_e_assento.append((passageiro, self.escolhe_assento(passageiro)))
            
    def ultimo_passageiro_nao_esta_em_seu_assento(self):
        return sao_diferentes(*self.passageiro_e_assento[self.ultimo_assento])
        
    def relatorio_de_voos(self):
        print "total de passageiros transportados:", 
        print self.numero_de_voos * self.capacidade
        print "total de passageiros transportados fora de seus lugares:", 
        print sum(self.historico_de_passageiros_fora_de_seus_lugares)
        print "total de ultimos passageiros transportados fora de seus lugares:", 
        print self.total_de_ultimos_passageiros_fora_de_seus_lugares, self.numero_de_voos * self.capacidade


voos = 10000
passageiros_por_voo = 100
passageiros_transportados = passageiros_por_voo * voos

aviao = Aviao(passageiros_por_voo)

while voos:  # quantidade de simulacoes
    passageiros = xrange(passageiros_por_voo)

    aviao.novo_voo()

    for passageiro in passageiros:
        aviao.embarca(passageiro)
        
    voos -= 1
    
aviao.relatorio_de_voos()