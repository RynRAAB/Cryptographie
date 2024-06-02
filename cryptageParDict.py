from generateurDeDict import *
from trouverCle import isAlphabet 

#Dans tous les sous programmes il faut recuperer le fichier crypté ainsi que le dictionnaire juste apres l'execution , car apres chaque execution y a un nouveau dictionnaire qui se genere automatiquement

def cryptCar (d:dict[chr,chr] , c:chr) -> chr :
    cryptC:chr
    if isAlphabet(c) : 
        cryptC = d[c]
    else:
        cryptC = c
    return cryptC

def cryptChaine (d:dict[chr,chr] , chaine:str) -> str :
    cryptCh:str=str()
    for i in range (0 , len(chaine)) :
        cryptCh += cryptCar (d,chaine[i])
    return cryptCh

def cryptage (nomDictionnaire:str , nomFichier:str) : # ca va renvoyer un fichier crypté en utilisant un dictionnaire en entrée en argument sous forme de fichier
    d:dict[chr,chr] = fichierEnDict (nomDictionnaire)
    fic = open (nomFichier, 'r')
    cryptFic = open ("crypt" , 'w')
    contenu:str = fic.read()
    cryptFic.write(cryptChaine(d,contenu))
    fic.close()
    cryptFic.close()

def cryptageFichier (nomFichier) :
    # on commence d'abord par generer un dictionnaire pour le cryptage
    d:dict[chr,chr] = genereDict()
    dictEnFichier(d) #on renvoie ainsi le dictionnaire utilisé pour le cryptage sous forme d'un fichier pour pouvoir le decrypté plus tard
    cryptage ("dictionnaire.txt",nomFichier) 
