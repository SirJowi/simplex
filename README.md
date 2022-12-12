# Simplex-Algorithmus
Im Zuge eines Moduls zur Tragwerksoptimierung sollte der Simplex-Algorithmus als Programm umgesetzt werden. 
Dabei wurde Python empfohlen und damit entstand dieses, mein erstes, Python-Programm.

Der eigentliche Algorithmus ist als Funktion ausgelagert. 

In einer neuen Python-Datei wird die Funktion eingebunden und die Problemstellung in folgender Art übergeben:

Zielfunktion c:  
muss eine Maximum-Aufgabe sein (falls nicht, "*-1")

Nebenbedingungen A:     
Ungleichheitsbedingungen führen zu Schlupfvariablen (">=" -> "-x_i" ; "<=" -> "+x_i")
Ergebnisvektor der Nebenbedingungen dürfen nicht negativ sein (falls doch, "*-1")

Ergebnisvektor b:  
Ergebnisvektor der Nebenbedingungen
