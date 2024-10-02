class Animal:
    def __init__(self, name, species, breed, age, health_status):
        self.name = name
        self.species = species
        self.breed = breed
        self._age = age
        self.health_status = health_status

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            raise ValueError("Age must be positive")

    def display_info(self):
        print(f"Animal: {self.name}, Species: {self.species}, Breed: {self.breed}, Age: {self._age}")

    def set_health_status(self, status):
        self.health_status = status
        print(f"{self.name}'s health status updated to: {self.health_status}")

    @staticmethod
    def shelter_policy():
        return "All animals must receive regular medical check-ups."

class AdoptedAnimal(Animal):
    def __init__(self, name, species, breed, age, health_status, adoption_date):
        super().__init__(name, species, breed, age, health_status)
        self.adoption_date = adoption_date

    def display_info(self):
        super().display_info()
        print(f"Adoption Date: {self.adoption_date}")

class Visitor:
    def __init__(self, visitor_name, contact_info):
        self.visitor_name = visitor_name
        self.contact_info = contact_info

    def visit_shelter(self):
        print(f"Visitor {self.visitor_name} is visiting the shelter.")

class Adoption(AdoptedAnimal, Visitor):
    def __init__(self, name, species, breed, age, health_status, adoption_date, visitor_name, contact_info):
        AdoptedAnimal.__init__(self, name, species, breed, age, health_status, adoption_date)
        Visitor.__init__(self, visitor_name, contact_info)

    def display_info(self):
        AdoptedAnimal.display_info(self)
        print(f"Adopted by: {self.visitor_name}, Contact: {self.contact_info}")

if __name__ == "__main__":
    animal1 = Animal("Buddy", "Dog", "Golden Retriever", 5, "Healthy")
    adopted_animal = AdoptedAnimal("Milo", "Cat", "Siamese", 3, "Good", "2023-05-15")
    adoption1 = Adoption("Max", "Dog", "Labrador", 4, "Excellent", "2023-06-20", "John Doe", "555-1234")

    animal1.display_info()
    print(f"Current age: {animal1.age}")

    animal1.age = 6
    print(f"New age: {animal1.age}")

    try:
        animal1.age = -1
    except ValueError as e:
        print(f"Error: {e}")
    animal1.set_health_status("Slight injury")
    adopted_animal.display_info()
    adoption1.display_info()

    print(Animal.shelter_policy())