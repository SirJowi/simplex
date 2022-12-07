import numpy as np

#Koeffizienten des Gleichungssystems
A = np.array([[ 1, 1, -1, 0,  0],
              [-1, 1,  0, 1,  0],
              [-2, 1,  0, 0, -1]])

#Ergebnisvektor des Gleichungssystems
b = [5, 5, 2]

#Koeffizienten der Zielfunktion
c = [2, 3, 0, 0, 0]

#Platzhalter fuer Hilfsgroesse q (Liste mit Nullen und der gleichen Zeilenanzahl von A)
q = [0]*len(A)

k = 1
#Abbruchkriterium: Das Ergebnis lässt sich verbessern, solange Koeffizienten der Zielfunktion > 0
while max(c) > 0:

    print("Iterationsschritt:", k, "--------------------------")
    k = k +1

    #PIVOTSPALTE: Finde Indize des groessten Koeffizienten in der Zielfunktion c
    piv_j = c.index(max(c))

    #Schleife über alle Zeilen von A
    for i in range(len(A)):
        #Quotientenberechnung für Hilfsgroesse q
        q[i] = b[i] / A[i, piv_j]

    #PIVOTZEILE: Finde Indize des kleinsten positiven Koeffizienten in q
    piv_i = q.index(min([i for i in q if i > 0]))

    #Aenderung der Koeffizienten von b
    #Schleife über alle Zeilen von b
    for i in range(len(A)):
        #Normierung der Zeile i vom Ergebnisvektor b
        if i == piv_i:
            b[i] = b[i] / A[piv_i, piv_j]
        #Berechnungen der übrigen Koeffizienten von b
        else:
            b[i] = b[i] - b[piv_i] * A[i, piv_j]
    print("Ergebnisvektor:")
    print(b)

    #Aenderung der Koeffizienten von A
    for s in range(len(A[0])):                      #über Spalte s (0 bis 4)
        for r in range(len(A)):                     #über Zeile  r (0 bis 2)
            if s == piv_j and r == piv_i:
                A[r, s] = 1 / A[piv_i, piv_j]
            if s != piv_j and r == piv_i:
                A[r, s] = A[r, s] / A[piv_i, piv_j]
            if s == piv_j and r != piv_i:
                A[r, s] = A[r, piv_j] - (A[r, piv_j] * A[piv_i, s]) / A[piv_i, piv_j]
            if s != piv_j and r != piv_i:
                A[r, s] = A[r, s] - (A[r, piv_j] * A[piv_i, s]) / A[piv_i, piv_j]
    print("Koeffizientenmatrix:")
    print(A)

    #Aenderung der Koeffizienten von c
    for s in range(len(A[0])):
        c[s] = c[s] - (c[piv_j] * A[piv_i, s]) / A[piv_i, piv_j]
    print("Zielfunktion:")
    print(c)
