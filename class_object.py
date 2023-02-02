class stud:

    # class attribute
    name = ""
    age = 0

# create stud1 object
stud1 = stud()
stud1.name=input("Enter name: ")
stud1.age=input("\nEnter age: ")

# create another object stud2
stud2 = stud()
stud2.name=input("\nEnter name: ")
stud2.age=input("\nEnter age: ")

# access attributes
print(f"\n {stud1.name} is {stud1.age} years old!")
print(f"\n {stud2.name} is {stud2.age} years old!")