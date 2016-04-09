# PASSWORD CRACKER
import sys
import string
import time
import mincemeat
start_time = time.time() #start time
a=[]
low=list(string.ascii_lowercase) #lowercase
num=list(map(chr, range(48, 58))) #numbers
l=low+num
for i in range(0,len(l)):
    a.append(l[i])
    for j in range(0,len(l)):
        a.append(l[i]+l[j])
        for k in range(0,len(l)):
            a.append(l[i]+l[j]+l[k])
            for z in range(0,len(l)):
                a.append(l[i]+l[j]+l[k]+l[z]) #creating permutations

def chunks(a, n): #splitting into chunks
    for i in range(0, len(a), n):
        yield a[i:i+n]
data=chunks(a,1000)
datasource=dict(enumerate(data)) #key value pairs

for i in range(0,len(datasource)):
    new_key=str(i)+"&"+sys.argv[1] #adding the sys.arg to the key with a delimiter
    datasource[new_key] = datasource.pop(i)

def mapfn(k,v):
    password=k.split('&')[1] #splitting the sys.arg from the key, using the delimiter
    import hashlib
    for i in range(0,len(v)):
        if hashlib.md5(v[i]).hexdigest()[:5]==password: #check for match
            yield 1,v[i] #yield matched pass

def reducefn(k, vs):
    return vs
	
s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print "Hacked passwords: %s" % results

print("--- Time elapsed: %s seconds ---" % (time.time() - start_time))	
