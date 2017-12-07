#!/usr/bin/env python
# -*- coding: latin-1 -*-
import sys
import os
import string

def ntdocmapper():
  for line in sys.stdin:
    words = line.strip().split()
    for word in words:
	word_f = filter(str.isalpha, word)
        if len(word_f) >= 2:
      		print "%s\t1" % (os.getenv('mapreduce_map_input_file','???'))
          
if __name__ == '__main__':
  ntdocmapper()
