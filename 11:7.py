s = ""
for c in ['J', 'a', 'n', 'e']:
    s = c + s
print(s)

s = 0
for x in range(5,10):
    s = s + x
print(s)

n = 0
for i in range(1,11):
    n = n + (i % 2)
print(n)

print(3%2)

name = "Alice"
age = 30
message = "My name is %s, and I am %d years old." % (name, age)
print(message)


def pattern(height):
    for i in range(height):
        print('*'*9)


pattern(10)

def pattern(height, width):
    for i in range(height):
        print('*'*width)


pattern(1000,200)
