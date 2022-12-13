"""Implementierung des Simplex-Optimierungsalgorithmus in Python - 10/12/22"""

import numpy as np


def simplex(A, b, c):
    # SIMPLEX-ALGORITHMUS beginnt hier---------------------------------------------------
    # Platzhalter für Hilfsgröße q (Liste mit Nullen und der gleichen Dimension, wie b)
    q = np.empty(len(b))

    # Ergebnis der Optimierungsfunktion
    z = 0.0

    # Ermittlung der Anzahl der Variablen ohne Schlupf-Variablen
    anz_mgl_basis = 0
    while c[anz_mgl_basis] != 0:
        anz_mgl_basis += 1

    # Pivot-Elemente abspeichern, zur Ermittlung der Basisvariablen und deren Lösungen
    speicher_piv = np.full(len(c), np.inf)  # vorfüllen, weil alle geänderten Orte später erkennbar sein sollen

    # Zählvariable für Indizierung der Iterationsschritte
    k = 1

    # Abbruchkriterium-------------------------------------------------------------------
    # Das Ergebnis lässt sich verbessern, solange Koeffizienten der Zielfunktion > 0
    while max(c) > 0 and k < 10:     # k begrenzt, damit Schleife nicht unendlich läuft

        # Abgrenzung der einzelnen Iterationsschritte in der Ausgabe
        print("")
        print("------------------------------------")
        print("Iterationsschritt:", k,)
        k = k + 1

        # PIVOT-SPALTE:------------------------------------------------------------------
        # Finde Indizes des größten Koeffizienten in der Zielfunktion c
        piv_s = np.argmax(c)    # liefert die Position des größten Wertes in Array

        # PIVOT-ZEILE:-------------------------------------------------------------------
        # Schleife über alle Zeilen von q
        for i in range(len(q)):
            if A[i, piv_s] != 0:
                q[i] = b[i] / A[i, piv_s]   # Hilfsgröße q
            if A[i, piv_s] == 0:
                q[i] = np.inf
        print("Hilfsquotient \t : q =", q)

        # Finde Indizes des kleinsten positiven Koeffizienten in q
        for i in range(len(q)):
            if q[i] < 0:
                q[i] = np.inf   # setzt alle Einträge < 0 auf Unendlich
        piv_r = np.argmin(q)    # liefert die Position des kleinsten Wertes in Array

        # PIVOT-Element:-----------------------------------------------------------------
        piv = A[piv_r, piv_s]
        print("Pivot-Element \t :", "A[", piv_r, ",", piv_s, "] =", piv)

        # Orte der Pivot-Elemente jedes Iterationsschrittes abspeichern
        speicher_piv[piv_s] = piv_r

        # Normieren der Pivot-Zeile von b und A------------------------------------------
        b[piv_r] = b[piv_r] / A[piv_r, piv_s]
        A[piv_r] = A[piv_r] / A[piv_r, piv_s]   # ganze Zeile von A durch Pivot-Element

        # ÄNDERUNG b---------------------------------------------------------------------
        for i in range(len(b)):     # Schleife über alle Zeilen von b
            if i != piv_r:      # alle Elemente von b außer Pivot-Zeile
                b[i] = b[i] - b[piv_r] * A[i, piv_s]
        print("Ergebnisvektor \t : b =", b)

        # ÄNDERUNG z
        z = z - b[piv_r] * c[piv_s]
        print("Gewinn \t\t\t : z =", z)

        # ÄNDERUNG c---------------------------------------------------------------------
        for j in range(len(A[0])):
            if j != piv_s:      # alle Elemente von c außer Pivot-Spalte
                c[j] = c[j] - c[piv_s] * A[piv_r, j]

        c[piv_s] = 0            # Pivot-Spalte erst zum Schluss 0 setzen
        print("Zielfunktion \t : c =", c)

        # ÄNDERUNG A---------------------------------------------------------------------
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i != piv_r and j != piv_s:   # alle Elemente von A außer Pivot-Element
                    A[i, j] = A[i, j] - A[i, piv_s] * A[piv_r, j]

        for i in range(len(A)):
            if i != piv_r:
                A[i, piv_s] = 0     # Pivot-Spalte erst zum Schluss 0 setzen
        print("Koeffizientenmatrix : A =")
        print(A)

    # Ende des Simplex Algorithmus------------------------------------------------------
    print()
    print("------------------------------------")
    print("|  SIMPLEX-VERFAHREN ABGESCHLOSSEN |")
    print("------------------------------------")
    print("Basisvariablen der Zielfunktion:")
    # Ermittlung der Basisvariablen und deren Werte
    for i in range(len(c)):
        if speicher_piv[i] != np.inf and i < anz_mgl_basis:
            print("x  ", i+1, "=", b[round(speicher_piv[i])])
            # muss gerundet werden, da die Werte vorher nicht als Integer abgespeichert
            # und somit nicht für die Indizierung eines Arrays nutzbar

    # Ermittlung ob Schlupf-Variablen Basisvariablen sind
    for i in range(len(c)):
        if speicher_piv[i] != np.inf and i >= anz_mgl_basis:
            print("x_s", i-anz_mgl_basis+1, "=", b[round(speicher_piv[i])])
    print("------------------------------------")
