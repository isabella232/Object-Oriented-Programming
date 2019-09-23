class Dog:
    organism_type = "animal"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __del__(self):
        print("Destructor called, Dog object deleted.")

    def bark(self):  # class method!
        print(self.name + " says woof woof!")

    @staticmethod
    def get_species():  # static method!
        print("Dogs are mammals!")


my_dog = Dog("coco", 4, "westie")
my_dog.bark()
Dog.get_species()
del my_dog
