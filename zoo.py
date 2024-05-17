
#Giuseppe Guttoriello
class Animal:
    def __init__(self,name:str, species:str, age:int, height:int, width:int, preferred_habitat:str, fence:str =None):
        #health che è uguale a round(100 * (1 / age), 3).
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1/age), 3)
        self.fence = fence

animal1 = Animal("Gino","maiale",12,11,11,"Tropicale")

class Fence:
    def __init__(self, area, temperature, habitat, animals: list = []):
        self.animals = animals
        self.area =  area
        self.temperature = temperature
        self.habitat = habitat

    

fence_1 = Fence(122, 26, "tropicale", [animal1])

class Zookeeper:
    def __init__(self, name, surname,id):
        self.name = name
        self.surname = surname
        self.id = id

    def add_animal(self, animal: Animal, fence: Fence):
        if animal.preferred_habitat == fence.habitat and animal.height * animal.width  < fence.area:
                fence.animals.append(animal)
        
    
    def remove_animal(self, animal: Animal, fence: Fence):
        if animal in fence.animals:
            fence.animals.remove(animal)
            fence.area = fence.area - (animal.height * animal.width)
        
    
            
    def feed(self, animal: Animal): #mettere fence dagli attributi animals
        if animal.fence:
            if animal.height * animal.width < animal.fence.area:
                animal.health = animal.health + animal.health * 1 / 100
                animal.height = animal.height + animal.height * 2 /  100
                animal.width = animal.width + animal.width * 2 /  100
                animal.fence.area -= animal.height + animal.width
        else:
                animal.health = animal.health + animal.health * 1 / 100
                animal.height = animal.height + animal.height * 2 /  100
                animal.width = animal.width + animal.width * 2 /  100

  

    def clean(self, fence: Fence):
        areaanimale = 0
        for i in fence.animals:
            areaanimale += i.width * i.height 
        arearimasta = fence.area - areaanimale
        if arearimasta == 0:
            return areaanimale
        else:
            return areaanimale / arearimasta



class Zoo:
    def __init__(self, fences, zoo_keepers):
        self.fences = fences
        self.zoo_keepers = zoo_keepers

    def describe_zoo(self):
        print("guardians:")
        for zookeeper in self.zoo_keepers:
            print(f"Zookeeper(name={zookeeper.name}, surname={zookeeper.surname}, id={zookeeper.id})")
        print("Fences:")

        for fences in self.fences:
            print(f"Fence(area={fences.area}, temperature={fences.temperature}, habitat={fences.habitat}\n with animals:")
            for animals in fences.animals:
                print(f"Animal(name={animals.name}, species={animals.species}, age={animals.age})")
            print("##############################")


