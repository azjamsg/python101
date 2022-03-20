a = 7
b = 3
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

print('o' in 'John')
print('o' not in 'John')

a = [3,7,42]
b = [3,7,42]
print(a == b)
print(a is b) # false not in same memory space
print(id(a), id(b))
