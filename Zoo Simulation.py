from random import Random, randint

class Animals(object):
    isAlive = True
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age
        
animalCountA = randint(2, 10)
animalCount = range(1, animalCountA)
animalCount2 = 0
animals = {}
animalsAlive = True
beans = ""

for i in animalCount:
    animalCount2 += 1
    animalType = ""
    animalSpecies = randint(1, 4)
    if animalSpecies == 1:
        animalType = "Penguin" 
    elif animalSpecies == 2:
        animalType = "Monkey"
    elif animalSpecies == 3:
        animalType = "Tiger"
    elif animalSpecies == 4:
        animalType = "Giraffe"
    animals[str(i)] = Animals(animalType, randint(1, 50))

while animalsAlive == True:
    print("----------")
    for animal in animals:
        if animals[animal].age == 60:
            animals[animal].isAlive = False
        if animals[animal].isAlive == True:
            animals[animal].age += 1
            print(animals[animal].breed + " Age: " + str(animals[animal].age))
        if animals[animal].isAlive == False:
            print(animals[animal].breed + " is dead")
    for animal in animals:
        if animals[animal].isAlive == False:
            animalCount2 += 1
            if animalCount2 == animalCountA:
                animalsAlive = False
                print("All Animals are dead")
        else:
            animalCount2 = 0
    print("----------")
    beans = input("Press Enter")