from __future__ import division
import datetime
from numpy.random import randint

voos = 1000000
passageiros = 100
ultimos_fora_do_lugar = 0
foras_do_lugar = 0

inicio = datetime.datetime.now()

for i in xrange(voos):
    escolhido = randint(passageiros)
    if escolhido == 0: continue
    else: foras_do_lugar += 1
    
    while True:
        try:
            if escolhido == 98:
                ultimos_fora_do_lugar += 1
                break
            escolhido = randint(escolhido+1, passageiros)
            foras_do_lugar += 1
        except ValueError:
            break
            
print voos * passageiros, 'em', (datetime.datetime.now() - inicio).seconds, 's'
print ((foras_do_lugar + ultimos_fora_do_lugar) / (voos * passageiros)) * 100, "% fora do lugar"
print (ultimos_fora_do_lugar / voos) * 100, "% ultimos fora do lugar"