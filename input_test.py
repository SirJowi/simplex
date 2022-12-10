""""Eingabe eines Test Simplex-Tableau in die ausgelagerte Funktion"""

from simplex import *

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

simplex(A, b, c)
