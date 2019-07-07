from collections import namedtuple
from datetime import date

#  Summons Number: int
#  Plate ID: str
#  Registration State: str
#  Plate Type: str
#  Issue Date: date
#  Violation Code: int
#  Vehicle Body Type: str
#  Vehicle Make: str
#  Violation Description str
filename = 'nyc_parking_tickets_extract.csv'
with open(filename) as file:
    # class io.TextTOWrapper
    file_iter = iter(file)
    # strip out the line ending '\n'
    headers = next(file_iter).strip('\n')

    # clean out white space in header labels
    headers: str = headers.replace(" ", "_")

    # data is a list of strings from second line down
    data: list = next(file_iter).strip('\n').split(',')
    # print('data = ', data)

    # namedtuple unpacking headers string
    Car = namedtuple('Car', headers)

    # spiting the headers string into a list of strings
    headerlist = headers.split(',')
    # print('headers = ', headers)

    data_type_list = ['int', 'str', 'str', 'str', 'date', 'int', 'str', 'str', 'str']
    cars = Car(*data)
    # print('cars = ', cars)
    cars_type = Car(*data_type_list)
    # print(cars)
    # print(cars_type)
    # print(len(cars))
    # print(data_type_list)
    # print(list(zip(data, data_type)))

    def cast(data_type, data_value):
        if data_type == 'float':
            return float(data_value)
        elif data_type == 'int':
            return int(data_value)
        else:
            return str(data_value)


    def date_modifier(row):
        date_string = row[4]
        date_list = date_string.split('/')
        date_format_type = ['int' for i in range(4)]
        finaldate = [cast(date_format_type, date_list) for date_format_type, date_list in zip(date_format_type, date_list)]
        assert all(isinstance(i, int) for i in finaldate)
        date_object = date(*reversed(finaldate))
        assert date_object.year == 2016
        assert date_object.month == 5
        assert date_object.day == 10
        return date_object

    final = [cast(data_type, value) for data_type, value in zip(data_type_list, data)]
    final[4] = date_modifier(final)
    print(final)
    print(len(final))
    print(list(type(i) for i in final))

