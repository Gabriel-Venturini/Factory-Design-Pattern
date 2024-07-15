from abstract import Car, VehicleCreator

class NewCar(VehicleCreator):
    def create_vehicle(self):
        return Car()