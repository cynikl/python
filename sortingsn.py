#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2015-09-20 Cyril Niklaus v 1.0
# 2017-04-20 Cyril Niklaus v 1.1
# line 39 modified 2017-04-20, by Wade Robson, on slack macadmins
import argparse

Help_Message = """
-------------------------------------------------------------------------'
Cyril Niklaus (cyril.niklaus@artcomputer.ch) 2017-04-20

Ce programme aide à la correction de la saisie des numéros de série
pour le DEP. Il va enlever le S qui préfixe les numéros scannés et aussi
vérifier et éliminer si nécessaire les doublons.

Utilisation:
Il suffit de fournir le nom du fichier csv contenant les numéros de série
ainsi que le nom du fichier où l\'on souhaite enregistrer les numéros corrigés.
Par défaut le programme va les enregistrer dans le dossier où il se trouve.
-------------------------------------------------------------------------
"""
parser = argparse.ArgumentParser(description=Help_Message, formatter_class=argparse.RawTextHelpFormatter)
args = parser.parse_args()

wordlist = list()
try:
    fname = raw_input("Saissisez le nom du fichier CSV à traiter: ")
    fhand = open(fname)
except:
    print 'Ce fichier n\'existe pas. Vérifiez le nom et recommencez. \nPour l\'aide, lancez le programme avec -h:\npython sortingsn.py -h'
    quit()

outputfilename = raw_input("Saissisez le nom du fichier à sauvegarder: ") +".txt"

for line in fhand:
    line = line.rstrip()
    if line == '' : continue
    # split is for strings
    wordlist.append(line.split()[0])

new_text = "\n".join(line[1:] for line in wordlist)

snlist = new_text.split()#list splist into letters, split into words
#snlist.sort()# removed as the set does not respect order :)

# now to remove duplicates
uniquesnset = set(snlist)
#make it into a list again
uniquesnlist = list(uniquesnset)
uniquesnlist.sort()

#to write the list to file
with open(outputfilename, 'w+') as snlistfile:
    for item in uniquesnlist:
    #snlist.txt.write("%s\n" % item)
        print>>snlistfile, item

