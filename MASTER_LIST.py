# 1
n=int(input(" entrer l'intervalle : "))
tab = []
for i in range(n+1):
    if i % 2 == 0:
        tab.append(i)
print(tab)

#2
liste_entier=[1,2,3,4,5]
liste_chenn=[str(nombre) for nombre in liste_entier]
print(liste_chenn)

#3
list_minus=['un','deux','trois','quatre']
list_maj=[maj.upper() for maj in list_minus]
print(list_maj)

#4
liste_nombres = [10, 20, 30, 40, 50, 60, 70, 80, 90]
liste_3=[]
for i in range(len(liste_nombres)):
    if i % 3 == 0:
        liste_3.append(liste_nombres[i])
print(liste_3)


