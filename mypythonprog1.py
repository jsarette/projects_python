    # create a list of 100 numbers  0 to 99
# print the list
# print the list in reverse order
# print the list in reverse order using a for loop

# create a list of 100 numbers  0 to 99
mylist = range(100)
print (mylist)

def even(x):
    return x % 2 == 0   # returns True if x is even

odd = lambda x: x % 2 == 1  # returns True if x is odd  (lambda function)      

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)
# list of 10 people
people = [Person("John", 36), Person("Mary", 37), Person("Bob", 40), Person("Alice", 39), Person("Joe", 38), Person("Sue", 35), Person("Tom", 41), Person("Jane", 42), Person("Bill", 43), Person("Kate", 44)]  

# print the list of people
for p in people:
    print (p.name, p.age)       


PEOPLE = [      
    
]  # empty list
# add people to the list
PEOPLE.append(Person("John", 36))
PEOPLE.append(Person("Mary", 37))
PEOPLE.append(Person("Bob", 40))
PEOPLE.append(Person("Alice", 39))
PEOPLE.append(Person("Joe", 38))
PEOPLE.append(Person("Sue", 35))
PEOPLE.append(Person("Tom", 41))
PEOPLE.append(Person("Jane", 42))
PEOPLE.append(Person("Bill", 43))
PEOPLE.append(Person("Kate", 44))