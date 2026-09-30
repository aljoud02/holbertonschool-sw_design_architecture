#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def mode(self) -> str:
        pass


class Bus(Vehicle):
    def mode(self) -> str:
        return "road"


class Train(Vehicle):
    def mode(self) -> str:
        return "rails"


class Bike(Vehicle):
    def mode(self) -> str:
        return "lane"


class Scooter(Vehicle):
    def mode(self) -> str:
        return "scooter_lane"


class VehicleFactory:
    def __init__(self):
        self._registry = {}

    def register_kind(self, name: str, cls):
        self._registry[name] = cls

    def create(self, kind: str):
        if kind not in self._registry:
            raise ValueError(f"Unknown vehicle kind: {kind}")
        return self._registry[kind]()


def main():
    factory = VehicleFactory()
    factory.register_kind("bus", Bus)
    factory.register_kind("train", Train)
    factory.register_kind("bike", Bike)

    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())

    # Registering the new scooter vehicle type
    factory.register_kind("scooter", Scooter)
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
