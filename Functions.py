def greeting(name):
    print("Hello " + name + "!")
    
greeting("Brian")

def greeting(name,age):
    print("Hello " + name + ",you are " + age + "!")
    
greeting("Brian","32")


def greeting(name,age=28):
    print("Hello " + name + ", you are " + str(age) + "!")
    print(f"Hello {name}, you are {age}!")

name = input("Enter your name: ")    
greeting(name,32)
greeting("Judith")

#named functions
def greeting(name, age=28, color="red"):
 #Greets user with “name” from “input box” and “age”, if unavailable, default age is used   
   
   print(f"Hello {name.capitalize()}, you will be {age+1} next birthday!")
   print(f"We hear you like the color {color.lower()}!")

greeting(age=27, name="brian",color="Blue")

Profile(yob=1995,weight=83.5,height=192,eye_color="blue")
