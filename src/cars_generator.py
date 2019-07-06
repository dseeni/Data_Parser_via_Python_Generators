def file_reader(file):
    with open(file) as file:
        for line in file:
            print(line)


file_reader('nyc_parking_tickets_extract.csv')

