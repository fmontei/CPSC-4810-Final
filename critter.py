import random

class Critter:
    def __init__(self, name, type, hunger, boredom):
        self.__name = name
        self.__type = type
        self.__hunger = hunger
        self.__boredom = boredom

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type

    @property
    def hunger(self):
        return self.__hunger

    @property
    def boredom(self):
        return self.__boredom

    def feed(self):
        self.__hunger -= 1
        if self.__hunger < 0:
            self.__hunger = 0

    def play(self):
        self.__boredom -= 1
        if self.__boredom < 0:
            self.__boredom = 0

class CritterFarm:
    def __init__(self, name, num):
        self.__name = name
        self.__num_critters = num
        self.__list = []
        self.__randomize()

    def __randomize(self):
        name_list = ["Rocket", "Sally", "Bert", "Spot", "Zeus"]
        type_list = ["Cow", "Dog", "Chicken", "Pig", "Cat"]

        for i in range(0, self.__num_critters):
            hunger = random.randint(0, 5)
            boredom = random.randint(0, 5)
            name = name_list[random.randint(0, len(name_list) - 1)]
            type = type_list[random.randint(0, len(type_list) - 1)]
            self.__list.append(Critter(name, type, boredom, hunger))

    def print_list(self):
        print("1) Cow(s):")
        print("\t", end = "")
        for i in range(0, len(self.__list) - 1):
            if self.__list[i].type == "Cow":
                print(self.__list[i].name, end = " ")
        print("\n2) Dog(s):")
        print("\t", end = "")
        for i in range(0, len(self.__list) - 1):
            if self.__list[i].type == "Dog":
                print(self.__list[i].name, end = " ")
        print("\n3) Chicken(s):")
        print("\t", end = "")
        for i in range(0, len(self.__list) - 1):
            if self.__list[i].type == "Chicken":
                print(self.__list[i].name, end = " ")
        print("\n4) Pig(s):")
        print("\t", end = "")
        for i in range(0, len(self.__list) - 1):
            if self.__list[i].type == "Pig":
                print(self.__list[i].name, end = " ")
        print("\n5) Cat(s):")
        print("\t", end = "")
        for i in range(0, len(self.__list) - 1):
            if self.__list[i].type == "Cat":
                print(self.__list[i].name, end = " ")

    def make_noise(self):
        for i in range(0, len(self.__list) - 1):
            if self.__list[i].type == "Cow":
                print("Moo", end = " ")
            elif self.__list[i].type == "Dog":
                print("Woof", end = " ")
            elif self.__list[i].type == "Chicken":
                print("Cock-a-doodle-doo", end = " ")
            elif self.__list[i].type == "Pig":
                print("Oink", end = " ")
            elif self.__list[i].type == "Cat":
                print("Meow", end = " ")

    def feed_critters(self):
        print("Name\t     Type     Hunger")
        for crit in self.__list:
            crit.feed()
            print("%s\t%8s\t%d" % (crit.name, crit.type, crit.hunger))

    def play_critters(self):
        print("Name\t     Type     Boredom")
        for crit in self.__list:
            crit.play()
            print("%s\t%8s\t%d" % (crit.name, crit.type, crit.boredom))
            

    @property
    def name(self):
        return self.__name

def main():

    name = input("What do you want your critter farm to be called? ")
    num_critters = int(input("How many critters do" 
                             " you want your farm to have? "))

    farm = CritterFarm(name, num_critters)
    
    choice = None
    while choice != "0":
        print("""
              Critter Farm Caretaker

              0 - Quit
              1 - List your critters
              2 - Listen to your critters
              3 - Feed your critters
              4 - Play with your critters
              """)
        choice = input("Choice: ")
        print()

        if choice == "0":
            print("Good-bye.")
        elif choice == "1":
            farm.print_list()
        elif choice == "2":
            farm.make_noise()
        elif choice == "3":
            farm.feed_critters()
        elif choice == "4":
            farm.play_critters()

        print()

main()
