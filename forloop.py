aString = 'Hello'
for ch in aString:
    print(ch,end = ',')
    

print(len(aString))
print(aString[-1])

i = 0
length = len(aString)
while i < length:
    print('Unicode representation of', aString[i], 'is', ord(aString[i]))
    i += 1

for i in range(10):
    if(i==9):
        print(i)
    else:
        print(str(i),end=",")

aStr = 'Hello'
