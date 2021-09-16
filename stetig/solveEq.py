import sympy as sy 

# Diskret 3x3
pi0, pi1, pi2 = sy.symbols("pi0 pi1 pi2")

equations = [
                sy.Eq( 1/4*pi0      + 0*pi1         + 9/16*pi2,     pi0  ),
                sy.Eq( 1/2*pi0      + 2/3*pi1       + 4/16*pi2,     pi1  ),
                sy.Eq( 1/4*pi0      + 1/3*pi1       + 3/16*pi2,     pi2  ),
                sy.Eq(     pi0      +     pi1       +      pi2,     1)
]

print("\n Diskret 3x3 stationäre Vereilung")
print(sy.solve(equations))

# Stetig 4x4

pi0, pi1, pi2, pi3 = sy.symbols("pi0 pi1 pi2 pi3") 

equations2 = [
                sy.Eq( -3/5*pi0     + 0*pi1     + 4/19*pi2      + 0*pi3,     0),
                sy.Eq(  1/5*pi0     - 4/5*pi1   + 0*pi2         + 1/3*pi3,   0),
                sy.Eq(  2/5*pi0     + 1/5*pi1   - 5/19*pi2      + 1/3*pi3,   0),
                sy.Eq(   0*pi0      +3/5*pi1    + 1/19*pi2      - 2/3*pi3,   0),
                sy.Eq(   pi0        +    pi1    +      pi2      +     pi3,   1)
            ]

print("\n Stetig 4x4 stationäre Verteilung")
print(  sy.solve(   equations2, (pi0, pi1, pi2, pi3) )  )


# stetig 3x3
pi0, pi1, pi2 = sy.symbols("pi0 pi1 pi2")

equations3 = [
                sy.Eq( -1/2*pi0         + 1/20*pi1      + 1/10*pi2,     0 ),
                sy.Eq( 0*pi0            - 3/10*pi1      + 2/9*pi2,      0 ),
                sy.Eq( 1/2*pi0          + 1/4*pi1       - 29/90*pi2,    0 ),
                sy.Eq( pi0              +      pi1      +       pi2,    1 )
            ]
print("\n Stetig 3x3, stationäre Verteilung aus Intensitätsmatrix Q: ")
print(  sy.solve( equations3, (pi0, pi1, pi2) ) )