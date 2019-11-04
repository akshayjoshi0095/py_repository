
'''
>not mutable
>insertion order is preserved but not in case of set and dictionary
>non dynamic in nature
>dublicates
>heterogenous

Note - count() , len() are two func where counting starts from 1 not from zero

IMP-
1-way of creating tuple with only one element
>> t=(ele,)
    >> if We donot give this , then system will consider it as int instead of tuple

2-1-way of creating an empty tuple
>> t=()

3- while comparision, system always consider tuple greater then list
>> t=(0,)
   l=[11,12,13]

   cmp(t,l)         l>t
   >>1              >>False


## Imp function
# >>>len(l) --- returns length of tuple
# >>>l.count(element)   ---- return no. of type a particular element present in the tuple,
# >>>l.index(ele)  ---------	return the very 1st index at which particular element is present, system consider this index from 0
# >>> unpacking and packing is possible
# >>> member operator is applicable i.e in operator


##Not applicable in tuple
t.insert(index,value)
t[i]=value -- updation of element is not allowed
t.append()
t.extend()

del l[index]
l.remove(ele)   --- remove only first appeared element
l.pop   ------------remove one element randomly and also return it
l.pop(index)  ----- remove and return the element present in the specified index which is now got deleted


## way to reverse ele of a tuple

2- reversed(t)
>> python commom method
>> it always creates seperate object
>> it returns a generator


### way of sorting the tuple

2-sorted(t)
>> python inbuilt method
>> always return a sorted tuple, even if applied for datatype other then tuple.
>> always creates a new object


## mathmatical operation

1- concatination(+)
>> join two tuple
>> always creates a seperate object
>> we can concatinate more than two tuple ---- which is not possible by any other method

>> on + diff datatypes = TypeError: can only concatenate tuple (not "tuple") to tuple


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





'''











































