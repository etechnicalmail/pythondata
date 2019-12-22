Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d1 = {'a':1, 'b':2, 'c':3}
>>> dir(d1)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> l1 = [2,3,4]
>>> l1[0]
2
>>> d1['a']
1
>>> d1['d']
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    d1['d']
KeyError: 'd'
>>> d1.get('a')
1
>>> d1.get('d')
>>> d1.get('a', 0)
1
>>> d1.get('d', 0)
0
>>> d1.item()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    d1.item()
AttributeError: 'dict' object has no attribute 'item'
>>> d1.items()
dict_items([('a', 1), ('b', 2), ('c', 3)])
>>> d1.keys()
dict_keys(['a', 'b', 'c'])
>>> d1.values()
dict_values([1, 2, 3])
>>> d1.pop()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d1.pop()
TypeError: pop expected at least 1 arguments, got 0
>>> d1.pop('a')
1
>>> d1.pop({'b':2})
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    d1.pop({'b':2})
TypeError: unhashable type: 'dict'
>>> d1.popitem({'b':2})
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d1.popitem({'b':2})
TypeError: popitem() takes no arguments (1 given)
>>> help(d1.popitem)
Help on built-in function popitem:

popitem(...) method of builtins.dict instance
    D.popitem() -> (k, v), remove and return some (key, value) pair as a
    2-tuple; but raise KeyError if D is empty.

>>> d1.popitem()
('c', 3)
>>> d1
{'b': 2}
>>> d1['a'] = 1
>>> d1
{'b': 2, 'a': 1}
>>> d2 = {'x':24, 'y':25}
>>> d1.update(d2)
>>> d1
{'b': 2, 'a': 1, 'x': 24, 'y': 25}
>>> d1['dict'] = d2
>>> d1
{'b': 2, 'a': 1, 'x': 24, 'y': 25, 'dict': {'x': 24, 'y': 25}}
>>> d1['dict']
{'x': 24, 'y': 25}
>>> d1['dict']['y']
25
>>> l1 = [['p', 'q'], {15:'l', 16:'m'}]
>>> d1[a] = l1
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    d1[a] = l1
NameError: name 'a' is not defined
>>> d1['a'] = l1
>>> d1
{'b': 2, 'a': [['p', 'q'], {15: 'l', 16: 'm'}], 'x': 24, 'y': 25, 'dict': {'x': 24, 'y': 25}}
>>> d1['a'][1]
{15: 'l', 16: 'm'}
>>> d1['a'][0][1]
'q'
>>> d1['a'][1][16] = 'n'
>>> d1
{'b': 2, 'a': [['p', 'q'], {15: 'l', 16: 'n'}], 'x': 24, 'y': 25, 'dict': {'x': 24, 'y': 25}}
>>> d1['a'][1]
{15: 'l', 16: 'n'}
>>> d1['a'][1].update(d1['dict'])
>>> d1
{'b': 2, 'a': [['p', 'q'], {15: 'l', 16: 'n', 'x': 24, 'y': 25}], 'x': 24, 'y': 25, 'dict': {'x': 24, 'y': 25}}
>>> d1['a'].append(d1['dict'])
>>> d1
{'b': 2, 'a': [['p', 'q'], {15: 'l', 16: 'n', 'x': 24, 'y': 25}, {'x': 24, 'y': 25}], 'x': 24, 'y': 25, 'dict': {'x': 24, 'y': 25}}
>>> d1['a']
[['p', 'q'], {15: 'l', 16: 'n', 'x': 24, 'y': 25}, {'x': 24, 'y': 25}]
>>> d1['a'][1]
{15: 'l', 16: 'n', 'x': 24, 'y': 25}
>>> d1['a'][1]['dict']=d1['dict']
>>> d1
{'b': 2, 'a': [['p', 'q'], {15: 'l', 16: 'n', 'x': 24, 'y': 25, 'dict': {'x': 24, 'y': 25}}, {'x': 24, 'y': 25}], 'x': 24, 'y': 25, 'dict': {'x': 24, 'y': 25}}
>>> dir(d1)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> help(d1.fromkeys)
Help on built-in function fromkeys:

fromkeys(iterable, value=None, /) method of builtins.type instance
    Create a new dictionary with keys from iterable and values set to value.

>>> d2 = dict()
>>> d2.fromkeys(['a','b'],0)
{'a': 0, 'b': 0}
>>> help(d2.setdefault)
Help on built-in function setdefault:

setdefault(key, default=None, /) method of builtins.dict instance
    Insert key with a value of default if key is not in the dictionary.
    
    Return the value for key if key is in the dictionary, else default.

