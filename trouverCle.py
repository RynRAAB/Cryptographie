def isAlphabet (c:chr) -> bool :
    if 65 <= ord(c) <= 90  or  97 <= ord(c) <= 122 :
        return True
    else:
        return False

def occCarDansUneChaine (chaine:str , c:chr) -> int :
    if (isAlphabet(c)):
        occ:int = 0
        for i in range (0 , len(chaine)) :
            if chaine[i] == c :
                occ += 1
    else:
        occ=0
    return occ

def carPlusPresent (chaine:str) -> chr :
    indiceCPP:int = 0
    maxPresence:int = occCarDansUneChaine(chaine,chaine[0])
    for i in range (1,len(chaine)) :
        if occCarDansUneChaine(chaine,chaine[i]) > maxPresence :
            maxPresence = occCarDansUneChaine(chaine,chaine[i])
            indiceCPP = i
    return chaine [indiceCPP]

def trouveCle (chaine:str) -> int :
    cpp:chr = carPlusPresent (chaine)
    cle:int
    if 65 <= ord(cpp) <= 90 :
        cle = (ord(cpp) - ord('E')) %26
    else:
        cle = (ord(cpp) - ord('e')) %26
    return cle

def trouveCleFichier (nomFichier:str) -> int :
    fic=open(nomFichier,"r")
    contenu:str = fic.read()
    cle:int = trouveCle(contenu)
    fic.close()
    return cle

