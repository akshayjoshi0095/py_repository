import logging

'''
f=open(file: Union[str, bytes, int, PathLike],
         mode: str = ...,
         buffering: int = ...,
         encoding: Optional[str] = ...,
         errors: Optional[str] = ...,
         newline: Optional[str] = ...,
         closefd: bool = ...,
         opener: Optional[(str, int) -> int] = ...)
         
f.name          ## returns complete path of the file with name and extension
f.mode          ## return the open mode
f.closed        ## return True if close else return False
f.close()       ## close the opened file
f.readable()    ## True - if file is in readable form else False
f.writable()    ## True - if file is in writeable form else False


r-  Also Default mode but for binary file we have specify explicity
If the file is not present in the defined location --- FileNotFoundError
print 'is_readable:%s'%f.readable()              ### is_readable:True
print 'is_writeable:%s'%f.writable()             ### is_writeable:False

w-
If the file is not present in the defined location --- it will automatically creats file
print 'is_readable:%s'%f.readable()              ### is_readable:False
print 'is_writeable:%s'%f.writable()             ### is_writeable:True

a
If the file is not present in the defined location --- it will automatically creats file
print 'is_readable:%s'%f.readable()              ### is_readable:False
print 'is_writeable:%s'%f.writable()             ### is_writeable:True

r+
print 'is_readable:%s'%f.readable()              ### is_readable:True
print 'is_writeable:%s'%f.writable()             ### is_writeable:True

w+
print 'is_readable:%s'%f.readable()              ### is_readable:True
print 'is_writeable:%s'%f.writable()             ### is_writeable:True

a+
print 'is_readable:%s'%f.readable()              ### is_readable:True
print 'is_writeable:%s'%f.writable()             ### is_writeable:True

x
print 'is_readable:%s'%f.readable()              ### is_readable:False
print 'is_writeable:%s'%f.writable()             ### is_writeable:True
Through error if the files already present   --- File Exit Error

binary files=rb,wb,ab,r+b,w+b,a+b,xb
>> used for images, audio file and audio files

eg
f=open('D:\\ScreenShots\\pic1.jgp')
x=f.read()
f.close()
f=open('D:\\TRY\\new_pic1.jgp','wb')
f.write(x)
f.close()
f=open('D:\\TRY\\new_pic1.jgp','rb')
print f.read()



writing operation
1- write()  -- write only the content given within braces at one time, separator is compulsory
    eg.f=open('D:\\abc.txt', 'w')
       f.write('Hi, I am Akshay. \n I am from Uttarakhand')
       f.close()
    
2- writelines() ---write multiple line at one time, separator is compulsory, different lines must be provided in a list with separator
    eg-f=open('D:\\abc.txt', 'w')
       l=['akshay','uk','hld\n','seeshmahal\n']
       f.writelines(l)
       f.close()


read operation
1-read()    --- for reading the completly
2-read(n)      --- used to read only first element and even seperator like lines,comma and space is count as one values
3-readline  --- used to read lines one by one, on specifying more readlines() it never raise any exception
4-readlines()  -- read all the lines of the file and keep all lines of the file in a list, it is almost opposite to writelines()
    eg.f=open('D:\\abc.txt', 'r')
        print 'data:',f.readlines()
        f.close()
    o/t- ['akshayukhld\n', 'seeshmahal\n']

with:-
>> benefit of using with is that we do not explicitly need to close the file, as the compiler comes to the end of with
loop file will automatically get closed.
>> even in case of Exception also



###### Concept of tell() and seek()

f.tell(): this function retuns the current loaction of the cursor in the current file
>If we open the file with
r mode then default cursore location would be at 0
w mode then default cursore location would be at 1
a mode then default cursore location would be at last alphabet location   ## but in my machine this is not working.

NOTE:- but in Py 3 for all the mode default cursore location is at 0

f.seek(digit): This func is used to move cursor directly from one location to other as defined by user in arg
        > system will start counting fron very 1st letter as 0 will move upto (end-1)
        > if we define f.seek(4), system will start counting fron very 1st letter as 0 and will stop at 4th place
        > eg f.seek(2)  if f=akshay
            print f.read()
            f.close()
        o/t-shay

In py 2:
>> takes two arg

seek(offset(compulsory), fromwhere(compulsory))
offset - kitne step
fromwhere - koi se position se (ie 0,1,2)

fromwhere:
1- means count of seek will start from the current cursor position in the file and in forward direction
2- means count of seek will start from the very last index of the file and in backward direction

>> Io only accept +ve values in seek()

seek(-17)
>>ValueError: negative seek position -17
>> Invalid argument

In py 3
>> takes one arg

seek(offset(compulsory))
>> in py3 offset is always calculate fron starting index(ie from zeroth place means always from default one)



Txt handeling

Note- 
1-f=open('D:\\TRY\\FileHandeling7.txt')
  for i in f:          ### each time i contains one line of file in str() type , we can make use of string api to achieve results
    print i,


2-f.readlines()  >> ['line1\n', 'line2\n', 'line3\n',]
>> opp. to readlines()


## WAP to create a dublicate txt file 
with open('D:\\TRY\\FileHandeling7.txt','w') as f7:
    with open('D:\\TRY\\FileHandeling.txt') as f:
        f7.write(f.read())

		
directory handeling
>>  to know current working directory
    to create a dir
    to delete a dir 
    to rename a dir
    to get content of the dir


import os

way to get current directory
>>os.getcwd()

way to create new directory
>>os.mkdir('foldername with location')

way to create new multiple directories
>>os.makedirs('foldername with location\\folder\\folder\\folder\\folder')
>>means with this we can create folders which exist inside multiple folders at one time only.

way to remove a directory
>>os.rmdir('foldername with location')

way to create new multiple directories
>>os.removedirs('foldername\\folder\\folder\\folder\\folder with location')
>>means with this we can delete folders which exist inside multiple folders at one time only.

way to rename a dir
>>os.rename('foldername with location','newfoldername with location')

way to list the name of all the files/folder existing inside a dir
>> os.listdir('foldername with location')    ### it return all names in a list
>>os.listdir('.')  >> here '.' represent allfolder from cwd(current directory)
>>>>returns a list

way to know the no. of files/folder exit in a dir.
>>len(os.listdir('foldername with location'))
>>returns a list 

way to know all the subfolder and files 
>os.walk('foldername with location')      ### it always return a generator
>>returns a generator

Differnce b/t listdir() and walk()
>>  listdir() do not consider sub directories but walk() consider them also
>> listdir() returns list while walk() returns a generator


way to run py file during the execution of program in cmd 
>> os.system('filename with directory')
>> now compiler will go to this location and run the defined file in the cmd means whatever is defined in that particular file will
get executed.

way to know the details of any file
>>os.stat('foldername with location')



CSV Handeling

1-Way to writing csv
f=openfile('path with name',w,newline='')
w=csv.writer(f)
w.writerow(['ele1','ele2','ele3'])

now of times we use w.writerow that many rows will get created
and column depends on the no. of element we are passing in the list

eg - 
with open('D:\\TRY\\student1.csv','w') as f:
    w=csv.writer(f)
    w.writerow(['Name','Age','salary','exp'])
    while True:
        res = input('do u want one more entry:')
        if res.lower() == 'no':
            break
        name = input('name:')
        age = input('age')
        sal = input('sal')
        exp = input('exp')
        w.writerow([name, age, sal])
		
		
### WAP to create a dublicate csv file

with open('D:\\TRY\\student5.csv','w',newline='') as f:
    with open('D:\\TRY\\student.csv', 'r') as f1:
        w=csv.writer(f)
        r=csv.reader(f1)
        data=list(r)
        print data
        for i in data:
            w.writerow(i),



## WAP a achieve data engineering with csv file

with open('D:\\TRY\\student6.csv','w',newline='') as f:
    with open('D:\\TRY\\student.csv', 'r') as f1:
        w=csv.writer(f)
        r=csv.reader(f1)
        data=list(r)
        print data
        for i in range(0,len(data)):
            if i==0:
                l=data[i]
                index1=l.index('salary')
                index2=l.index('expenses')
                print index1,type(index1)
                print index2, type(index2)
                l.append('sav')
                w.writerow(l)
            else:
                l = data[i]
                l.append(float(l[index1])-float(l[index2]))
                w.writerow(l)
				

'''

