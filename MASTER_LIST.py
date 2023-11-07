#1 Kreye yon lis eleman ki divizib pa 2, nan entèval [0-n] enklizif
n = int(input(" entrer l'intervalle : "))
tab = []
for i in range(n + 1):
    if i % 2 == 0:
        tab.append(i)
print(tab)

#2 Ou gen yon lis antye, konvèti l an yon lis chenn.
liste_entier = [1, 2, 3, 4, 5]
liste_chenn = [str(nombre) for nombre in liste_entier]
print(liste_chenn)

#3 Ou gen yon lis chenn ki an miniskil, konvèti an yon lis chenn majiskil
list_minus = ["un", "deux", "trois", "quatre"]
list_maj = [maj.upper() for maj in list_minus]
print(list_maj)

#4 Ou gen yon lis, kreye yon nouvo lis ki fèt ak eleman ki nan endèks ki divizib pa 3 yo sèlman
liste_nombres = [10, 20, 30, 40, 50, 60, 70, 80, 90]
liste_3 = []
for i in range(len(liste_nombres)):
    if i % 3 == 0:
        liste_3.append(liste_nombres[i])
print(liste_3)

#5 Ou gen lis eleman, kreye yon nouvo lis ki gen chak 3 eleman yo gwoupe anndan yon tipl. 
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
liste_tuples = []
for i in range(0, len(list1), 3):
    if i + 2 < len(list1):
        tuple = (list1[i], list1[i + 1], list1[i + 2])
        liste_tuples.append(tuple)
print(liste_tuples)

#6 Ou gen yon lis, ki gen yon pakèt eleman ki repete. Konvèti l an yon lis, ki pa gen okenn doublon.
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 5, 6, 7, 8]
list_noDoub = set(list2)
print(list_noDoub)

#7 Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman komen ant 2 lis yo.doublon.
list_A = [1, 2, 3, 4, 5, 6, 7, 8]
list_B = [1, 2, 3, 4]
list_c = [i for i in list_A if i in list_B]
print(list_c)

#8 Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman distenge ant 2 lis yo.
list_k = [element for element in list_A if element not in list_B]
print(list_k)

#9 Ou gen yon diksyonè. Kreye yon nouvo lis ak kle yo sèlman, epi yon lòt ak valè yo sèlman.
entreprises = {
    "non": "Jean",
    "sirname": "Baptiste",
    "age": 30,
    "vil": "Pòtoprens",
    "plis": [1, 2, 3],
    
}

liste_kle = []
list_value = []
for kle in entreprises.keys():
    liste_kle.append(kle)
for value in entreprises.values():
    list_value.append(value)

print(liste_kle)
print(list_value)

#10 Reyini 3 lis ansanm, san okenn doublon.
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [11, 12, 13, 14, 15, 1, 2, 4, 5]
list3 = [20, 22, 11, 4, 5]
list_temp = list1 + list2 + list3
tab_safe = set(list_temp)
print(tab_safe)
