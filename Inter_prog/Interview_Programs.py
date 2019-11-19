from threading import *


'''
1-WAP fabonicci series using generator
'''
def fabo_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for i in fabo_generator():
    if i > 100:
        break
    print(i, end=',')
print('\n')


'''
2-WAP fabonicci series
'''
def fabo1(NoOfElement):
    a, b = 0, 1
    while NoOfElement > 0:
        print
        a, b,
        a, b = b, a + b
        NoOfElement -= 1

fabo1(10)

'''
   3-Wap of printing prime no series upto the given no..
'''

def Prime(n):
    a=2
    l=list()
    l1=[0,1]
    while len(l)<=n:
        m=2
        while m<a:
            if a%m==0:
                break
            else:
                m+=1

        if m==a:
            l.append(a)
        else:
            l1.append(a)
        a+=1
    print('prime no.:',l)
    print('non-prime no.:', l1)
Prime(50)

# ------------------------------------------------
l2 = [2, 3, 4]
l3 = [5, 6, 7]
for i in l2:
 for j in l3:
     print(i, j,end=',')

print('\n')
print([(i, j) for i in l2 for j in l3])

'''
 WAP to change str of lowercase to uppercase without using lower/upper
'''
s = 'akshay'
for i in s: print(chr(ord(i) - 32),end=',')



def sorting(l):
    for i in range(1, len(l)):
        k = l[i]
        j = i - 1
        while (j >= 0 and l[j] > k):
            l[j + 1] = l[j]
            l[j] = k
            j = j - 1
        print(l)


sorting([9, 7, 3, 8, 1, 100, -7, 34, 56])


# from threading import *
def sum(*s):
    res = 0
    for i in s:
        res = res + i
    return res


def multithreading_return(*l):
    print('sum is {} \n'.format(sum(*l)))


print(current_thread().name)
t1 = Thread(target=multithreading_return, args=(1, 2, 3, 4))
t2 = Thread(target=multithreading_return, args=(5, 5, 5, 5, 2, 3, 5))
t1.start()
t2.start()
print('\ndone')



'''
WAP of factorial

NOTE :- returning is compulsory and then either store in variable or print directly

'''
def fact(n):
    if n==0:
        return 1
    else:
        result=n*fact(n-1)
        return result
res=fact(5)
print ('factorial:%d'%res)


''' Anonymous func()'''

l=[1,2,3,4,5,6,7,8,9]
print(list(map(lambda x:x**2,l)))
print(list(filter(lambda x:x%2==0,l)))
s=lambda x:x**2
print (s(6))

'''
WAP to change str of lowercase to uppercase without using lower/upper
'''

s='akshay'
for i in s:
    print(chr(ord(i)-32),end='')

	
'''
selection sort:
principle:- find the min most element and then delete it from it location and place it to the 0th index
            and then repeat the same with rest of the element
'''
l=[2,5,4,78,4,6,-7,8,0]
for i in range(0,len(l)):
    min=l[i]
    for j in range(i+1,len(l)):
        if min>l[j]:
            min=l[j]
            print('min:',min)
    l.remove(min)
    l.insert(i,min)
print ('sorted list:',l)

