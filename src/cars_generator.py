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
cars_header_label =['int', 'str', 'str', 'str', 'date', 'int', 'str', 'str', 'str']


# you should make this class work with any files, let it in take in the key, and from there case objects
class FileReader:

    def __init__(self, filename, header_key):
        self._filename = filename
        self._data_key = header_key
        self._headers = None
        self._file_read = []

    def __iter__(self):
        return FileReader.clean_row(self)

    def clean_row(self):
        with open(self._filename) as file:

            # class io.TextTOWrapper
            # strip out the row ending '\n'
            headers = next(file).strip('\n')

            # clean out white space in header labels
            headers_clean: str = headers.replace(" ", "_")
            # spiting the headers string into a list of strings
            self._headers = headers_clean.split(',')
            yield headers_clean

            for row in file:
                # data is a list of strings from second row down
                data: list = row.strip('\n').split(',')
                # print('data = ', data)

                # namedtuple unpacking headers string seperting elements by comma
                Row = namedtuple('Row', headers_clean)
                #self._file_read.append(self._headers)
                # print('self._headers = ',self._headers)
                # print('50:', 'self._headers ''='' ',self
                final_data_list = [FileReader.cast(data_type, value) for data_type, value in zip(self._data_key, data)]

                final_data_list[4] = FileReader.date_modifier(final_data_list[4])
                finaldatarow = Row(*final_data_list)
                # self._file_read.append(finaldatarow)
                yield finaldatarow

    @staticmethod
    def cast(data_type, data_value):
        if data_type == 'float':
            return float(data_value)
        elif data_type == 'int':
            return int(data_value)
        else:
            return str(data_value)

    @staticmethod
    def date_modifier(date_string):
        date_list = date_string.split('/')
        date_format_key = ['int' for i in range(3)]
        finaldate = [FileReader.cast(date_format_key, date_list)
                     for date_format_key, date_list in zip(date_format_key, date_list)]
        assert all(isinstance(i, int) for i in finaldate)
        date_object = date(finaldate[2], finaldate[0], finaldate[1])
        # assert date_object.year == 2016
        # assert date_object.month == 5
        # assert date_object.day == 10
        return date_object


file = FileReader(source_file, cars_header_label)
fileiter = iter(file)
for i in range(100):
    print(next(fileiter))
