import numpy as np

def summeNote(noten, P, n):
    """Berechnung der Summen-Anzahl einer Note der Schüler"""
    if type(noten) is list:
        notenList = list()
        for i in range(len(noten)):
            calc = round(noten[i] * P[i][n])
            notenList.append(calc)
        return sum(notenList)
    else:
        print("noten must be an array-like list item")


if __name__ == "__main__":

    P = [   
            [0.63, 0.21, 0.12, 0.04, 0.00, 0.00],
            [0.18, 0.50, 0.23, 0.07, 0.02, 0.00],
            [0.09, 0.19, 0.41, 0.17, 0.09, 0.05],
            [0.02, 0.09, 0.17, 0.37, 0.23, 0.12],
            [0.00, 0.05, 0.07, 0.17, 0.51, 0.20],
            [0.00, 0.00, 0.05, 0.11, 0.19, 0.65]
    ]

    noten = [4, 10, 8, 2, 2, 2]

    anzahl = sum(noten)

    print("Schüler insgesamt: {}".format(anzahl))

    for i in range(len(noten)):
        anzahlNotenKlasse6 = [summeNote(noten, P, n) for n in range(len(noten))]
    print("Alle Noten am Ende der 6. Klasse: {}".format(anzahlNotenKlasse6))

    for i in range(len(anzahlNotenKlasse6)):
        anzahlNotenKlasse7 = [summeNote(anzahlNotenKlasse6, P, n) for n in range(len(noten))]
    print("Alle Noten am Ende der 7. Klasse {}".format(anzahlNotenKlasse7))

    for i in range(len(anzahlNotenKlasse7)):
        anzahlNotenKlasse8 = [summeNote(anzahlNotenKlasse7, P, n) for n in range(len(noten))]
    print("Alle Noten am Ende der 8. Klasse {}".format(anzahlNotenKlasse8))

    for i in range(len(anzahlNotenKlasse8)):
        anzahlNotenKlasse9 = [summeNote(anzahlNotenKlasse8, P, n) for n in range(len(noten))]
    print("Alle Noten am Ende der 9. Klasse {}".format(anzahlNotenKlasse9))


    # WS 10.Klasse Note 2
    vector = np.array([4/anzahl, 10/anzahl, 8/anzahl, 2/anzahl, 2/anzahl, 2/anzahl])

    results = list()
    results.append(vector @ P)

    for i in range(5):
        temp = results[i] @ P
        results.append(temp)

    # Print
    print("k\tp(k)") 
    for i in range(5+1):
        print(str(i+6) + "\t" + str(results[i]))