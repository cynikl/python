#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2015-09-20 Cyril Niklaus v 1.0
# 2017-04-20 Cyril Niklaus v 1.1
# line 39 modified 2017-04-20, by Wade Robson, on slack macadmins
import argparse

HELP_MESSAGE = """
-------------------------------------------------------------------------'
Cyril Niklaus (cyril.niklaus@company.com)

Ce programme aide à la correction de la saisie des numéros de série
pour le DEP. Il va enlever le S qui préfixe les numéros scannés et aussi
vérifier et éliminer si nécessaire les doublons.

Utilisation:
Il suffit de fournir le nom du fichier csv contenant les numéros de série
ainsi que le nom du fichier où l\'on souhaite enregistrer les numéros corrigés.
Par défaut le programme va les enregistrer dans le dossier où il se trouve.
-------------------------------------------------------------------------
"""
PARSER = argparse.ArgumentParser(description=HELP_MESSAGE, formatter_class=argparse.RawTextHelpFormatter)
ARGS = PARSER.parse_args()

WORDLIST = list()

try:
    FNAME = raw_input("Saissisez le nom du fichier CSV à traiter: ")
    FHAND = open(FNAME, 'rU')
except:
    print(
        'Ce fichier n\'existe pas. Vérifiez le nom et recommencez.'
        '\nPour l\'aide, lancez le programme avec -h:\npython sortingsn.py -h'
        )
    quit()

OUTPUTFILENAME = raw_input("Saissisez le nom du fichier à sauvegarder: ") +".txt"

for line in FHAND:
    line = line.rstrip('\r\n')
    #line = line.rstrip()
    if line == '':
        continue
    # split is for strings
    WORDLIST.append(line.split()[0])

NEW_TEXT = "\n".join(line[1:] for line in WORDLIST)

SNLIST = NEW_TEXT.split()#list splist into letters, split into words
#SNLIST.sort()# removed as the set does not respect order :)

# now to remove duplicates
UNIQUESNSET = set(SNLIST)
#make it into a list again
UNIQUESNLIST = list(UNIQUESNSET)
UNIQUESNLIST.sort()

#to write the list to file
with open(OUTPUTFILENAME, 'w+') as snlistfile:
    for item in UNIQUESNLIST:
    #snlist.txt.write("%s\n" % item)
        print>>snlistfile, item
