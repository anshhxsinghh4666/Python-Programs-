# Class Method (Decorator) : A class method is bound to the class & receive the class as an implicit first argument.

class person1:
    name = "Ansh Singh"  #Class attribute

    def change_name(self, name):
        self.name = name  # Instance attribute

# NOTE: The name in class attribute is different from the instance attribute.

p1 = person1()
p1.change_name("Nehal dagar")  # This will assign the name to instance attribute.
print(p1.name)   # So this will print Nehal dagar.
print(person1.name)  # This will call the name in class sttribute. So this will NOT print the new name Nehal Dagar , instead this will print Ansh Singh. Therefore the class attribute is still the same.

# To change the class attribute check the code below:  (Instance method)
class person2:
    name = "Ansh Singh"  #Class attribute

    def change_name(self, name):
        person2.name = name   # To change the class attribute use person.name instead of self.name.

p1 = person2()
p1.change_name("Nehal dagar")  # This will assign the name to class attribute.
print(p1.name)   # So this will print Nehal dagar.
print(person2.name)  # This will also print Nehal dagar.

# OR

class person3:
    name = "Ansh Singh"  #Class attribute

    def change_name(self, name):
        self.__class__.name = name   # To change the class attribute use self.__class__.name instead of self.name

p1 = person3()
p1.change_name("Nehal dagar")  # This will assign the name to class attribute.
print(p1.name)   # So this will print Nehal dagar.
print(person3.name)  # This will also print Nehal dagar.

# OR (using Class Method)

class person4:
    name = "Ansh Singh"  #Class attribute

    @classmethod   #decorator
    def change_name(cls, name):
        cls.name = name   # To change the class attribute use @classmethod

p1 = person4()
p1.change_name("Nehal dagar")  # This will assign the name to class attribute.
print(p1.name)   # So this will print Nehal dagar.
print(person4.name)  # This will also print Nehal dagar.