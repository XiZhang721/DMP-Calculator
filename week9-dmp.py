def b(x,n,p):
    q=1-p
    a=p**x
    c=q**(n-x)
    d=e(n)/(e(n-x)*e(x))
    return a*c*d

def e(x):
    i,j=1,1
    while(i<=x):
        j*=i
        i+=1
    return j

def k(l,u,n,p):
    q=0
    for i in range (l,u+1):
        q+=b(i,n,p)
    return q

def std(n,p):
    k=[]
    q=0
    a=0
    for i in range (0,n+1):
        k.append(b(i,n,p))
        q+=i*b(i,n,p)
    for i in range (0,n+1):
        a+=((i-q)**2)*k[i]
    return a**(1/2)

