name= input('What is your name?: ')
print(name)

name= input('What is your name?: ')
age=input('What is your age?: ')
print('Hello '+ name + '! You are '+ age + ' years old.')

#simple calculator

num1=input('Enter a digit: ')
num2=input('Enter a second number:')
answer=num1+num2
print(answer)

# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name


first_name = input('Enter your first name')
distance_km =input('Enter your distance in km')
#convert distance to miles
distance_miles = float(distance) /1.609

print('Hello '+ first_name.capitalize() + '. Your distance is ' + distance_km + ' km' + ' or ' + str(distance_miles)+ ' miles.')
print(f'Hello {name.title()}. Your distance is {distance_km}km or {distance_miles} miles.')
