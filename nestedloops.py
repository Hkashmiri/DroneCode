Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
a = ['hello','goodbye','salute']
a[2]
'salute'
a[2][0]
's'
#it can give you the letters of the string
a[::-1]
['salute', 'goodbye', 'hello']
a[::-1][::-1]
['hello', 'goodbye', 'salute']
a[::-1][:-1:-1]
[]
a[::-1][-1::1]
['hello']
a[::-1][-1::]
['hello']
a[::-1][::-1][::-1][::-1]
['hello', 'goodbye', 'salute']
a[::-1][-1:-1:-1]
[]
b = [[4,5,6],[7,9,3,4],[1,2,3]]
b[2]
[1, 2, 3]
b[2][2]
3
b[2][2]=-1
b
[[4, 5, 6], [7, 9, 3, 4], [1, 2, -1]]
a[::-1][::-1]
['hello', 'goodbye', 'salute']
a[::-1][::-2]
['hello', 'salute']
c='abcd'
c[::-1]
'dcba'
firstelement = 'salute'
secondelement = 'goodbye'
thirdelement = 'hello'
firstelement[::-1]
'etulas'
firstelement[::-1]secondelement[::-1]
SyntaxError: invalid syntax
firstelement[::-1], secondelement[::-1]
('etulas', 'eybdoog')
firstelement[::-1], secondelement[::-1], thirdelement[::-1]
('etulas', 'eybdoog', 'olleh')
[s[::-1] for s in a[::-1]]
['etulas', 'eybdoog', 'olleh']
myList = ['color', (5,7), [10,['red','while']], (True,False),'exam']
myList[1][1]
SyntaxError: multiple statements found while compiling a single statement
myList[1][2]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    myList[1][2]
NameError: name 'myList' is not defined
myList = ['color', (5,7), [10,['red','while']], (True,False),'exam']
myList[1][1]
SyntaxError: multiple statements found while compiling a single statement
myList = ['color', (5,7), [10,['red','while']], (True,False),'exam']
myList[1][1]
7
myList[2][1][0]
'red'
myList[0][::-1]
'roloc'
myList[0][::-2]
'rlc'
myList[2][1][0][::-1]
'der'
apple = myList[2][1]
strawberry, turkey = myList[2][1]
strawberry
'red'
turkey
'while'
# You can assign 2 values in a list to two variables but you cannot assign 3 variables to 2 values in a list.
str(123)
'123'

list(123)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
>>>     list(123)
TypeError: 'int' object is not iterable
>>> list('123')
['1', '2', '3']
str['1', '2', '3']
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
>>>     str['1', '2', '3']
TypeError: type 'str' is not subscriptable
>>> ''.join(['1', '2', '3'])
>>> '123'
s = 'hello'
s[0]='j'
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
>>>     s[0]='j'
TypeError: 'str' object does not support item assignment
>>> list(s)
['h', 'e', 'l', 'l', 'o']
s[0]=j
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
>>>     s[0]=j
NameError: name 'j' is not defined
s[0]='j'
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
>>>     s[0]='j'
TypeError: 'str' object does not support item assignment
>>> list(s[0])='j'
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
>>> list(s[0])=='j'
>>> False
>>> abc = list(s)
abc[0]='j'
>>> print(abc)
['j', 'e', 'l', 'l', 'o']
>>> ''.join(['j', 'e', 'l', 'l', 'o'])
'jello'
>>> ''.join(['j' if i == 'h' else i for i in list(s)])
>>> 'jello'
del myList[2][1]
>>> print myList
SyntaxError: incomplete input
>>> print(myList)
['color', (5, 7), [10], (True, False), 'exam']
>>> ['color', (5, 7), [10], (True, False), 'exam']
>>> ['color', (5, 7), [10], (True, False), 'exam']
>>> 

x=[nothing]
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
>>>     x=[nothing]
NameError: name 'nothing' is not defined
>>> [x*x for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> [x*x for x in range(10) if x % 3 == 0]
[0, 9, 36, 81]
>>> [a+b for a in list('hi') for b in list('hi')]
['hh', 'hi', 'ih', 'ii']
>>> ['1'+'2'+'3' for '1' in list('1,2,3') for 2 in list('1,2,3')]
SyntaxError: cannot assign to literal
>>> ['1'+'2'+'3' for i in list('1,2,3') for j in list('1,2,3')]
['123', '123', '123', '123', '123', '123', '123', '123', '123', '123', '123', '123', '123', '123', '123', '123', '123', '123', '123', '123', '123', '123', '123', '123', '123']
