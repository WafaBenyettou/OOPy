class Dog:
    def __init__(self, name, age):
        self.__name = name  # Private attribute

    def get_name(self):
        return self.__name

buddy = Dog("Buddy", 3)
print(buddy.get_name())  # Buddy
