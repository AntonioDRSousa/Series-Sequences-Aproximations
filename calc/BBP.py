from decimal import *

def BBP(nit,prc):
    def frac(k,t):
        v=[(4,1),(2,4),(1,5),(1,6)]
        r , s = v[t]
        return Decimal(r)/Decimal(8*k+s)

    def it(k):
        a = 1/Decimal(16**k)
        b = frac(k,0)-frac(k,1)-frac(k,2)-frac(k,3)
        return a*b

    getcontext().prec = prc
    sm=0
    for i in range(0,nit+1):
        sm += it(i)   
    return str(sm)
    
def read():
    nit = int(input("number of iterations = "))
    prc = int(input("precision = "))
    ndigits = int(input("number of digits = "))
    njoin = int(input("number of join digits = "))
    nparts = int(input("number of parts of join digits = "))
    return nit, prc, ndigits, njoin, nparts

def write(s,ndigits,njoin,nparts):
    print("------------------------------")
    s1 , s2 = s.split('.')
    s2 = s2[0:ndigits]
    print(s1+".")
    x = 0
    for i in range(0,len(s2)):
        print(s2[i],end="")
        if (i%njoin==(njoin-1)):
            print(" ",end="")
            x+=1
        if x==nparts:
            x=0
            print()
    print()
    print("------------------------------")

def main_BBP():
    nit, prc, ndigits, njoin, nparts = read()
    s = BBP(nit,prc)
    write(s,ndigits,njoin,nparts)