#1 Ou gen yon diksyonè. Rekipere tout valè yo, gras ak kle yo epi retounen yon lis valè.
list_val=[]
dict1 = {
    "clé1": "valeur1",
    "clé2": "valeur2",
    "clé3": "valeur3"
}
for cle,valeur in dict1.items():
    val=dict1[cle]
    list_val.append(val)
print(list_val)


#2 Mande itilizatè a, tape yon valè... epi verifye si l gen akolad devan ak dèyè.
input_user=input('antre yon mot : ')
if input_user[0]=="{" and input_user[-1]=="}":
    print('li gen akolad ni devan ni deye')

#3 Pakouri yon diksyonè, epi afiche tout kle yo.
entreprises = {
    "non": "Jean",
    "sirname": "Baptiste",
    "age": 30,
    "vil": "Pòtoprens",
    "plis": [1, 2, 3],
    
}
for kle in entreprises:
    print(kle)

#4 Pakouri yon diksyonè, epi afiche tout valè yo.
for cle,kle in entreprises.items():
    print(f"{cle}:{kle}")

#5 Pakouri yon diksyonè, pou w kapab kreye yon kopi(nouvo) sou disksyonè sa.
dict_copy=entreprises.copy()
print(dict_copy)

#6 Anndan yon diksyonè ki gen kle ak valè(valè yo ka nenpòt tip done). 
#       Ajoute yon underscore devan ak dèyè tout valè ki se chenn yo
test = {"name": "Lub", "age": 14, "assets": ["laptop", "phone"]}
for cle,valeur in test.items():
    if isinstance(valeur,str):
        test[cle]="_"+valeur+"_"
print(test)

#7 Nan yon diksyonè ki gen valè ki se chenn sèlman.
#       Kreye yon nouvo diksyonè ki gen tout eleman ki gen valè ki dijit yo sèlman. Ekzanp:
dict_chenn={"a": "12", "b": "abc", "c": "12r", "d":"90"}
dic_digit={}
for cle, valeur in dict_chenn.items():
    if valeur.isdigit():
        dic_digit[cle]=valeur
print(dic_digit)

#8 Pakouri yon disksyonè, pou w mete l sou fòm lis, kote chak eleman nan disksyonè sa, 
#       vin sou fòm tipl(kle, valè) anndan lis la.
diction={"a":1, "b": 2}
liste_tipl=[]
for cle,valeur in diction.items():
    tuple=(cle,valeur)
    liste_tipl.append(tuple)
print(liste_tipl)

#9 Pakouri yon lis tipl, pou w mete l sou fòm diksyonè
liste_tipl=[("a",1), ("b",2)]
dict_tipl={}
for cle,info in liste_tipl:
    dict_tipl.update({
        cle:info
    })
print(dict_tipl)

#10
diksyone1 = {
    "non": "Jean",
    "sirname": "Baptiste",
    "age": 30,
    "vil": "Pòtoprens",
    "plis": [1, 2, 3],
    
}

diksyone2 = {
    "non": "Marie",
    "sirname": "Lorel",
    "age": 25,
    "vil": "Gonaïves",
    "plis": {4, 5, 6},
    
}
nouvo_diksyone = {}

for kle in set(diksyone1.keys()) | set(diksyone2.keys()):
    if kle in diksyone1 and kle in diksyone2:
        if isinstance(diksyone1[kle], int) and isinstance(diksyone2[kle], int):
            nouvo_diksyone[kle] = diksyone1[kle] + diksyone2[kle]
        else:
            nouvo_diksyone[kle] = str(diksyone1[kle]) + str(diksyone2[kle])
    elif kle in diksyone1:
        nouvo_diksyone[kle] = diksyone1[kle]
    elif kle in diksyone2:
        nouvo_diksyone[kle] = diksyone2[kle]

print(nouvo_diksyone)