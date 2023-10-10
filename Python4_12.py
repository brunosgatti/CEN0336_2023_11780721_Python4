#!/usr/bin/env python3

dna_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

dnax = []

for dna in dna_list:
    dnax.append(len(dna)), dnax.append(dna)

#dna_tuple = [tuple(dnalen) for dnalen in dnalen_list]
print(dnax)
#dna_tuple


#lenghts = [len(dna) for dna in dnas]
#
#lenghts_iterator = iter(lenghts)
#dnas_iterator = iter(dnas)
#for x in dnas:
  # dnas = (next(lenghts_iterator), next(dnas_iterator), sep = '\t')
  # print(next(lenghts_iterator), next(dnas_iterator), sep ='\t')
  # print(dnas)
