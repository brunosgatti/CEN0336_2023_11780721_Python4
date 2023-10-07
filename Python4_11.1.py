#!/usr/bin/env python3

dnas = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']


lenghts = [len(dna) for dna in dnas]

lenghts_iterator = iter(lenghts)
dnas_iterator = iter(dnas)
for x in dnas:
   print(next(lenghts_iterator), next(dnas_iterator), sep ='\t')

