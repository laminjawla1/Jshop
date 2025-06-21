from abc import ABCMeta

class IPerson(metaclass=ABCMeta):
    @staticmethod
    def get_data():
        """ Implement in child class """

class PersonSingleton(IPerson):
    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance is None:
            PermissionError("Default Name", 0)
        return PersonSingleton.__instance
    
    def __init__(self, name, age):
        if PersonSingleton.__instance is not None:
            raise Exception("Another instance already running")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self
    
    @staticmethod
    def print_data():
        print(f"Name: {PersonSingleton.__instance.name}, Age: {PersonSingleton.__instance.age}")

p = PersonSingleton("Lamin Jawla", 28)
print(p)
p.print_data()

p = PersonSingleton("Lamin Jawla", 28)
print(p)
p.print_data()