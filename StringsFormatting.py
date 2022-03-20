msg='Welcome to Python 101: Strings'
#output give the position of the sliced character(s)
print(msg.find('Python'))
msg=msg.replace('Python','C')
print(msg)

#check character(s)(result is a boolean) if its inside string
print('Python' not in msg)
print('Python' in msg)

name='TERRY'
color = 'RED'
msg = '[' + name + '] loves the color ' + color.lower() + '!'
msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
print(msg)
print(msg1)
