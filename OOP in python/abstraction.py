from abc import ABC, abstractmethod
class vechile(ABC):

    @abstractmethod
    def start(self):
        pass

class Bike(vechile):
    def start(self):
        print("Bike starts with kick")

b=Bike()
b.start()
