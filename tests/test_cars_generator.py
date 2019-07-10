from src.cars_generator import FileReader as Fr
from pytest import raises
import types


def test_file_reader_repr(test_file):
    assert test_file.__repr__() == "FileReader(nyc_parking_tickets_extract.csv, Vehicle_Make, date_column=4)"


def test_file_reader_is_iterable(test_file):
    assert '__iter__' in dir(test_file)
    assert isinstance(iter(test_file), types.GeneratorType)


def test_file_reader_column_to_track_value_error():
    source_file = 'nyc_parking_tickets_extract.csv'
    with raises(TypeError):
        file = Fr(source_file, 123, date_column=4)
        return file
