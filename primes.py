# PALINDROME PRIMES
import random
import time
import mincemeat
start_time = time.time()

p=range(2,10000001)
random.shuffle(p)
def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]
data=chunks(p,10000)
datasource=dict(enumerate(data))

def mapfn(k,v):
    from random import randint
    x=v
    for i in range(1,len(x)):
        a=str(x[i])
        b=str(x[i])[::-1]
        if a==b:
            j = randint(1, 4)
            yield j,x[i]

def reducefn(k, vs):
    a=[]
    for i in range(0,len(vs)):
        check=1
        for n in range(2,int(vs[i]**0.5)+1):
            if vs[i]%n==0:
                check=0
                break
        if check==1:
            a.append(vs[i])
    return a
    
s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

result = s.run_server(password="changeme")
print "Palindrome primes"
x= result[1]+result[2]+result[3]+result[4]
x = sorted(filter(lambda a: a != 0, x))
print x
print "Sum: %d" % sum(x) 
print "Count: %d" % len(x)
print("--- %s seconds ---" % (time.time() - start_time))
