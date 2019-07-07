from collections import namedtuple
from datetime import date

filename = 'nyc_parking_tickets_extract.csv'
#  Summons Number: int
#  Plate ID: str
#  Registration State: str
#  Plate Type: str
#  Issue Date: date
#  Violation Code: int
#  Vehicle Body Type: str
#  Vehicle Make: str
#  Violation Description str
with open(filename) as file:
    file_iter = iter(file)
    headers = next(file_iter).strip('\n')
    headers = headers.replace(" ","_")
    print(headers)
    print(type(headers))
    data = next(file_iter).strip('\n').split(',')
    # print(headers)
    # print(type(headers))
    # print(data)
    Car = namedtuple('Car', headers)
    headers = headers.split(',')
    print(len(headers))
    print(type(headers))
    data_type = ['int', 'str', 'str', 'str', 'date', 'int', 'str', 'str', 'str']
    cars = Car(*data)
    cars_type = Car(*data_type)
    print(cars)
    print(cars_type)
    
    # print(len(cars))
    print(data_type)
    # print(list(zip(data, date_type)))

    def cast(data_type, value):
        if data_type == 'float':
            return float(value)
        elif data_type == 'int':
            return int(value)
        else:
            return str(value)
    final = [cast(data_type, value) for data_type, value in zip(data_type, data)]

    final = Car(*final)
    print(final)

# def file_reader(self):
#     with open(self.file) as csv:
#         yield next(iter(csv))
#         # for line in csv:
#         #     print(line)

# testdate = date(2012, 12, 12)
# print(testdate)
