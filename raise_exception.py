class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    def print_exception(self):
        print("User define exception: ", self.msg)



# A = Accident("hello")
# A.print_exception()

try:
    raise Accident("crash between two cars")
except Accident as e:
    e.print_exception()    