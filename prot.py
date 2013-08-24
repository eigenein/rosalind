#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools


rna_codon_table_tokens_iterator = iter("""
    UUU F      CUU L      AUU I      GUU V
    UUC F      CUC L      AUC I      GUC V
    UUA L      CUA L      AUA I      GUA V
    UUG L      CUG L      AUG M      GUG V
    UCU S      CCU P      ACU T      GCU A
    UCC S      CCC P      ACC T      GCC A
    UCA S      CCA P      ACA T      GCA A
    UCG S      CCG P      ACG T      GCG A
    UAU Y      CAU H      AAU N      GAU D
    UAC Y      CAC H      AAC N      GAC D
    UAA Stop   CAA Q      AAA K      GAA E
    UAG Stop   CAG Q      AAG K      GAG E
    UGU C      CGU R      AGU S      GGU G
    UGC C      CGC R      AGC S      GGC G
    UGA Stop   CGA R      AGA R      GGA G
    UGG W      CGG R      AGG R      GGG G
""".split())

rna_codon_table = dict()
while True:
    try:
        codon = next(rna_codon_table_tokens_iterator)
    except StopIteration:
        break
    amino = next(rna_codon_table_tokens_iterator)
    rna_codon_table[codon] = amino

rna_string = input()

for codon_start_index in range(0, len(rna_string), 3):
    codon = rna_string[codon_start_index:codon_start_index + 3]
    amino = rna_codon_table[codon]
    if amino != "Stop":
        print(amino, end="")
print()
