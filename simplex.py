"""Implementierung des Simplex-Optimierungsalgorithmus in Python - 08/12/22"""

import numpy as np

# Koeffizienten des Gleichungssystems
A = np.array([[1, 1, -1, 0,  0],
              [-1, 1,  0, 1,  0],
              [-2, 1,  0, 0, -1]])

# Ergebnisvektor des Gleichungssystems
b = np.array([5, 5, 2])

# Koeffizienten der Zielfunktion
c = np.array([2, 3, 0, 0, 0])

# Platzhalter für Hilfsgröße q (Liste mit Nullen und der gleichen Zeilenanzahl wie A)
q = np.empty(len(A))

# Zählvariable für Indizierung der Iterationsschritte
k = 1

# Abbruchkriterium-------------------------------------------------------------------------
# Das Ergebnis lässt sich verbessern, solange Koeffizienten der Zielfunktion > 0
while max(c) > 0:

    # Abgrenzung der einzelnen Iterationsschritte in der Ausgabe
    print("Iterationsschritt:", k, "--------------------------")
    k = k + 1

    # PIVOT-SPALTE:-----------------------------------------------------------------------
    # Finde Indizes des größten Koeffizienten in der Zielfunktion c
    piv_j = np.argmax(c)

    # PIVOT-ZEILE:-----------------------------------------------------------------------
    # Schleife über alle Zeilen von A
    for i in range(len(A)):
        # Hilfsgröße q
        q[i] = b[i] / A[i, piv_j]
    # Finde Indizes des kleinsten positiven Koeffizienten in q
    piv_i = np.argmin(c)

    print("Pivotelement [zeile, spalte]:")
    print("[", piv_i, ",", piv_j, "]")
    # ÄNDERUNG b-----------------------------------------------------------------------
    # Schleife über alle Zeilen von b
    for i in range(len(A)):
        # Normierung der Zeile i vom Ergebnisvektor b
        if i == piv_i:
            b[i] = b[i] / A[piv_i, piv_j]
        # Berechnungen der übrigen Koeffizienten von b
        else:
            b[i] = b[i] - b[piv_i] * A[i, piv_j]
    print("Ergebnisvektor:")
    print(b)

    # ÄNDERUNG A-----------------------------------------------------------------------
    for s in range(len(A[0])):                      # über Spalte s (0 bis 4)
        for r in range(len(A)):                     # über Zeile r (0 bis 2)
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

    # ÄNDERUNG c-----------------------------------------------------------------------
    for s in range(len(A[0])):
        c[s] = c[s] - (c[piv_j] * A[piv_i, s]) / A[piv_i, piv_j]
    print("Zielfunktion:")
    print(c)
