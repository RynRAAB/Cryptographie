from generateurDeDict import *
from trouverCle import isAlphabet 

def chercheAntecedent (d:dict[chr,chr], c:chr) -> chr :
    for k,v in d.items() : 
        if v==c :
            return k

def decryptCar (d:dict[chr,chr] , c:chr) -> chr :
    decryptC:chr
    if isAlphabet(c) :
        decryptC = chercheAntecedent (d,c)
    else:
        decryptC = c
    return decryptC

def decryptChaine (d:dict[chr,chr],chaine:str) ->str :
    decryptCh:str = str()
    for i in range (0, len(chaine)) : 
        decryptCh += decryptCar (d,chaine[i])
    return decryptCh

def decryptFichier (nomDictionnaire:str, nomFichier:str) :
    d:dict[chr,chr] = fichierEnDict (nomDictionnaire)
    fic = open (nomFichier , "r")
    decryptFic = open ("decrypt" ,"w")
    contenu:str = fic.read()
    contenu = decryptChaine (d,contenu)
    fic.close()
    decryptFic.write (contenu)
    decryptFic.close()

