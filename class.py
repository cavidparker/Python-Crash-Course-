class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o

    def do_work(self):
        if self.occupation == "tennies players":
            print(self.name, "playes tennies")
        elif self.occupation == "footbal player":
            print(self.name, "playes footbal")
        elif self.occupation == "actor":
            print(self.name, "shoots a film")

    def speak(self):
        print(self.name, "says how are you")           


tom = Human("tom cruise", "actor")
tom.do_work()
tom.speak()

messi = Human("messi", "footbal player")
messi.do_work()
messi.speak()




############ Function ##############
# def human(name, occupation):
#     if occupation == "actor":
#         print(name, "shoots the film")
#     else:
#         print("No one")

# a = human("messi", "actor")
# print(a)        


