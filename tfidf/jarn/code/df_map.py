#!/usr/bin/env python
# -*- coding: latin-1 -*-

import sys
import os

def dfmapper():
  for line in sys.stdin:
    print "%s\t1" % line.strip()

if __name__ == '__main__':
  dfmapper()


# para a avaliação, não precisa alterar este código, execute-o como está