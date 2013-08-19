#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections


counter = collections.Counter(input())
print("%d %d %d %d" % tuple(map(counter.get, "ACGT")))
