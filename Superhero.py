
# Base class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        return f"I am {self.name} from {self.origin}, and I wield the power of {self.power}!"

    def use_power(self):
        return f"{self.name} uses {self.power} to save the day!"

# Subclass with polymorphism
class FlyingHero(Superhero):
    def use_power(self):
        return f"{self.name} soars through the skies with {self.power}!"

# Subclass with encapsulation
class TechHero(Superhero):
    def __init__(self, name, power, origin, gadgets):
        super().__init__(name, power, origin)
        self.__gadgets = gadgets  # private attribute

    def reveal_gadgets(self):
        return f"{self.name} has gadgets like: {', '.join(self.__gadgets)}"
