from cryptageDeCesar import *
from trouverCle import *
from cryptageParDict import *
from decryptageParDict import *
from cryptageToutCar import *

def choisir() -> int :
    choix:int=0
    print ("Choisir une option (en  respectant le chiffrement suivant): ")
    print ("  1 -> Caractères alphabetiques")
    print ("  2 -> 128 Caractères de la table ASCII")
    while choix!=1 and choix!=2 :
        choix = int(input ("Entrez un chiffre valide : "))
    return choix

def choisirOption1() -> int :
    choix:int = 0
    print ("Choisir une option (en  respectant le chiffrement suivant): ")
    print ("  1 -> CRYPTAGE")
    print ("  2 -> DECRYPTAGE")
    print ("  3 -> TROUVER LA CLE D'UN CRYPTAGE DE CÉSAR")
    while choix<1 or choix>3 :
        choix = int(input ("Entrez un chiffre valide : "))
    return choix

def choisirOption2() -> int :
    choix:int = 0
    print ("Choisir une option (en  respectant le chiffrement suivant): ")
    print ("  1 -> MÉTHODE DE CÉSAR")
    print ("  2 -> MÉTHODE DU DICTIONNAIRE ALÉATOIRE")
    while choix<1 or choix>2 :
        choix = int(input ("Entrez un chiffre valide : "))
    return choix

def cryptageCesar (choix:int) :
    fichier:str = input ("Saisir le nom du fichier à crypter : ")
    cle:int = int (input ("Saisir la cle du cryptage : "))
    print ("RQ: ce programme va creer un fichier crypt contenant le cryptage demandé, pensez à le récuperer avant la prochaine execution !")
    if choix==1:
        cryptFichierCesar (fichier,cle)
    else:
        cryptFichierAscii(fichier,cle)

def decryptageCesar(choix:int) :
    fichier:str = input ("Saisir le nom du fichier à decrypter : ")
    cle:int = int(input ("Saisir la cle du decryptage : "))
    print ("RQ: ce programme va creer un fichier decrypt contenant le decryptage demandé, pensez à le récuperer avant la prochaine execution !")
    if choix==1:
        decryptFichierCesar (fichier,cle)
    else:
        decryptFichierAscii(fichier,cle)

def cryptageDict (choix:int) :
    fichier:str = input ("Saisir le nom du fichier à crypter : ")
    print ("RQ: ce programme genere un dictionnaire aleatoire sous forme d'un fichier (dictionnaire.txt) muni du fichier crypté (crypt), pensez à les récuperer avant la prochaine execution !")
    if choix==1:
        cryptageFichier(fichier)
    else:
        cryptageFichierAscii(fichier)

def decryptageDict (choix:int) :
    fichier:str = input ("Saisir le nom du fichier à decrypter : ")
    dict:str = input ("Saisir le nom du dictionnaire à utiliser pour ce decryptage : ")
    print ("RQ: ce programme crée un fichier (decrypt) contenant le decryptage voulu, pensez à le récuperer avant la prochaine execution !")
    if choix==1:
        decryptFichier (dict,fichier)
    else:
        decryptFichierAscii(dict,fichier)

def CleCesar (choix:int) :
    if choix==1:
        fichier: str = input ("Saisir le nom du fichier : ")
        cle:int = trouveCleFichier(fichier)
        print ("La clé de ce cryptage est :",cle)
        print( "RQ: ce programme crée un fichier (decrypt) contenant le decryptage du fichier entré, pensez à le récuperer avant la prochaine execution !")
        decryptFichierCesar (fichier,cle)
    else:
        print ("Clé introuvable dans ce cas.")

def execution() :
    print ("***************************************************************************************************************")
    print ("************************************************ - BIENVENUE - ************************************************")
    print ("***************************************************************************************************************")
    choix:int=choisir()
    print ("***************************************************************************************************************")
    choix1:int = choisirOption1()
    print ("***************************************************************************************************************")
    choix2:int = choisirOption2()
    print ("***************************************************************************************************************")
    if choix1==1 and choix2==1:
        cryptageCesar(choix)
    elif choix1==1 and choix2==2:
        cryptageDict(choix)
    elif choix1==2 and choix2==1:
        decryptageCesar(choix)
    elif choix1==2 and choix2==2:
        decryptageDict(choix)
    else:
        CleCesar(choix)    
    print ("***************************************************************************************************************")
    print ("*************************************************** - FIN - ***************************************************")
    print ("***************************************************************************************************************")
    
execution()