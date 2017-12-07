#!/usr/bin/env python
# -*- coding: latin-1 -*-
import sys

for line in sys.stdin:
	line = line.strip()
	termo,tfidf,doc_id = line.split("\t")
        
	print '%s\t%s\t%s' % (termo,tfidf,doc_id)

# para a avaliação, não precisa alterar este código, execute-o como está