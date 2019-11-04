

'''
>mutable
>insertion order is preserved but not in case of set and dictionary
>dynamic in nature
>dublicates
>heterogenous


## len(list)
	>> return no. of element present in the list
	>> consider count

# NOTE:- 1-count() and len() function always consider counting from 1 instead from 0

##way of accessing the ele
1-list[index]
2-Slicing-- l[start: end: step]  >> it will go upto (end-1) only, always create a new element

reversing by slice -    l[::-1], l[-1:-len(l)-1:-1]

if we give , instead to :   >>> TypeError: list indices must be integers, not tuple



### way of reversing a list

a-Affecting same list
l.reverse(), list=somelist

b- without Affecting same list >> create new obj always
slicing, copy(), reversed(l)[This will return a generator], Mathematical operation(i.e +,*)


### way to update the existing element at any index
l[i]=value  >> in this system will change the value of by the specified  value at the 'i'th index of the list.


## Imp function
# >>>len(l) --- returns length of list
# >>>l.insert(index,value)   --insert value at the specified location, system consider this index from 0
# >>>l.count(element)   ---- return no. of type a aprticular element present in the list
# >>>l.index(ele)  ---------	return the very 1st index at which particular element is present, system consider this index from 0
# >>> unpacking is possible but packing is not possible
# >>> member operator is applicable i.e in operator


### alasing(=) and cloning concept

>> in alasing address of both the remains same
>> means any change in one object will be appear to another object also. i.e l1=l2, address of both the object is same

>> in cloning we make a copy of the object1 with some other name such that both the object has different address
>> any change in any one element will not appear in other object  i.e copy(), slicing


#way of adding element to list

1-l.append()
>> accept only one argument at one time. In case of giving more than one argument - TypeError: append() takes exactly one argument (2 given)
>> add new element at last always, if this new element is any sequence than the sequence will get added to list as last element
>> it increase the of list by one always

2-l.extend(l1)
>> accept only one argument at one time and that argument should be a seqence(i.e list, tuple, string)
>> add the element of l1 into l, means element of l1 would sit in l from the end position.
>> it accepts only sequence as argument.

IMP:-
		l=[1,2]
		t=(3,4)
		s={5,6}
		d={1001:'a',1002:'b'}
		l.extend(t)
			>>l=[1,2,3,4]
		l.extend(s)
			>>l=[1,2,3,4,5,6]
		l.extend(d)
			>>l=[1,2,3,4,5,6,1001,1002]  >> only key will get added to the list not the values

## way to reverse ele of a list

1-l.reverse()
>> list specific method
>> make change on the same element
>> it always return list

2- reversed(l)
>> python commom method
>> it always creates seperate object
>> it returns a generator


### way of sorting the list

1-l.sort()
>>list specific function
>> always affect the main object
>> always return list

2-sorted(l)
>> python inbuilt method
>> return a sorted list
>> always creates a new object

### way to delete element from the list
1- del l[index]
2- l.remove(ele)   --- remove only first appeared element
3- l.pop   ------------remove one element randomly and also return it
4- l.pop(index)  ----- remove and return the element present in the specified index which is now got deleted
5- del l    -----------will the complete list

### + / * operation on list

1- concatination(+)
>> join two list
>> always creates a seperate object
>> we can concatinate more than two list ---- which is not possible by any other method

	     extend															concatination
	> affect same list			    								>create separate list
	> argument sequence canbe of any datatype						>in this all must be of same type
	> it adds only one sequence to list at one time					> it can adds only many sequence(only list) to list at one time

>> on + diff datatypes = TypeError: can only concatenate list (not "tuple") to list

2-Repetition(*)
>> used for repetition of element
>> int is necessary to give.
>> it also creates separate object


### comparition of list
1-cmp(l1,l2)
>> principle - it compare two sequence element by element
	eg.l=[1,1000]
		l1=[1,2,4,4,5]

		cmp(l,l1)
		>>1

		l>11
		>>True

>> return 1 when l1>l2
>> return 0 when l1==l2
>> return -1 when l1<l2

2- l1>l2, l1<l2, l1==l2 >>>> return True/False
>> principle - it compare two sequence element by element


### Program

### WAP to take a list and remove the dublicates from the list     ----- making loop of only one list
#l=[10,50,50,100,100,100,20,30,40,20,30,90,40]
l=input('enter a list:')
for i in l:
    n=l.count(i)
    if n>1:
        l.reverse()
        for j in range(1,n):
            l.remove(i)
        l.reverse()
    else: continue
l.sort()
print'updated list:{}'.format(l)

# #expected output
# #enter a list:[10,50,50,100,100,100,20,30,40,20,30,90,40]
# #updated list:[10, 20, 30, 40, 50, 90, 100]


'''

