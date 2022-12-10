"""Implementierung des Simplex-Optimierungsalgorithmus in Python - 08/12/22"""

import numpy as np

# EINGABE DES TABLEAUS---------------------------------------------------------------
# Koeffizienten des Gleichungssystems
A = np.array([
    [1.0, 1.0, -1.0, 0.0, 0.0],
    [-1.0, 1.0, 0.0, 1.0, 0.0],
    [-2.0, 1.0, 0.0, 0.0, -1.0]
])

# Ergebnisvektor des Gleichungssystems
b = np.array([5.0, 5.0, 2.0])

# Koeffizienten der Zielfunktion
c = np.array([2.0, 3.0, 0.0, 0.0, 0.0])

# SIMPLEX-ALGORITHMUS beginnt hier---------------------------------------------------
# Platzhalter für Hilfsgröße q (Liste mit Nullen und der gleichen Zeilenanzahl wie A)
q = np.empty(len(A))

# Ergebnis der Optimierungsfunktion
z = 0.0

# Zählvariable für Indizierung der Iterationsschritte
k = 1

# Abbruchkriterium-------------------------------------------------------------------
# Das Ergebnis lässt sich verbessern, solange Koeffizienten der Zielfunktion > 0
while max(c) > 0 and k < 4:     # k begrenzt, damit Schleife nicht unendlich läuft

    # Abgrenzung der einzelnen Iterationsschritte in der Ausgabe
    print("")
    print("------------------------------------")
    print("Iterationsschritt :", k,)
    k = k + 1

    # PIVOT-SPALTE:------------------------------------------------------------------
    # Finde Indizes des größten Koeffizienten in der Zielfunktion c
    piv_s = np.argmax(c)    # liefert die Position des größten Wertes in Array

    # PIVOT-ZEILE:-------------------------------------------------------------------
    # Schleife über alle Zeilen von A
    for i in range(len(A)):
        q[i] = b[i] / A[i, piv_s]   # Hilfsgröße q
    print("Hilfsquotient \t q:", q)

    # Finde Indizes des kleinsten positiven Koeffizienten in q
    for i in range(len(q)):
        if q[i] < 0:
            q[i] = np.inf   # setzt alle Einträge < 0 auf Unendlich
    piv_r = np.argmin(q)    # liefert die Position des kleinsten Wertes in Array

    # PIVOT-Element:-----------------------------------------------------------------
    piv = A[piv_r, piv_s]
    print("Pivot-Element \t  :", "A[", piv_r, ",", piv_s, "] =", piv)

    # Normieren der Pivot-Zeile von b und A------------------------------------------
    b[piv_r] = b[piv_r] / A[piv_r, piv_s]
    A[piv_r] = A[piv_r] / A[piv_r, piv_s]   # ganze Zeile von A durch Pivot-Element

    # ÄNDERUNG b---------------------------------------------------------------------
    for i in range(len(b)):     # Schleife über alle Zeilen von b
        if i != piv_r:      # alle Elemente von b außer Pivot-Zeile
            b[i] = b[i] - b[piv_r] * A[i, piv_s]
    print("Ergebnisvektor \t b:", b)

    # ÄNDERUNG z
    z = z - b[piv_r] * c[piv_s]
    print("Gewinn \t\t\t z:", z)

    # ÄNDERUNG c---------------------------------------------------------------------
    for j in range(len(A[0])):
        if j != piv_s:      # alle Elemente von c außer Pivot-Spalte
            c[j] = c[j] - c[piv_s] * A[piv_r, j]

    c[piv_s] = 0            # Pivot-Spalte erst zum Schluss 0 setzen
    print("Zielfunktion \t c:", c)

    # ÄNDERUNG A---------------------------------------------------------------------
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i != piv_r and j != piv_s:   # alle Elemente von A außer Pivot-Element
                A[i, j] = A[i, j] - A[i, piv_s] * A[piv_r, j]

    for i in range(len(A)):
        if i != piv_r:
            A[i, piv_s] = 0     # Pivot-Spalte erst zum Schluss 0 setzen
    print("Koeffizientenmatrix A:")
    print(A)
