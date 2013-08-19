#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import itertools
import operator
import sys


lines = filter(operator.truth, sys.stdin)
lines = map(str.strip, lines)

grouped_lines = list()

current_id = None
for line in lines:
    if line[:1] == ">":
        current_id = line[1:]
    else:
        grouped_lines.append((current_id, line))

dna_strings = dict()
for id, line in grouped_lines:
    if id in dna_strings:
        dna_strings[id] += line
    else:
        dna_strings[id] = line


def gc_percentage(item):
    id, dna_string = item
    return id, 100.0 * len(list(bp for bp in dna_string if bp in "GC")) / len(dna_string)


dna_strings = dict(map(gc_percentage, dna_strings.items()))
print("%s\n%s" % max(dna_strings.items(), key=operator.itemgetter(1)))
