from abstract import Motorcycle, VehicleCreator

class NewMotorcycle(VehicleCreator):
    def create_vehicle(self):
        return Motorcycle()