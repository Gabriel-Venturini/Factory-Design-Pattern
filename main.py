from concrete import NewCar, NewMotorcycle

def main():
    create_car = NewCar()
    print(create_car.what_type())

    create_motorcycle = NewMotorcycle()
    print(create_motorcycle.what_type())

if __name__ == "__main__":
    main()