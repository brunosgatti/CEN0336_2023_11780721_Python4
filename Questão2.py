#!/usr/bin/env python3

#Write a script that splits a string into a list. In your script:

#Save the string "sapiens, erectus, neanderthalensis" as a variable named taxa
taxa = 'sapiens, erectus, neanderthalensis'

#Print taxa
print(taxa)

#Print taxa[1]. What do you get?
print('\nPrinting taxa[1], we get:', taxa[1])

#Print type[taxa]. What is its type?
print('\nIts type is', type(taxa))

#Split taxa into individual words and print the result of the split.
print('\n', taxa.split(','))

#Store the result of split in a new variable named species
species = taxa.split(',')

#Print species
print('\n', species)

#Print the species[1]. What do you get?
print('\nPrinting species[1], we get:', species[1])

#Print type(species). What is its type?
print('\nIts type is', type(species))

#Sort the list alphabetically and print.
print(sorted(species, key=None, reverse=False))

#Sort the list by length of each string and print (the shortest string should be first).
print(sorted(species, key=len))

