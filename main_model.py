from os import linesep
from spellchecker import SpellChecker

spell = SpellChecker()

symbol=['.','!',',',':',';','"','(',')','-','--']
file = open(r".\spellchecker\Dataset\aspell.txt","r+")

while True:
    next_line = file.readline()

    if not next_line:
        break;

    line = ''.join(i for i in next_line if not i in symbol)
    res =line.split()
    misspelled = spell.unknown(res)
    for word in misspelled:
        print("\nTHE INCORRECT WORD IS :- "+word)
    # Get the one `most likely` answer
        print("THE PORBABLE CORRECT WORD IS :-") 
        print(spell.correction(word))
        
    # Get a list of `likely` options
        print("THE OTHERS POSSIABLE WORD IS :- ")
        print(spell.candidates(word))
        print("\n")

