""""Eingabe des Simplex-Tableau von Aufgabe 1 in die ausgelagerte Funktion"""

from simplex import *

# EINGABE DES TABLEAUS---------------------------------------------------------------
# Koeffizienten des Gleichungssystems
A = np.array([
    [1., 1., 1., 0., 0.],
    [1., -2., -1., 0., 0.],
    [2., 1., -1., 0., 1.]
])

# Ergebnisvektor des Gleichungssystems
b = np.array([5., 3., 1.])

# Koeffizienten der Zielfunktion
c = np.array([-1.0, 1.0, -1.0, 0.0, 0.0])

simplex(A, b, c)
