#!/usr/bin/env python3

dna_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']


lenghts = [len(dna) for dna in dna_list]

lenghts_iterator = iter(lenghts)
dnas_iterator = iter(dna_list)

for dna in dna_list:
   print(dna_list.index(dna), next(lenghts_iterator), next(dnas_iterator), sep ='\t')
