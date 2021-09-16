from math import factorial as fac 

def binomial(n, k):
    try:
        return fac(n) // fac(k) // fac(n-k) 
    except ValueError:
        return 0

def pascal(m):
    for x in range(m+1):
        print( [ binomial(x, y) for y in range(x+1) ] ) 

def main():
    #input = raw_input
    n = int(input("Enter a value for n: "))
    k = int(input("Enter a value for k: "))
    print(binomial(n, k))

if __name__ == "__main__":
    #pascal(8)
    main()