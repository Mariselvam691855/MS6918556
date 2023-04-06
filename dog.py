class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    
    def description(self):
        print(f"{self.name} is {self.age} years old.")
        
    def get_info(self):
        print(f"{self.name} has {self.coat_color} coat color.")
    
class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)
        
    def bark(self):
        print(f"{self.name} is barking loudly.")
        
    def hunt(self):
        print(f"{self.name} is hunting for prey.")
        
class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)
        
    def snore(self):
        print(f"{self.name} is snoring loudly.")
        
    def guard(self):
        print(f"{self.name} is guarding its territory.")
        
my_dog = Dog('Max', 3, 'brown')
my_dog.description()
my_dog.get_info()

my_jack = JackRussellTerrier('Jack', 2, 'white')
my_jack.description()
my_jack.get_info()
my_jack.bark()
my_jack.hunt()

my_bulldog = Bulldog('Buddy', 5, 'grey')
my_bulldog.description()
my_bulldog.get_info()
my_bulldog.snore()
my_bulldog.guard()