import numpy as np
from prim import prims, singlePrims


def linKonGru(m, a, c, x0, n):
    x = list()
    x.append(x0)

    for i in range(n+1):
        temp = ((a * x[i] + c) % m)
        x.append(temp)

    print("k\tp(k)") 
    print("------------")
    for i in range(n+1):
        print(str(i) + "\t" + str(x[i]))



if __name__ == "__main__":
    m = 240
    x0 = 603
    n = 5

    print("Prims of {}: {}".format(m, prims(m)))

    # a
    aFirst = int(np.floor( np.sqrt(m) ))
    aLast = int(m - 1)
    print("a element of [{}, ..., {}]".format(aFirst, aLast))
    aList = [i for i in range(aFirst, aLast)]

    # c
    cFirst = int(np.floor( m/5 ))
    cLast = int(m - 1)
    print("c element of [{}, ..., {}]".format(cFirst, cLast))
    cList = [i for i in range(cFirst, cLast)]

    # m und c Teiler-Fremd: c darf KEINE prims von m enthalten
    c = 340
    # a-1 und m Teiler-Freund: a-1 muss ALLE prims von m enthalten
    a = 43
    # wenn m/4 dann auch a-1/4
    

    # lineare Kongruenz berechnen
    linKonGru(m, a, c, x0, n)








