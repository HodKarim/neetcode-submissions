class Pet:
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species #assigns value of species parameter




# Do not modify below this line
my_pet = Pet("Fluffy", "cat")
print(f"My pet is a {my_pet.species} named {my_pet.name}")
