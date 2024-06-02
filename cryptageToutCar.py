from random import randint
from generateurDeDict import *
from cryptageParDict import cryptage
from decryptageParDict import *

# en ce qui concerne le cryptage de César des 128 caracteres de la table ASCII
def cryptCarAscii (c:chr, cle:int) -> chr :
    nvlCle:int = (cle+ ord(c)) % 128
    if nvlCle==0 :
        nvlCle=128
    return chr(nvlCle)

def cryptChaineAscii (chaine:str, cle:int) -> str:
    nvlChaine:str = str()
    for i in range (0, len(chaine)) :
        nvlChaine += cryptCarAscii (chaine[i], cle)
    return nvlChaine

def decryptChaineAscii (chaine:str, cle:int) -> str:
    cle =  (-1)*int(cle)
    return cryptChaineAscii (chaine, cle)

def cryptFichierAscii (fichier:str ,cle:int) :
    fic = open(fichier, 'r')
    cryptFic = open ("crypt", 'w')
    content:str = fic.read()
    content= cryptChaineAscii (content, cle)
    cryptFic.write(content)
    fic.close()
    cryptFic.close()

def decryptFichierAscii (fichier:str , cle:int):
    fic = open(fichier, 'r')
    decryptFic = open ("decrypt", 'w')
    content:str = fic.read()
    content= decryptChaineAscii (content, cle)
    decryptFic.write(content)
    fic.close()
    decryptFic.close()

# en ce qui concerne le cryptage en dictionnaire des 128 caracteres de la table ASCII


def initDict (d:dict[int,int]) :
    for i in range (1,129) :
        d[i] = 0

def dejaPris (d:dict[int,int] , element:int) -> bool :
    for  v in d.values():
        if  v==element:
            return True
    return False

def genereDictChiffresAscii () -> dict[int,int] :
    d:dict[int,int] = dict()
    initDict(d)
    for i in range (1,129) :
        val:int = 0
        while dejaPris(d,val) : 
            val = randint(1,128)
        d[i] = val
    return d

def genereDictAscii() -> dict[chr,chr] :
    dch:dict[int,int] = genereDictChiffresAscii()
    d:dict[chr,chr] = dict()
    for k,v in dch.items() :
        d[chr(k)] = chr(v)
    return d

def cryptageFichierAscii (nomFichier) : # on commence d'abord par generer un dictionnaire pour le cryptage
    d:dict[chr,chr] = genereDictAscii()
    dictEnFichier(d) #on renvoie ainsi le dictionnaire utilisé pour le cryptage sous forme d'un fichier pour pouvoir le decrypté plus tard
    cryptage ("dictionnaire.txt",nomFichier) 




# en ce qui concerne le decryptage en dictionnaire a 128 caracteres

def decryptCarAscii (d:dict[chr,chr] , c:chr) -> chr :
    decryptC:chr
    decryptC = chercheAntecedent (d,c)
    return decryptC

def decryptChaineAscii (d:dict[chr,chr],chaine:str) ->str :
    decryptCh:str = str()
    for i in range (0, len(chaine)) : 
        decryptCh += str(decryptCarAscii (d,chaine[i]))
    return decryptCh

def decryptFichierAscii (nomDictionnaire:str, nomFichier:str) :
    d:dict[chr,chr] = fichierEnDict (nomDictionnaire)
    fic = open (nomFichier , 'r')
    decryptFic = open ("decrypt" ,'w')
    contenu:str = fic.read()
    contenu = decryptChaineAscii (d,contenu)
    fic.close()
    decryptFic.write (contenu)
    decryptFic.close()