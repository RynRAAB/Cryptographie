from trouverCle import *

def cryptCar (c:chr , cle:int) -> chr :
    chiffreAscii:int 
    if isAlphabet(c) :
        chiffreAscii = ord(c) + cle 
        if 97 <= ord(c) <= 122 : 
            chiffreAscii = (chiffreAscii-97) %26 +97 
        else:
            chiffreAscii = (chiffreAscii-65) %26 +65
    else:
        chiffreAscii = ord(c)
    return chr (chiffreAscii)

def cryptChaine (chaine:str , cle:int) -> str :
    chaineCrypte:str = str()
    for i in range (0 , len(chaine)) :
        chaineCrypte += cryptCar(chaine[i],cle)
    return chaineCrypte

def decryptChaine (chaine:str , cle:int) -> str :
    return cryptChaine (chaine,(-1)*cle)

def cryptFichierCesar (nomFichier:str , cle:int) :
    fic = open (nomFichier,'r')
    cryptFic = open ("crypt" , 'w')
    contenu:str = fic.read()
    cryptFic.write(cryptChaine(contenu,cle))
    fic.close()
    cryptFic.close()

def decryptFichierCesar (nomFichier:str , cle:int):
    fic = open (nomFichier,'r')
    decryptFic = open ("decrypt" , 'w')
    contenu:str = fic.read()
    decryptFic.write(decryptChaine(contenu,cle))
    fic.close()
    decryptFic.close()