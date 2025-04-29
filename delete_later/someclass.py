class Animal:
    def __init__(self, type, name):
        self.__type = type
        self.name = name
    
    # def __str__(self):
    #     return f"{self.__type} named {self.name}"
    
    def get_type(self):
        return self.__type

class Parent:
    def __init__(self):
        print('This is the parent!')

class GrandChild(Child):
    def __init__(self):
        # super().__init__()
        print('This is the grandchild!')
   
class Child(GrandChild):
    def __init__(self):
        super().__init__()
        print('This is the child!')


x = GrandChild()
# myanimal = Animal("Cat", "Buddy")
# myanimal.__type = "Elephant"  # This will not change the private attribute
# print(myanimal.__type)  # Output: Cat (not the private attribute)
# print(myanimal)  # Output: Dog named Buddy
# print(myanimal.get_type())  # Output: Dog