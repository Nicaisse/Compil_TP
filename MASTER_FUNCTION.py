import string
import random
import re
#1 kreye yon fonksyon ki ap pran yon paramèt yon mo, epi li retounen envès la.
def mot_correct(mot):
    mot_inv=mot[::-1]
    return mot_inv
motAFFICH=mot_correct('lala')
# print(motAFFICH)

#2 kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik.
def generer(n):
    lettres=string.ascii_letters
    chaine_random = ''.join(random.choice(lettres) for i in range(n))
    print(chaine_random)
# generer(5)

#3 kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik, san repetisyon.
def genere_nodoub(n):
    lettres= string.ascii_letters
    chainenodoub=set()
    while len(chainenodoub)<n:
        c=random.choice(lettres)
        chainenodoub.add(c)
    # chaine=''.join(chainenodoub)
    chaine=''.join(chainenodoub)
    print(chaine)
genere_nodoub(5)

#4 kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alafanimerik, san repetisyon.
def alfa_numeric(n):
    alfa_nim=string.ascii_letters+string.digits
    print(alfa_nim)
    alfa=set()
    abd=False
    while len(alfa)<n and abd==False:
        alfa1=set()
        ran=random.choice(alfa_nim)
        alfa.add(ran)
    chaine=''.join(alfa)
    for caract in chaine:
        if caract.isdigit():
            abd=True
    print(chaine)
alfa_numeric(5)

#5 Ou gen yon lis chenn. Jenere yon SLUG apati chenn nan. Nan yon SLUG,
#       tout karaktè ki akseptab yo se: alfanimerik ak "-"
def jenere_slug(chenn):
    chenn_no_alfanimerik = re.sub(r'[^a-zA-Z0-9-]', '-', chenn)
    slug_finale = re.sub(r'-+', '-', chenn_no_alfanimerik)
    return slug_finale.lower()

chenn = "Sa a se yon tèks#ekzanp!123"
slug = jenere_slug(chenn)
print(slug) 

#6 Kreye yon fonksyon ki ap separe chak lèt nan yon mo ak yon vigil
def splitmot():
    mot="AYITI"
    mot2=[]
    for i in mot:
        mot2.append(i+',')
    mot3=''.join(mot2)
    print(mot3)
splitmot()

#7 Kreye yon fonksyon ki ap kripte yon mo, avèk endèks li nan alfabè a. Chak karaktè dwe separe ak yon tirè.
def criptage(mot):
    alfabet=string.ascii_letters
    tab=[]
    for i,caractere in enumerate(mot):
        carac=caractere
        for j,element2 in enumerate(alfabet):
            if carac==element2:
                index=str(j+1)
        tab.append(index)
    chaine="-".join(tab)
    print(chaine)
mot="alo"
criptage(mot)

#8 Kreye yon fonksyon ki ap dekripte yon mo ki fèt ak endèks chak lèt nan alfabè a, separe ak yon tirè.
def decryptage(chaine):
    alfabet=string.ascii_letters
    tab=[]
    chaine_split=chaine.split("-")
    for element in chaine_split:
        num=int(element)
        for j,element2 in enumerate(alfabet):
            if num==(j+1):
                bgy=element2
        tab.append(bgy)
    mot=''.join(tab)
    print(mot)
chaine="1-12-15"
decryptage(chaine)


#9 Kreye yon fonksyon ki ap pran 2 paramèt, epi ki pèmite valè yo. Answit li retounen tou 2 valè yo sou fòm Tuple.
def pemitasyon(val1,val2):
    temp=val1
    val1=val2
    val2=temp
    tipl=(val1,val2)
    print (tipl)

pemitasyon(2,4)

#10
def inisyal(nom):
    while not isinstance(nom,str):
        nom=input('entre un nom sans aucun element numeric')
    inis=re.split(r'[-\s]',nom)
    inisyal_maj=''.join(element[0].upper() for element in inis)
    print (inisyal_maj)
inisyal('Jean-batis ja')
