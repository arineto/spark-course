#!/usr/bin/env python  
# -*- coding: latin-1 -*-
import sys
import math

tf, idf, tfidf, tpd_atual, D_atual = (0,0,0,0,0)


for line in sys.stdin:
    line = line.strip()
    doc_id,tpd,D,termo,f,tD = line.split("\t")

    # linha de controle: split[3] { termo } = "_"        
    if termo == "_": # controle
        tpd_atual = float(eval(tpd))
        D_atual = float(eval(D))
    else: # dados
        f = float(eval(f))
        tD = float(eval(tD))
        tf = f/tpd_atual
        idf = math.log((D_atual + 1) / (tD + 1), 10)
        tfidf = tf * idf
        print "%s\t%f\t%s" % (termo, tfidf, doc_id)
