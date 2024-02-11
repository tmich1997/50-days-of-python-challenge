# Day 41: Only Words with Vowels

def words_with_vowels(str_words):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = str_words.split()
    new_words = []

    for word in words:
        for char in word:
            if char in vowels:
                new_words.append(word)
                break

    return new_words

string_arg = "You have no rhythm,"

print(words_with_vowels(string_arg))

# Extra Challenge: Class of Cars

# define a class named Car
class Car:
    # Iniitialiser or Instance attribute
    # This is where you define the attributes
    # Attributes: model, colour, year, transmission, electric

    def __init__(self, model, colour, year, transmission, electric=False):
        self.model = model
        self.colour = colour
        self.year = year
        self.transmission = transmission
        self.electric = electric
    
    # method to print
        
    def print_cars(self):
        print(f"car_model = {self.model}")
        print(f"Colour = {self.colour}")
        print(f"Year = {self.year}")
        print(f"Transmission = {self.transmission}")
        print(f"Electric = {self.electric}")

# Made 3-subclasses that inherits from the parent class Car

class BMW(Car):
    def __init__(self, model, colour, year, transmission, electric=False):
        super().__init__(model, colour, year, transmission, electric)

class Tesla(Car):
    def __init__(self, model, colour, year, transmission, electric=False):
        super().__init__(model, colour, year, transmission, electric)
        
class Ford(Car):
    def __init__(self, model, colour, year, transmission, electric=False):
        super().__init__(model, colour, year, transmission, electric)


# These are objects/when we have to use a class, we are instantiating objects

ford1 = Ford("focus", "white", 2020, "Auto")
ford1.print_cars()

bmw1 = BMW("x6", "silver", 2018, "Auto")
bmw1.print_cars()

tesla1 = Tesla("S", "beige", 2017, "Auto", True)
tesla1.print_cars()
