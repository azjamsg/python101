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
