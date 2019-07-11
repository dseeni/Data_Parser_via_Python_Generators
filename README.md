# Python Deep Dive Part 2 Project 3

### Generic CSV data paraser via generators 

- FileReader(self, filename, column_to_track,*, date_column=None)
    
- Automatically cast column data into respective data types: float, string, integer, date

- Date restricted only to one column via date_column 

- Return the frequency distribution of data via column_to_track 
    * Make sure you white space is replaced with "_" for column_to_track

### Processing "nyc_parking_tickets_extract.csv":
**_Most Common Citations by..._**

- Vehicle Make: ('TOYOT', 112)

- Vehicle Body Type: ('SUBN', 352) 

- Violation Description: ('PHTO SCHOOL ZN SPEED VIOLATION', 140)

- Registration State: ('NY', 779)

- Issue Date: (datetime.date(2016, 11, 14), 10)


