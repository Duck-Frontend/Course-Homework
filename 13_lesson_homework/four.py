from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):

    def speak(self):
        print("Гав")


class Cat(Animal):

    def speak(self):
        print("Мяу")


class AnimalFactory:

    def create_animal(self, type):
        match type:
            case 'dog': return Dog()
            case 'cat': return Cat()
