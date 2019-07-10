from pytest import fixture
from src.cars_generator import FileReader as Fr

@fixture(scope='function')
def test_file():
    source_file = 'nyc_parking_tickets_extract.csv'
    file = Fr(source_file, 'Vehicle_Make', date_column=4)
    return file
