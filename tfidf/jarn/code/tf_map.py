#!/usr/bin/env python
# -*- coding: latin-1 -*-
import sys
import os
import string

def tfmapper():
  for line in sys.stdin:
    words = line.strip().split()
    for word in words:
	word_f = filter(str.isalpha, word)
        if len(word_f) >= 2:
      		print "%s\t%s\t1" % (word_f.lower(), os.getenv('mapreduce_map_input_file', 'noname'))

if __name__ == '__main__':
  tfmapper()
