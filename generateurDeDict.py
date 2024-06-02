from random import randint

def initDict (d:dict[int,int]) :
    for i in range (1,27) :
        d[i] = 0

def dejaPris (d:dict[int,int] , element:int) -> bool :
    for  v in d.values():
        if  v==element:
            return True
    return False

def genereDictChiffres () -> dict[int,int] :
    d:dict[int,int] = dict()
    initDict(d)
    for i in range (1,27) :
        val:int = 0
        while dejaPris(d,val) : 
            val = randint(1,26)
        d[i] = val
    return d

def genereDict() -> dict[chr,chr] :
    dch:dict[int,int] = genereDictChiffres()
    d:dict[chr,chr] = dict()
    for k,v in dch.items() :
        d[chr(k+64)] = chr(v+64)
    for k,v in dch.items() :
        d[chr(k+96)] = chr(v+96)
    return d

def dictEnFichier (d:dict[chr,chr]):
    fic = open  ("dictionnaire.txt","w")
    for k,v in d.items () :
        ligne:str = k+" => "+v+'\n'
        fic.write(ligne)
    fic.close()

def fichierEnDict (nomFichier:str) -> dict[chr,chr] :
    fic = open (nomFichier , 'r')
    d:dict[chr,chr]=dict()
    ligne:str = " "
    while ligne != "" :
        ligne = fic.readline()
        if ligne != "":
            d[ligne[0]] = ligne[len(ligne)-2]
    fic.close()
    return d

def afficheDict (d:dict): 
    for k,v in d.items() :
        print(k,"->",v)
