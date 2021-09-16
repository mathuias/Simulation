

if __name__ == "__main__":

    alpha = 0.05
    chi2quantile = 1 - alpha
    n = [60, 33, 13, 14]
    p = [0.52324, 0.24936, 0.119, 0.108368]

    length = len(n)
    df = length-1
    n_sum = sum(n)

    # calculate n star
    n_star = list()

    for i in range(length):
        temp = p[i] * n_sum
        n_star.append(temp)

    # calculate single test_values
    test_values = list()

    for i in range(length):
        temp = ( n[i] - n_star[i] )**2 / n_star[i]
        test_values.append(temp)

    test = sum(test_values)

    print("i\tn\tp(i)\tn*(i)\t((n(i)-n*(i))^2 / n*(i))") 
    print("--------------------------------------------------------")
    
    for i in range(length):
        print(str(i) + "\t" + str(n[i]) + "\t" + str(p[i]) + "\t" + str(n_star[i]) + "\t" + str(test_values[i]) )

    print("Sum of n: {}".format(n_sum))
    print("Number of table values: {}".format(length))
    print("Freiheitsgrade: {}".format(df))
    print("Chi^2 Verteilung 1-alpha: {}".format(chi2quantile))
    print("eswf.uni-koeln.de/glossar/chivert.htm")
    print("\n")
    print("Final Test Value: {}".format(test))
    
    
