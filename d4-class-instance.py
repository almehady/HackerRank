class Person:
    # Add some more code to run some checks on initial_age
    def __init__(self, initial_age):
        if initial_age < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = initial_age

    # Do some computations in here and print out the correct statement to the console
    def amIOld(self):
        if self.age < 13:
            print("You are young.")
        elif (13 <= self.age) and (self.age < 18):
            print("You are a teenager.")
        else:
            print("You are old.")

    # Increment the age of the person in here
    def yearPasses(self):
        self.age += 1


t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
