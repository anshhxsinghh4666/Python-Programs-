# ABSTRACTION: Hiding the implementation details of a class and only showing the essential features to the user.


# Implementation details: User is not seeing the folowing details i.e hidden from user.
class car:
    def __init__(self):
        self.accelerator = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.accelerator = True
        print("Car started")

# Essential features: User only sees the start method.
car1 = car()
car1.start()

