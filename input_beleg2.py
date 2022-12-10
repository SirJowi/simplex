""""Eingabe des Simplex-Tableau von Aufgabe 2 in die ausgelagerte Funktion"""

from simplex import *

# EINGABE DES TABLEAUS---------------------------------------------------------------
# Koeffizienten des Gleichungssystems
A = np.array([
    [-1., 2., 1., -1., 1., 0., 0.],
    [1., 4., 0., -2., 0., 1., 0.],
    [1., -1., 0., 1., 0., 0., 1.]
])

# Ergebnisvektor des Gleichungssystems
b = np.array([1., 1., 4.])

# Koeffizienten der Zielfunktion
c = np.array([-2.0, 2.0, 1.0, 1.0, 0.0, 0., 0.])

simplex(A, b, c)
