
#### writing operation

##1- write()  -- write only one line at one time, separator is compulsory
f=open('D:\\def.txt','w')
f.write('Akshay ')
f.write('Joshi')
f.close()

##2- writelines() ---write multiple line at one time, separator is compulsory, different lines must be provided in a list with separator
with open('D:\\xyz.txt','w') as f:
    l=['alpha\n','beta\n','charlie\n','Delta']
    f.writelines(l)


### read operation

####1- read()    --- for reading the completly
f=open('D:\\def.txt','r')
print f.read()

####2-read(n)      --- used to read only first element and even seperator like lines,comma and space is count as one values
print f.read(10)
f.close()

#####3-readlines  --- used to read lines one by one, on specifying more readlines() it never raise any exo
f=open('D:\\xyz.txt','r')
print f.readline(),         ## this function automatically add \n so to avoid it , is used
print f.readline(),
print f.readline(),
print f.readline(),
print f.readline(),
f.close()

#4-readlines()  -- read all the lines of the file and keep all lines of the file in a list
with open('D:\\xyz.txt','r') as f:      #### benifit of using with is that we do not explicitly need to close the file,
    list=f.readlines()                      # >>  as the compiler comes of the with loop file will automatically get closed.
    print '\n readlines:%s'%list
    for i in range (len(list)):
        print list[i],
print f.closed                    ######### proof of with statement i.e True


### way of reading a file without using readlines()
with open('D:\\xyz.txt','r') as f:
    for r in f:                         ### here type(f) is <type 'file'>, it return a iterator containing content of each line which we can read
        print r,                         ##   >> by for loop

### program for copy paste
f1=open('D:\\xyz.txt','r')
f2=open('D:\\mno.txt','w+')
f2.write(f1.read())
f1.close()
f2.close()


### WAP to get whether a file exist in the given location if yes then print the data

import os,sys

fname=input('enter the file name:')
if os.path.isfile(fname):
    print 'file exist'
    f=open(fname,'r')
else:
    print 'file do not exist'
    sys.exit()
print 'data:',f.read()

#### Wap to find no. of lines, word in each lines, character in the lines

lcount=wcount=ccount=0
with open(fname,'r') as f:
    for i in f:
        lcount=lcount+1
        wcount=wcount+len(i.split())
        ccount=ccount+len(i)

print 'lcount:',lcount
print 'wcount:',wcount
print 'ccount:',ccount



### WAP for binary data
f=open('D:\\ScreenShots\\pic1.jgp')
x=f.read()
f.close()
f=open('D:\\TRY\\new_pic1.jgp','wb')
f.write(x)
f.close()
f=open('D:\\TRY\\new_pic1.jgp','rb')
print f.read()



### WAP to undersand concept of tell() and seek()

with open('D:\\TRY\\FileHandeling5.txt','w') as f:
    f.write('Akshay is a very brave boy')
    print 'current position:',f.tell()
    f.seek(17)
    f.write('handsome boy')
    print 'current position:', f.tell()
f=open('D:\\TRY\\FileHandeling5.txt','r')
print f.read()


bfjdvkjdfvjkd

