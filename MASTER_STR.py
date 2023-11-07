#1 Nan yon chenn karaktè, mete tout karaktè yo an miniskil.
chaine="AYIBOBO HAITI"
minuscule=chaine.lower()
print(minuscule)

#2 Nan yon chenn karaktè, koupe chenn nan tout kote 
#   ki gen espas. Epi afiche yon lis ki gen chak eleman yo
split=chaine.split(' ')
print(split)


#3 Nan yon chenn karaktè, mete tout premye lèt chak mo an majiskil.
texte = "voici une chaine de caractères a mettre en majuscule."
nouveau_texte=texte.title()
print(nouveau_texte)

#4Nan yon chenn karaktè, rekipere premye lèt chak mo.Epi afiche yon nouvo chenn ak tout inisyal sa yo.
chaine=texte.split()
tab=[mot[0] for mot in chaine]
nouvomot=''.join(tab)
print(nouvomot)

#5 Ranplase tout karaktè "a" ki nan yon chenn pa "@"
phrase_modifier=texte.replace('a','@')
print(phrase_modifier)

#6Mete yon chenn karaktè devan dèyè, answit mete l an majiskil.
mot1="ayiti"
mot2=mot1[::-1].upper()
print(mot2)


#7Afiche endeks premye karaktè "a" ki nan yon chenn.
chenn="Ayiti kapab avanse"
index=None
for i,caractere in enumerate(chenn):
    if caractere=="a":
        index=i
        print(index)
        break
if index is None:
    print("il n'y a pas de 'a' dans cette phrase")


#8Afiche total tout endeks karaktè "a" ki nan yon chenn (Kit se a majiskil oubyen miniskil).
chenn="Ayiti kapab avanse"
index=None
som=0
for i,caractere in enumerate(chenn):
    if caractere=="a" or caractere=="A":
        index=i
        som+=i
if index is None:
    print("il n'y a pas de 'a' dans cette phrase")
else:
    print(f"la somme de tout les index de 'a' est egale {som}")


#9 Kreye yon lis ki gen endeks tout karaktè "a" ki nan yon chenn (Sèlman a miniskil). Ekzanp:
chenn="Ayiti kapab avanse"
tab_index=[]
for i,caractere in enumerate(chenn):
    if caractere=="a":
        tab_index.append(i)

print(tab_index)

#10 Retire tout espas ki nan yon chenn, epi kole chenn sa ak kantite karaktè li genyen (Pa kontwole espas yo).
chenn="Ayiti kapab avanse"
chenn_modif=chenn.replace(' ','')
total_index=len(chenn_modif)
result=chenn_modif + str(total_index)
print(result)
