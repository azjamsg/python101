friends = ['John','Michael','Terry','Eric','Graham']
print(friends)

#print the second friend's name
print(friends[1])

print(friends[1],friends[4])
print(friends[2:4])

#find number of elements in list
print(len(friends))

print(friends.index('Eric'))

#count instances of element in list
print(friends.count('Eric'))

friends = ['John','Michael','Terry','Eric','Graham']
cars = [911,130,328,535,740,308]
print(friends)
friends.sort()
print(friends)
# sort in reverse order
friends.sort(reverse=True)
print(friends)
# print in reverse 
friends.reverse()
print(friends)

print(min(cars))
print(max(cars))

friends.append('TerryG')

#insert in index 1
friends.insert(1,'TerryG')

#extend list
friends.extend(cars)

friends.remove('Terry')

#pop last element
friends.pop()

#copy list
new_friends = friends[:] #only copy memory position
new_friends = friends.copy
new_friends = list(friends)
