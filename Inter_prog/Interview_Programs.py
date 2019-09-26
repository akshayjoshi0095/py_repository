###     1-WAP fabonicci series using generator

def fabo_generator():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

for i in fabo_generator():
    if i>100:
        break
    print i,

print '\n'
###--------------------------------------------
###     2-WAP fabonicci series
def fabo1(NoOfElement):
    a,b=0,1
    while NoOfElement>0:
        print a,b,
        a,b=b,a+b
        NoOfElement-=1
        
fabo1(10)

###--------------------------------------------
###     3-Wap of printing prime no series upto the given no..

def Prime(n):
    p=[]
    for i in range(2,n+1):
        j=2
        while j<i:
            if i%j==0:
                print '%s is not a prime no'%i
                break
            j+=1
        if j==i:
            p.append(i)
            print '%s is a prime no'%i
    print 'list of all prime no:',p
    print 'sum:',reduce(lambda a,b:a+b,p)
Prime(50)

#------------------------------------------------
l2=[2,3,4]
l3=[5,6,7]
for i in l2:
    for j in l3:
        print (i,j),

print '\n'
print [(i,j) for i in l2 for j in l3]

#-----------------------------------------------------------------
#WAP to change str of lowercase to uppercase without using lower/upper

s='akshay'
for i in s:
    print chr(ord(i)-32),

## -------------------------------------------------------------------















