from abc import ABC, abstractmethod

class VehicleCreator(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass

    def what_type(self):
        vehicle = self.create_vehicle()
        return vehicle.type()