>>> d1.setdefault('c', 3)
3
>>> d1.setdefault('a', 3)
[['p', 'q'], {15: 'l', 16: 'n', 'x': 24, 'y': 25, 'dict': {'x': 24, 'y': 25}}, {'x': 24, 'y': 25}]
>>> d1.clear()
>>> d1
{}
>>> t1 = (2,3,4,5)
>>> dir(t1)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> t1.index(4)
2
>>> t1.index(45)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    t1.index(45)
ValueError: tuple.index(x): x not in tuple
>>> days = ['']
>>> s1 = {2,3,4,5}
>>> s1 = {2,3,1,6}
>>> s2 = {1,6,4,5,7,8}
>>> s3 = {7,8}
>>> dir(s1)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> s1.intersection(s2)
{1, 6}
>>> s2.intersection(s1)
{1, 6}
>>> s1.difference(s2)
{2, 3}
>>> s2.difference(s1)
{8, 4, 5, 7}
>>> s1.intersection(s3)
set()
>>> s1.union(s2)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> s1.union(s3)
{1, 2, 3, 6, 7, 8}
>>> s1.issubset(s2)
False
>>> s3.issubset(s2)
True
>>> s2.issuperset(s3)
True
>>> s1.diffrence_update(s2)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    s1.diffrence_update(s2)
AttributeError: 'set' object has no attribute 'diffrence_update'
>>> s1.difference_update(s2)
>>> s1
{2, 3}
>>> s2
{1, 4, 5, 6, 7, 8}
>>> s1.intersection(s2)
set()
>>> s1 = {1,2,3,6}
>>> s1.symmetric_diffrenece(s2)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    s1.symmetric_diffrenece(s2)
AttributeError: 'set' object has no attribute 'symmetric_diffrenece'
>>> s1.symetric_diffrenece(s2)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    s1.symetric_diffrenece(s2)
AttributeError: 'set' object has no attribute 'symetric_diffrenece'
>>> s1.symmetric_difference(s2)
{2, 3, 4, 5, 7, 8}
>>> s1.symmetric_difference_update(s2)
>>> s1
{2, 3, 4, 5, 7, 8}
>>> list = [1,2,2,3,3,4,3]
>>> l1 = [1,2,2,3,3,4,3]
>>> s5 = set(l1)
>>> s5
{1, 2, 3, 4}
>>> list(s5)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    list(s5)
TypeError: 'list' object is not callable
>>> fs1 = frozenset(s1)
>>> fs1
frozenset({2, 3, 4, 5, 7, 8})
>>> dir(fs1)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']
>>> range(5)
range(0, 5)
>>> 
=============================== RESTART: Shell ===============================
>>> range(5)
range(0, 5)
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> list(range(1,101))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
>>> list(range(1,101,2))
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> list(range(5,51,5))
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
>>> list(range(5,51,-5))
[]
>>> list(range(51,5,-5))
[51, 46, 41, 36, 31, 26, 21, 16, 11, 6]
>>> list(range(50,4,-5))
[50, 45, 40, 35, 30, 25, 20, 15, 10, 5]
>>> list(range(50,5,-5))
[50, 45, 40, 35, 30, 25, 20, 15, 10]
>>> list(range(50,4,-5))
[50, 45, 40, 35, 30, 25, 20, 15, 10, 5]
>>> b = True
>>> c = False
>>> d = 1
>>> b == d
True
>>> e = 0
>>> e == c
True
>>> e is c
False
>>> f = 15
>>> f == b
False
>>> if f:
	print("hello")

	
hello
>>> if e:
	print("hello")

	
>>> l1 = [32, 5]
>>> if l1:
	print("hello")

	
hello
>>> l1 = []
>>> if l1:
	print("hello")

	
>>> s1 = ""
>>> if s1:
	print("hello")

	
>>> a = True
>>> dir(a)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> help(a.numerator)
Help on int object:

