#1 
chaine="AYIBOBO HAITI"
minuscule=chaine.lower()
print(minuscule)

#2
split=chaine.split(' ')
print(split)


#3
texte = "voici une chaine de caractères a mettre en majuscule."
nouveau_texte=texte.title()
print(nouveau_texte)

#4
chaine=texte.split()
tab=[mot[0] for mot in chaine]
nouvomot=''.join(tab)
print(nouvomot)

#5
phrase_modifier=texte.replace('a','@')
print(phrase_modifier)

#6
mot1="ayiti"
mot2=mot1[::-1].upper()
print(mot2)


#7
chenn="Ayiti kapab avanse"
index=None
for i,caractere in enumerate(chenn):
    if caractere=="a":
        index=i
        print(index)
        break
if index is None:
    print("il n'y a pas de 'a' dans cette phrase")


#8
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


#9
chenn="Ayiti kapab avanse"
tab_index=[]
for i,caractere in enumerate(chenn):
    if caractere=="a":
        tab_index.append(i)

print(tab_index)

#10
chenn="Ayiti kapab avanse"
chenn_modif=chenn.replace(' ','')
total_index=len(chenn_modif)
result=chenn_modif + str(total_index)
print(result)
