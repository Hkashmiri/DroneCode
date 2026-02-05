Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> firstName = input("Enter your name")
Enter your name hafsah
>>> print firstName
SyntaxError: incomplete input
>>> print(firstName)
 hafsah
>>> hafsah
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    hafsah
NameError: name 'hafsah' is not defined. Did you mean: 'hash'?
>>> 
>>> lastName = input("Enter your last name ")
Enter your last name kashmiri
>>> print(lastName)
kashmiri
>>> print (firstName + lastName)
 hafsahkashmiri
>>> print (firstName + " "+ lastName)
 hafsah kashmiri
>>> type(hafsah kashmiri)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> type(lastName)
<class 'str'>
>>> 
>>> radius = input("Enter a radius: ")
Enter a radius: 4
>>> print radius
SyntaxError: incomplete input
>>> print(radius)
4
>>> area = 3.14
>>> area = 3.14*radius**2
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    area = 3.14*radius**2
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> area = 3.14*(radius*radius)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    area = 3.14*(radius*radius)
TypeError: can't multiply sequence by non-int of type 'str'
>>> TypeError: can't multiply sequence by non-int of type 'str'
SyntaxError: unterminated string literal (detected at line 1)
>>> area=3.14*float(radius)**2
>>> print("Area=" area)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(area)
50.24
>>> input.math
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    input.math
AttributeError: 'builtin_function_or_method' object has no attribute 'math'
>>> math.pi
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    math.pi
NameError: name 'math' is not defined
