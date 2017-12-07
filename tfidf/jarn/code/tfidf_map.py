#!/usr/bin/env python
# -*- coding: latin-1 -*-
import sys

for line in sys.stdin:
    line = line.strip()
    splits = line.split("\t")
    doc_id, tpd, D, termo, f, tD = ("_", "_","_", "_", "_","_")

    # doc_id        tpd     D
    # doc1.txt      8181    6
    # doc2.txt      4710    6
    # ...
    if len(splits) == 3:
        doc_id = splits[0]
        tpd = splits[1]
        D = splits[2]

    # termo     doc_id      f       tD      
    # carta     doc6.txt    4       4
    # carta     doc1.txt    5       4
    # carta     doc5.txt    17      4
    # ...
    else:
        termo = splits[0]
        doc_id = splits[1]
        f = splits[2]
        tD = splits[3]

    print '%s\t%s\t%s\t%s\t%s\t%s' % (doc_id,tpd,D,termo,f,tD)
    # doc1.txt  8181     6     -1         -1    -1
    # doc1.txt    -1    -1     carta       4     4
    # doc1.txt    -1    -1     casa       12     3
    # doc1.txt    -1    -1     catavento   3     5
    # ...
