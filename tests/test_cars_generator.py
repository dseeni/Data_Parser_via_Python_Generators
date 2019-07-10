from src.cars_generator import FileReader as Fr
from pytest import raises
import types


def test_file_reader_repr(test_file):
    assert test_file.__repr__() == "FileReader(src/nyc_parking_tickets_extract.csv, Vehicle_Make, date_column=4)"


def test_file_reader_is_iterable(test_file):
    assert '__iter__' in dir(test_file)
    assert isinstance(iter(test_file), types.GeneratorType)


def test_file_reader_column_to_track_value_error():
    source_file = 'nyc_parking_tickets_extract.csv'
    with raises(TypeError):
        file = Fr(source_file, 123, date_column=4)
        return file


def test_file_reader_column_to_track_new_column(test_file):
    test_file.column_to_track = 'Vehicle_Body_Type'
    ml = []
    for i in test_file:
        ml.append(i)
    assert test_file.highest_frequency_item == ('SUBN', 352)


def test_file_reader_column_to_track_new_column_2(test_file):
    test_file.column_to_track = 'Plate_Type'
    ml = []
    for i in test_file:
        ml.append(i)
    assert test_file.highest_frequency_item == ('PAS', 743)
