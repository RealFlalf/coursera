import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        if os.path.splitext(photo_file_name)[1] not in (".jpg", ".jpeg", ".png", ".gif"):
            raise ValueError
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        self.car_type = None

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = "car"


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        try:
            super().__init__(brand, photo_file_name, carrying)
            if body_whl.count("x") != 2:
                raise ValueError
            self.body_length = float(body_whl.split('x')[0])
            self.body_width = float(body_whl.split('x')[1])
            self.body_height = float(body_whl.split('x')[2])
            self.body_whl = body_whl
        except ValueError:
            self.body_length = float(0)
            self.body_width = float(0)
            self.body_height = float(0)
        self.car_type = "truck"

    def get_body_volume(self):
        return self.body_length * self.body_height * self.body_width


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = "spec_machine"


def get_car_list(csv_filename):
    car_list = []
    with open(file_path) as csv_fd:
        reader = csv.DictReader(csv_fd, delimiter=';')
        # next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                if row["car_type"] == "car":
                    car_list.append(Car(row["brand"], row["photo_file_name"], row["carrying"], row["passenger_seats_count"]))
                elif row["car_type"] == "truck":
                    car_list.append(Truck(row["brand"], row["photo_file_name"], row["carrying"], row["body_whl"]))
                elif row["car_type"] == "spec_machine":
                    car_list.append(SpecMachine(row["brand"], row["photo_file_name"], row["carrying"], row["extra"]))
                else:
                    pass
            except (ValueError, TypeError):
                pass
    return car_list


if __name__ == '__main__':
    file_path = "coursera_week3_cars.csv"
    cars = get_car_list(file_path)

    car = Car('Bugatti Veyron', 'bugatti.png', '0.312', '2')
    print(car.car_type, car.brand, car.photo_file_name, car.carrying, car.passenger_seats_count, sep='\n')
    truck = Truck('Nissan', 't1.jpg', '2.5', '2.4x2.3x2')
    print(truck.car_type, truck.brand, truck.photo_file_name, truck.body_length, truck.body_width, truck.body_height, sep='\n')
    spec_machine = SpecMachine('Komatsu-D355', 'd355.jpg', '93', 'pipelayer specs')
    print(spec_machine.car_type, spec_machine.brand, spec_machine.carrying, spec_machine.photo_file_name, spec_machine.extra, sep='\n')
    spec_machine.get_photo_file_ext()
    cars = get_car_list(file_path)
    print(len(cars))