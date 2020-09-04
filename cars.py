import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.car_type = None

    def get_photo_file_ext(self):
        print(os.path.splitext(self.photo_file_name)[1])


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count
        self.car_type = "Car"


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_length = body_whl.split('x')[0]
        self.body_width = body_whl.split('x')[1]
        self.body_height = body_whl.split('x')[2]
        self.body_whl = body_whl
        self.car_type = "Truck"

    def get_body_volume(self):
        return self.body_length * self.body_height * self.body_width


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = "SpecMachine"


def get_car_list(csv_filename):
    car_list = []
    with open(file_path) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            car_list.append(row)
    return car_list


if __name__ == '__main__':
    file_path = "coursera_week3_cars.csv"
    cars = get_car_list(file_path)

    # car = Car('Bugatti Veyron', 'bugatti.png', '0.312', '2')
    # print(car.car_type, car.brand, car.photo_file_name, car.carrying, car.passenger_seats_count, sep='\n')
    # truck = Truck('Nissan', 'nissan.jpeg', '1.5', '3.92x2.09x1.87')
    # print(truck.car_type, truck.brand, truck.photo_file_name, truck.body_length, truck.body_width, truck.body_height, sep='\n')
    # spec_machine = SpecMachine('Komatsu-D355', 'd355.jpg', '93', 'pipelayer specs')
    # print(spec_machine.car_type, spec_machine.brand, spec_machine.carrying, spec_machine.photo_file_name, spec_machine.extra, sep='\n')
    # spec_machine.get_photo_file_ext()
    # cars = get_car_list(file_path)
    #print(cars)