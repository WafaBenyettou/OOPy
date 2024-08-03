class Person:
    def __init__(self, name):
        self.name = name  # Public attribute

class Vehicle:
    def __init__(self, brand):
        self._brand = brand  # Protected attribute

class Diary:
    def __init__(self, secret):
        self.__secret = secret  # Private attribute