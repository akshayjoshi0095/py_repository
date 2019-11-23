"""
>>Python is a case sestive language
>>in Python indentation and space issues is present
>>SQL is not a cases senstive


##Best Features python
> Platform independent language >> means py code written in windows in appicable in other platform also like linix
> Functonal progarmming language(eg.function) as well as object oriented programming language(eg. methods)
> return any no. of values
> method overloading is not required.
> variable lenght argument thus we do not require method overloading 
> operator overloading is present
> multiple inhertance is possible
> loop + else statement
> cmd line reading capabilities

### Absent
>interface
>method overloading


NOTE:- 1-count() and len() function always consider counting from 1 instead from 0

2- Bollen results always comes in like False/True instead of false/true

3- to convert int into alphabet - chr(digit)
   to convert int into alphabet - ord('alphabet')
   
4-way to add , in a big int value
    x='{:,}'.format(1000000)
    x='10,000,000'
    type(x) >> str()
    
3- if we call any fundamental datatype without any argument, system will never throw any exception
    eg- int()       float()     complex()       str()       bool()
       >>0          >>0.0       >>0j            >>''        >>False

4->>> type(int)
        <type 'type'>
>>> type(type(int))
        <type 'type'>
>>> type('str')
        <type 'str'>
>>> type(type('str'))
        <type 'type'>
 
 Basiclly - type(<type 'type'>)         type(<type 'str'>)
             > <type 'type'>             > <type 'type'>

5-Way to creating complex no
    >x=2+6i
    >x=complex(12,5)
    >x=5+8J
    
    >x=8+9I
        > this will give error SyntaxError: invalid syntax
        > I or L stand for long in python.

6-If we want to input a string without inside single cots
	> str=raw_input('enter string:')
	
7-Difference b/t input() and raw_input()
	>only difference is that in raw_input() only accept str datatype only
	> means that we can give string without single and double cots
	> but in case of input we have to enter as per the datatype req. for the variable means that if we define any str without single cots python will through error.
      
8- sorted() do not work for sequence containing complex values.
    error - AttributeError: 'list' object has no attribute 'sorted'


9-enumerate(sequence, digit from which count will start) in Python
A lot of times when dealing with iterators, we also get a need to keep a count of iterations. 
Python eases the programmers’ task by providing a built-in function enumerate() for this task.
Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. 
This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.

e.g.:-
>>> s='akshay'
>>> for i in enumerate(list(s),0): print i
...
(0, 'a')
(1, 'k')
(2, 's')
(3, 'h')
(4, 'a')
(5, 'y')

>>> s='akshay'
>>> for i, j in enumerate(list(s),1):print i,'-',j
...
1 - a
2 - k
3 - s
4 - h
5 - a
6 - y

   
### Different way of reading inputs from Keyword

1- input('enter value:')
    > it takes all type of input as string
    > if we want to change that to some other datatype then we need to do type casting of that input

2- sys.stdin.readline()
    > it will also read all type of input as string datatype

3- Way of accepting multiple argument in one line code
    >a,b,c = [int(i) for i in input('enter 3 no.s : ').split()]

4- end= & sep=
    print (10,20,30,sep='.')
    print(10,end='//')
    print(20,end='////')
    print(30)


###Different way of formatting

1-print input'{} earn {}'.format('alpha','10000')
	>>alpha earn 10000

2-print input'{1} earn {0}'.format('alpha','10000')         ##catch point is that no. must start from 0 to n
	>>10000 earn alpha
	
	same as
	
	print input'{1:} earn {0:}'.format('alpha','10000')
	>>10000 earn alpha
	
	Note:- no. defined in the left side of : decides which argument has to be picked
		   no. defined in the right side of : decides how to represent that particular argument.
	
3-print '{:10} earn {:20}'.format('alpha',10000)
	>>alpha      earn                10000
	NOTE:- {:digit} - here this digit shows no. of spaces
			for string datatype - space comes in right hand side of string 
			for int datatype - space comes in left hand side of digit

4-Way of adding commas in a big int value:
	print '{:} earn {:,}'.format('alpha',10000000)  or   print '{} earn {:,}'.format('alpha',10000000)
		>>alpha earn 10,000,000
	Note- comma is applicable for the digit left side of decimal
		
5-Way of stamping a float value
	print '{:} earn {:,.5f}'.format('alpha',10000000.22374637854)
		>alpha earn 10,000,000.22375
	Note:- digit after . tells no of element we need after decimal point
			, is for commas as per international style
			f stand for float datatype

6-print '{} earn {:20,.5f}'.format('alpha',10000000.22374637854)
		>>alpha earn     10,000,000.22375
		
7-print '{1:d} earn {0:}'.format('alpha',10000000.12344667)
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	ValueError: Unknown format code 'd' for object of type 'float'
	
	Note - 1-with d we are not suppose to give decimal value but with f we can give int 
		   2- with f we can define a int value also but compiler will print a float value means it will add .000000(six zeroes)
		   3- if we define {:.3f} and in value we give 123.1 then sys will print 123.100


NOTE:-  %i, %d for int()
        %s for string
        %f for float
            

type(obj)
>> returns the datatype of an object

id(obj)
>> returns the addrress of an object


###  Way of inputing and printing value

NOTE:-  %i, %d for int()
        %s for string
        %f for float
    >> %s is applicable for all the data type
    
y=10.23
print('y=%d',y)   ## y=10
print('y=%f',y)   ## y=10.230000      
print('y=%s',y)   ## y=10.23




Imp_points:

### way of changing format of unicode string
unicodestring = u"Hello world"
print type(unicodestring)
asciistring = unicodestring.encode("ascii")
print type(asciistring)
print asciistring



All members in a Python class are public by default
>> we can access and modify from the outside the class using the object name.

### way of changing instance variable into protected variable
_instancevariable - is defined as protected varible
>> we can access and modify these variable also but it is not considered as a good programming habit


### way of changing instance variable into private variable
__instancevariable - is defined as private varible
>> we cannot access and modify these variable.
Python performs name mangling of private variables. Every member with double underscore will be changed to _object._class__variable. 
If so required, it can still be accessed from outside the class, but the practice should be refrained.
e.g obj._classname__privatevariable.


unicodestring = u"Hello world"
print type(unicodestring)
asciistring = unicodestring.encode("ascii")
print type(asciistring)
print asciistring


##  Common exceptions

1-TypeError: unbound method m2() must be called with A instance as first argument (got nothing instead)
    >> this come when while doing inhertance we call methods of parent class as Parentclass.method()
    >> correct way is Parentclass().method()

2- RuntimeError: cannot set daemon status of active thread
    >> this comes when we try to change the daemon status of a thread after starting it


## Operators:

1- '/' operator always perform floating point airthmetic and always return result of float data type
    eg. >>> 4/2
            2.0

2- '//'(floor operator) can performs both floating and integral arithmetic 
    >> if both the arguments are int then result will also be of int datatype
    >> if atleast any one of the argument is of float data type then result would be of float datatype
     eg:-   >>> 5/2
                2.5
            >>> 5//2
                2
            >>> 5.0//2
                2.0
            >>> 4.0//2
                2.0
            >>> 4//2.0
                2.0 

3- '%' return remainder
	>> it also works in same way as '//'
    >> if both the arguments are int then result will also be of int datatype
    >> if atleast any one of the argument is of float data type then result would be of float datatype
	eg:- >>> 4%2
			0
		>>> 4.0%2
			0.0
		>>> 4%2.0
			0.0
		>>> 4.0%2.0
			0.0


str * float
%
chaning of relational and equality operator









##way of printing data
a= input('enter your name:')
print ('a={}'.format(a))
print ('a:',a)
print ('a:%s'%a)
print ('{1},{2},{0}'.format('one','zero','three'))   ## catch point is that no we have to give no. starting from 0 to n



## sep() default separater is space
## end() default separater is \n
a,b,c,d=10,20,30,40
print (a,b,c,d)

### program to prove that tuple is faster then the list
import time

t1=time.clock()
l=[1,2,3,4,5,6]
for i in l:print (i)
t2=time.clock()
T1=t2-t1
print('time:',T1)

t3=time.clock()
t=(1,2,3,4,5,6)
for i in l:print (i)
t4=time.clock()
T2=t4-t3
print('time:',T2)

print (T1<T2)
"""

