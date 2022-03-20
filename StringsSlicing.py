
msg='welcome to Python 101: Strings'
print(msg*2)
print(msg,msg)
print(msg.upper())
print(msg.lower())
print(msg.capitalize())

print(len(msg))
print(msg.count('Python'))

print(msg[0])
print(msg[-3])

#after 2nd position
print(msg[2:])

#up to 6th position
print(msg[:7])

msg='welcome to Python 101: Strings'
msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]  
print(msg1.title())
#print backwards
print(msg1[::-1].title())
