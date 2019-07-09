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

source_file = 'nyc_parking_tickets_extract.csv'
cars_header_label = ['int', 'str', 'str', 'str', 'date', 'int', 'str', 'str', 'str']


# you should make this class work with any files, let it in take in the key, and from there case objects
class FileReader:

    def __init__(self, filename, header_key):
        self._filename = filename
        self._data_key = header_key
        self._headers = None

    def __iter__(self):
        return FileReader.readline(self._filename)

    def readline(self):
        with open(self._filename) as file:
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

            final = [FileReader.cast(data_type, value) for data_type, value in zip(data_type_list, data)]
            final[4] = FileReader.date_modifier(final[4])

            print('61:', 'final[4] ''='' ', final[4])
            print('62:', 'final[4] ''='' ', final[4])

            finalheaderrow = Car(*headerlist)
            finaldatarow = Car(*final)
            # print(finalheaderrow, sep='\n')
            return finaldatarow

    @staticmethod
    def cast(data_type, data_value):
        if data_type == 'float':
            return float(data_value)
        elif data_type == 'int':
            return int(data_value)
        else:
            return str(data_value)

    @staticmethod
    def date_modifier(row):
        date_list = row.split('/')
        date_format_type = ['int' for i in range(4)]
        finaldate = [FileReader.cast(date_format_type, date_list)
                     for date_format_type, date_list in zip(date_format_type, date_list)]
        assert all(isinstance(i, int) for i in finaldate)
        date_object = date(*reversed(finaldate))
        assert date_object.year == 2016
        assert date_object.month == 5
        assert date_object.day == 10
        return date_object


file = FileReader(source_file, cars_header_label)
row = [i for i in range(10)]

