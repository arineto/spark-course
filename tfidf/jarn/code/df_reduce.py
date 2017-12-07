#!/usr/bin/env python
# -*- coding: latin-1 -*-
import sys

def dfreducer():
  word_atual = None
  contador_atual = None
  space = []

  for line in sys.stdin:
    word,arquivo,freq,contador = line.strip().split()
    prefixo = "%s\t%s\t%s" %(word,arquivo,freq)

    if word == None:
      word_atual = word
      contador_atual = eval(contador)
      space.append(prefixo)
    elif word_atual == word:
      contador_atual += eval(contador)
      space.append(prefixo)
    else:
      for item in space:
        print "%s\t%d" % (item,contador_atual)

      word_atual = word
      contador_atual = eval(contador)
      space = [prefixo]

  for item in space:
    print "%s\t%d" % (item,contador_atual)

if __name__=='__main__':
  dfreducer()

# para a avaliação, não precisa alterar este código, execute-o como está