# f=open('D:\\abc.txt', 'r+')
# print f.name
# print f.mode
# print 'is_close:%s'%f.closed
# print 'file existing data:%s'%f.read()
#f.write('Hi, I am Akshay.')
# print 'file existing data 2nd time:%s'%f.read()
#print 'file existing data:%s'%f.read()
#f.close()
#print 'is_close:%s'%f.closed

#IOError: [Errno 0] Error

# serailization == Pickling
# desearlization == unpickling

# f=open('D:\\abc.txt', 'w')
# print f.name
# print f.mode
# f.write('Hi, I am Akshay.')
# f.close()
# print 'is_close:%s'%f.closed
#
#
# f=open('D:\\abc.txt', 'r')
# print 'file existing data:%s'%f.read()
# f.close()
# print 'is_close:%s'%f.closed
#
#
# f=open('D:\\abc.txt', 'a')
# f.write(' I am learning Python.')
# f.close()
# print 'is_close:%s'%f.closed
#
# f=open('D:\\abc.txt', 'r')
# print 'is_readable',f.read
# print 'file existing data:%s'%f.read()
# f.close()
# print 'is_close:%s'%f.closed
#
# f=open('D:\\abc.txt', 'w')
# #print 'is_writeable',f.writable()
# l=['Uttarakhand\n','Nainital\n','Kathgodam\n']
# f.writelines(l)
# f.close()
# print 'is_close:%s'%f.closed
#
#
# f=open('D:\\abc.txt', 'r')
# #print 'is_readable',f.readable()
# print 'file existing data:%s'%f.readline()
# print 'file existing data:%s'%f.readline()
# print 'file existing data:%s'%f.readline()
# print 'file existing data:%s'%f.readline()
# print 'file existing data:%s'%f.readline()
# f.close()
# print 'is_close:%s'%f.closed

##### Way of reading the file line by line
# with open('D:\\abc.txt', 'r') as f:   #### benifit of using with is that we do not explicitly need to close the file, as the compiler comes of the with loop file will automatically get closed.
#     j=1
#     for i in f.readlines():
#         print '{} lines is {}'.format(j,i)
#         j+=1
# print 'is_close:%s'%f.closed
# f.close()
# print 'is_close:%s'%f.closed