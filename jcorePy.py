 ******formating
 ******decorator 
 ******higher order function
 ******comprehension

 ******tuple>array>list>set>dictionary

 ======
 ***array--numpy array can contain same or different 
 dtype ordered elements. it is mutable means it can be 
 modified. elements can duplicate

 ======
 ***list--it can contain different dtype ordered elements.
 it is mutable. elements can duplicate

 ======
 ***tuple--it can contain different dtype ordered elements.
 it is immutable means it's elements can't be modified.
 elements can duplicate

 =======
 ***set--contain different dtype unordered elements and it is
 mutable. duplication not allow. because of unordered collection
 of elements we can't access it's elements using index.

 ***dictionary--it contain key value pair. unordered collection
 of elements & mutable. key can't ducplicate but values can.

 ===========================================================
 ------------store group of elements of same dtype----------
 ===========================================================
 =========array -- pop=========
 array_name.pop() used to remove last elements of array and aslo specified postition

 ==========array -- remove=======
 array_name.remove() parameter will be the value of array elements

 ==========array -- index=======
 array_name.index()  it will return the postition of array elements

 ==========array -- reverse=======
 array_name.reverse() it will reverse the direction

 ==========array -- insert=======
 array_name.insert(index, elements)

 ==========array --extend=========
 arr.extend(new_array)
 #extend array and iterable object


 ==================================================
 ---------------------numpy------------------------
 ==================================================
 ============array --slicing================
 b=a[start:stop:stepsize, start:stop:stepsize]


 ============array -- linspace===========
 from numpy import *
 my_arr = linspace(start,end,num=50, dtype=)

 ===========array -- logspace==========
 from numpy import *
 my_arr = logspace(start, stop, num=50, endpoint=True, 
     base=10.0, dtype=None, axis=0)

 ===========array -- arange==========
 #it work like range. stop count less 1
 my_arr = arange(start, stop, stepsize, dtype=None)

 ============array -- zeros===========
 zeros(5, dtype=int)
 zeros((3,2), dtype=)


 ============array -- one===========
 ones(5, dtype=int)
 ones((3,2), dtype=)

 ===========array -- any()/all()==========
 a = array([101,102,103,104,105])
 b = array([1,2,3,4,5])
 c = a(comprision operator)

 # if one is true any() return true
 # if all true all() retuen true

 =============array -- where()=============
 from numpy import *

 a = array([101,102,103,104,105])
 b = array([1,299,399,4,5])
 c = where(a>b, a, b)
 print(c)


 =========array -- nonzero===========
 a = nonzero(my_arr)

 # a return index of the elements which are not  zero

 =================array -- view()=============
 b=my_arr.view()
 #it will create different memory location but if we change
 something in b it will affect original array

 =================array -- copy()=============
 from numpy import *

 a = array([101,102,103,104,105])
 b = copy(a)
 # a and b are same but independent

 =================array -- reshape()============
 reshape(my_arr, (for3d num of array, rows, column))

 =================array -- flatten()============
 it convert 1d from 3d,2d
 my_arr.flatten()


 ===============array -- 2d array slicing=============
 b=a[start:stpp:stepsize, start:stpp:stepsize]


 ============array -- attribute of numpy array========
 # my_arr.ndim it represents dimension of array
 # my_arr.shape it represents the shape
 # my_arr.size it represents how much elements in this array
 # my_arr.itemsize it represents the size of array in bytes
 # my_arr.nbytes it represents total num of bytes



 ====================formating  /f-string=================
 index/key/name:[fill][align][sign][\#][0][width][,][.precision]type

 f'{b:-^+8,.2f}'

 https://www.youtube.com/watch?v=kr7PzMGgq68&list=PLbGui_ZYuhigZkqrHbI_ZkPBrIr5Rsd5L&index=94

 time: 40.00


 =====================string====================
 str.upper() #uppercase all str
 str.lower() #lowercase all str
 str.swapcase() #if upper do lower or lower do upper
 str.title() #uppercase all word first alphabet
 str.isupper() #if all upper return true
 str.islower() #if all lower return true
 str.istitle() #if all word first is upper return true
 str.isdigit() #if all are digit return true
 str.isalpha() #if all alphabet return true
 str.isalnum() #if all alphabet & num return true
 str.isspace() #if string is space it retuen true
 str.lstrip() #it remove left side space
 str.rstrip() #it remove right side space
 str.strip() #it remove both side space
 str.replace('old', 'new')
 str.split('seperate')
 ' '.join('tuple') #need to pass tuple
 str.startswith('specified string')
 str.endswith('specified string')

 ====================recursion===================
 import sys
 sys.setrecursionlimit(2000)
 print(sys.getrecursionlimit())
 i = 0
 def show():
     global i
     i=i+1
     print('mahfuz', i)
     show()
 show()

 ====================function decorator===============
 def decor1(fun):
     def inner():
         a=fun()
         mul = a*5
         return mul
     return inner

 def decor2(num):
     def inner():
         a=num()
         add=a+15
         return add
     return inner

 @decor2
 @decor1
 def num():
     return 10

 print(num())
 ====================================================
 ====================higher order function===========
 ====================================================
 ===============filter, map, reduce==================
 a=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

 b=list(filter(lambda n: n%2==0,a))
 print(b)

 c=list(map(lambda n: n+99, b))
 print(c)

 from functools import reduce
 d=reduce(lambda n,m: n+m, c)
 print(d)










 =======================filter function===============
 x = ['a', 'b', 'c', 'd','e','f','g','h']
 y = ['a', 'b', 'c', 'h']
 def high_marks(n):
     if n in x:
         return True
 b = filter(high_marks, y)
 for c in b:
     print(c)
 //////////////////////
 x = ['a', 'b', 'c', 'd','e','f','g','h']
 y = ['a', 'b', 'c', 'h']
 b = filter(lambda n: n in x, y)
 for c in b:
     print(c)

 =====================map function=================
 a=[10,20,30,40]
 b=[50,60,70,80]

 b=list(map(lambda a,b:(a+b,a-b),a,b))
 print(b)

 =====================reduce function==============
 from functools import *
 a=[10,20,30,40]

 b=reduce(lambda n,m:n+m,a)
 print(b)


 =======================generator function================
 def my_fun(a,b):
     while a<=b:
         yield a
         a+=1

 result=my_fun(1,5)

 print(next(result))
 print(next(result))

 print('-------after next function--------')

 for a in result:
     print(a)

 =====================================================
 ===============list//mutable//ordered================
 =====================================================
 lst.insert(expected index,elements)
 lst.pop() #it remove last elements of list & return it
 lst.pop(target index) #it remove elements given index & return it
 lst.remove(elements) #it remove given elements
 lst.index(elements) #it return given elements index
 lst1.extend(lst2) #it add two list
 ==lst.count(elements) #how many time this elements in lst
 str.sort() #it sort integer ascending order
 lst.clear() #all clear
 a=lst.copy() #create a independent copy
 a=lst[:] #create a independent copy
 ==================================
 ===============slicing nested list
 a=lst[start,stop,stepsize][index][start,stop,stepsize]
 a=[[10,20,30,40],
    [50,60,70,80],
    [90,100,110,120]]

 b=a[0:1]
 n=len(b)
 for i in range(n):
     b=a[0:2][i][1:]
     print(b)





 ==========list comprehension
 a1=[0,1,2,3,4]
 a2=[i+1 for i in a1]
 print(a2)
 ============
 a1=[0,1,2,3,4]
 a2=[i for i in range(20) if i%2==0]
 print(a2)
 ============
 a1=[0,1,2,3,4]
 a2=[i for i in range(20) if i%2==0 if i%3==0]
 print(a2)
 ============
 a2=[i if i%2==0 else "invalid" for i in range(10)]
 print(a2)
 ===============
 #nested list comprehension
 lst = [i*j for i in range(3) for j in range(3)]

 =======================================================
 ==================tuple/immutable/ordered==============
 =======================================================
 #we can delete or add tuple using slicing


 ========================================================
 ================set//mutable//unordered=================
 ========================================================

 a.update() #it add multiple elements, also can take tuple,list
 a.add() #it add elements set
 a.remove() #it remove given items if not found return error
 a.discard() #it remove given items if not found no error shows
 a.copy() #create a independent copy
 a.clear() #it clear all elements
 a.intersection(b) #it return common elements of 2 set
 a.union(b) #it return both sets all elements without repeating
 a.difference(b) #it return 1st set elements which are not exist on 2nd set
 a.issubset(b) #if all elements of 1st is in 2nd return true
 a.issuperset(b) #if 2nd set all elements are in 1st return true
 ====================
 ========set comprehension
 ====================
 a=set(range(20))
 b={i+1 for i in a}
 print(b)
 ===================
 b={i+1 for i in range(10)}
 print(b)
 ====================
 #if else set comprehension
 b = {i if i%2==0 else i*55 for i in range(20)}
 print(b)
 =====================
 st = {i*j for i in range(3) for j in range(3)}

 ========================================================
 =====================dictionary=========================
 ========================================================
 keys=[10,20,30,40]
 values=['mahfuz','rahman','bappi','anam']
 a=dict(zip(keys,values))


 a.clear() #it delete all elements without dictionary
 del a #it delete dictionary
 del a[] #it delete specific elements
 print('a' in a) #if 'a' in dict it return true
 a.copy() #it create independent copy of dicationary
 a.get(key,defaultvalue) #if the key is available then 
     return the value & not available return the defaultvalue
 a.items() #return an object that contains key-value pair as tuple
 a.keys() #it return all keys in dict key object
 a.values() #it rreturn all the values of dict.
 a.update({'e':70}) #adding elements
 a.pop(key, defalutvalue) #remove given key ,value & return
 a.popitem() #it remove last inserted of dict and return this
 a.setdefault(key,value) #if key found it return the value
                 else it will add the key ,value & return

 ======================
 ======dict comprehension
 =====================
