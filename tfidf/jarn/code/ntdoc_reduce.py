#!/usr/bin/env python
# -*- coding: latin-1 -*-
import sys

files_list = []
D = 0 # tamanho do corpus

def ntdocreducer():
  curFileName = None
  curcount = None

  for line in sys.stdin:
	filename, count = line.strip().split("\t")

	if (curFileName == None):
		curcount = eval(count)
		curFileName = filename
	elif (curFileName == filename):
		curcount += eval(count)
	else:
		#print "%s\t%s" % (curFileName, curcount)
		files_list.append((curFileName, curcount))
		curcount = eval(count)		
		curFileName = filename

  # imprime a ultima chave encontrada
  # print "%s\t%s" % (curFileName, curcount)		
  files_list.append((curFileName, curcount))

  D = len(files_list)
  for values in files_list:
	# nome_do_arquivo	total_termos	tam_corpus
	print "%s\t%s\t%s" % (values[0], values[1], D)		

if __name__=='__main__':
  ntdocreducer()

# para a avaliação, não precisa alterar este código, execute-o como está