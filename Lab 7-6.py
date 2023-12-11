def numsum (n1, n2):
    global tot
    tot = n1 + n2

def numsum2 (n3, n4):
    global tot2
    tot2 = n3 + n4

def totsum(a, b, c, d):
    numsum(a, b)
    numsum2(c, d)
    totsum = tot + tot2
    print (totsum)

totsum (1, 2, 3, 4)
totsum (5, 10, 15, 20)
totsum (10, 20, 30, 40)
totsum (1, 10, 100, 1000)