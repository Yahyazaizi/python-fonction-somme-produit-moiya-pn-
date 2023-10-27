def somme (t):
    return sum(t)

def produit (t):
    p=1
    for i in range(0,10):
        p = p * t[i]
    return p
def moiyan (t):
    m=0
    for i in range(0,10):
        m =somme(t)/10
    return m
def nature (t):
    for i in range(10):
        if t[i]>0:
            print("le nomeber et bositife:",t[i])
    for i in range(10):
        if t[i]<0:
            print("le nomeber et negative:",t[i])
t=[]
for i in range(10):
    v=float(input("svp doe un reel:"))
    t.append(v)
print(somme(t))
print(produit(t))
print(moiyan(t))
print(nature(t))
