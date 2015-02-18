#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
with open(sys.argv[1]) as f, open('pfsense-iso.3.6.1.2.1.31.1.1.1.10.3', 'w') as out:
     for line in f:
         out.write(line.split()[-1]+'\n')