class int(object)
 |  int([x]) -> integer
 |  int(x, base=10) -> integer
 |  
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is a number, return x.__int__().  For floating point
 |  numbers, this truncates towards zero.
 |  
 |  If x is not a number or if base is given, then x must be a string,
 |  bytes, or bytearray instance representing an integer literal in the
 |  given base.  The literal can be preceded by '+' or '-' and be surrounded
 |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
 |  Base 0 means to interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
 |  
 |  Methods defined here:
 |  
 |  __abs__(self, /)
 |      abs(self)
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __and__(self, value, /)
 |      Return self&value.
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __ceil__(...)
 |      Ceiling of an Integral returns itself.
 |  
 |  __divmod__(self, value, /)
 |      Return divmod(self, value).
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __float__(self, /)
 |      float(self)
 |  
 |  __floor__(...)
 |      Flooring an Integral returns itself.
 |  
 |  __floordiv__(self, value, /)
 |      Return self//value.
 |  
 |  __format__(self, format_spec, /)
 |      Default object formatter.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getnewargs__(self, /)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __index__(self, /)
 |      Return self converted to an integer, if self is suitable for use as an index into a list.
 |  
 |  __int__(self, /)
 |      int(self)
 |  
 |  __invert__(self, /)
 |      ~self
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __lshift__(self, value, /)
 |      Return self<<value.
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __neg__(self, /)
 |      -self
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __pos__(self, /)
 |      +self
 |  
 |  __pow__(self, value, mod=None, /)
 |      Return pow(self, value, mod).
 |  
 |  __radd__(self, value, /)
 |      Return value+self.
 |  
 |  __rand__(self, value, /)
 |      Return value&self.
 |  
 |  __rdivmod__(self, value, /)
 |      Return divmod(value, self).
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rfloordiv__(self, value, /)
 |      Return value//self.
 |  
 |  __rlshift__(self, value, /)
 |      Return value<<self.
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __round__(...)
 |      Rounding an Integral returns itself.
 |      Rounding with an ndigits argument also returns an integer.
 |  
 |  __rpow__(self, value, mod=None, /)
 |      Return pow(value, self, mod).
 |  
 |  __rrshift__(self, value, /)
 |      Return value>>self.
 |  
 |  __rshift__(self, value, /)
 |      Return self>>value.
 |  
 |  __rsub__(self, value, /)
 |      Return value-self.
 |  
 |  __rtruediv__(self, value, /)
 |      Return value/self.
 |  
 |  __rxor__(self, value, /)
 |      Return value^self.
 |  
 |  __sizeof__(self, /)
 |      Returns size in memory, in bytes.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  __sub__(self, value, /)
 |      Return self-value.
 |  
 |  __truediv__(self, value, /)
 |      Return self/value.
 |  
 |  __trunc__(...)
 |      Truncating an Integral returns itself.
 |  
 |  __xor__(self, value, /)
 |      Return self^value.
 |  
 |  bit_length(self, /)
 |      Number of bits necessary to represent self in binary.
 |      
 |      >>> bin(37)
 |      '0b100101'
 |      >>> (37).bit_length()
 |      6
 |  
 |  conjugate(...)
 |      Returns self, the complex conjugate of any int.
 |  
 |  to_bytes(self, /, length, byteorder, *, signed=False)
 |      Return an array of bytes representing an integer.
 |      
 |      length
 |        Length of bytes object to use.  An OverflowError is raised if the
 |        integer is not representable with the given number of bytes.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        `sys.byteorder' as the byte order value.
 |      signed
 |        Determines whether two's complement is used to represent the integer.
 |        If signed is False and a negative integer is given, an OverflowError
 |        is raised.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  from_bytes(bytes, byteorder, *, signed=False) from builtins.type
 |      Return the integer represented by the given array of bytes.
 |      
 |      bytes
 |        Holds the array of bytes to convert.  The argument must either
 |        support the buffer protocol or be an iterable object producing bytes.
 |        Bytes and bytearray are examples of built-in objects that support the
 |        buffer protocol.
 |      byteorder
 |        The byte order used to represent the integer.  If byteorder is 'big',
 |        the most significant byte is at the beginning of the byte array.  If
 |        byteorder is 'little', the most significant byte is at the end of the
 |        byte array.  To request the native byte order of the host system, use
 |        `sys.byteorder' as the byte order value.
 |      signed
 |        Indicates whether two's complement is used to represent the integer.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  denominator
 |      the denominator of a rational number in lowest terms
 |  
 |  imag
 |      the imaginary part of a complex number
 |  
 |  numerator
 |      the numerator of a rational number in lowest terms
 |  
 |  real
 |      the real part of a complex number

>>> l1 = [2,3,4]
>>> s1 = set(l1)
>>> s1
{2, 3, 4}
>>> l2 = list(s1)
>>> l2
[2, 3, 4]
>>> a = 7
>>> str(a)
'7'
>>> int('1234')
1234
>>> int('1234sdfds')
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    int('1234sdfds')
ValueError: invalid literal for int() with base 10: '1234sdfds'
>>> a = 7
>>> float(a)
7.0
>>> a = 7.5
>>> int(a)
7
>>> a = 7
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
>>> a = '12345'
>>> list(a)
['1', '2', '3', '4', '5']
>>> l2 = list(a)
>>> str(l2)
"['1', '2', '3', '4', '5']"
>>> "".join(l2)
'12345'
>>> "###".join(l2)
'1###2###3###4###5'
>>> l3 = [1,2,[3,4]]
>>> str(l3)
'[1, 2, [3, 4]]'
>>> 
>>> l2
['1', '2', '3', '4', '5']
>>> dict(l2)
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    dict(l2)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> enumerate(l2)
<enumerate object at 0x00000079923E43B8>
>>> dict(enumerate(l2))
{0: '1', 1: '2', 2: '3', 3: '4', 4: '5'}
>>> list(enumerate(l2))
[(0, '1'), (1, '2'), (2, '3'), (3, '4'), (4, '5')]
>>> dict(enumerate(l2)).items()
dict_items([(0, '1'), (1, '2'), (2, '3'), (3, '4'), (4, '5')])
>>> 
