Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================================================================ RESTART: /Users/hkashmiri23/Documents/comp sci freshman year/11:16:23.py ================================================================
2
>>> aString = "Phantom opera"
>>> aString
'Phantom opera'
>>> aString[3:4]
'n'
>>> aString[3:4],[3:4]
SyntaxError: invalid syntax
>>> aString[0,1]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    aString[0,1]
TypeError: string indices must be integers, not 'tuple'
>>> aString[0:1]
'P'
>>> aString[1:2]
'h'

>>> aString[1:13:1]
'hantom opera'
>>> aString[1:6:2]
'hno'
>>> aString[1:6:-2]
''
>>> aString[6:1:2]
''
>>> aString[6:1:-2]
'mta'
>>> aString[5:2:-2]
'on'
>>> aString[5:1:-2]
'on'
>>> aString[5:1:-1]
'otna'
>>> aString[5:0:-2]
'onh'
>>> aString[0:13:-1]
''
>>> aString[-1:13:-1]
''
>>> aString[0:-1]
'Phantom oper'
>>> aString[-1::-1]
'arepo motnahP'
>>> aString[::-1]
'arepo motnahP'
