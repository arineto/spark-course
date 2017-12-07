#!/usr/bin/env python
# -*- coding: latin-1 -*-

import sys

def tfreducer():
  prefixo_atual = None
  contador_atual = None

  for line in sys.stdin:
    word,arquivo,contador  = line.strip().split('\t')
    prefixo = '%s\t%s' % (word,arquivo)

    if prefixo_atual == None:
      prefixo_atual = prefixo
      contador_atual = eval(contador)
    elif prefixo_atual == prefixo:
      contador_atual += eval(contador)
    else:
      print "%s\t%s" % (prefixo_atual,contador_atual)
      prefixo_atual = prefixo
      contador_atual = eval(contador)

  print "%s\t%s" % (prefixo_atual,contador_atual)

if __name__=='__main__':
  tfreducer()

# para a avaliação, não precisa alterar este código, execute-o como está