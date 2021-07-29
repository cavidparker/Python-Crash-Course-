# class Father():
#     def gardening(self):
#         print("I enjoyed gardening")

# class Mother():
#     def cooking(self):
#         print("I love cooking")


# class Child(Father,Mother):
#     def sports(self):
#         print("I enjoy sports")
#         self.gardening()


# C = Child()
# C.sports()



class Father:
    def skills(self):
        print("cooking", "programming","model")

class Mother:
    def skills(self):
        print("cooking", "teaching","design")

class Child(Father,Mother):
    def skills(self):
        print("sports")
        Father.skills(self)


C = Child()
C.skills()                  