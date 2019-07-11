# Python Deep Dive Part 2 Project 3

### Generic CSV Data Paraser using Python Generators: 

- FileReader(self, filename, column_to_track,*, date_column=None)
    
- Second row data will automatically determine the data types for .csv file: float, string, integer, date

- Date restricted only to one column via date_column 

- Return the frequency distribution of data per Column Header via column_to_track 
    * Make sure you replace white space with "_" when passing in header names to column_to_track

### Processing "nyc_parking_tickets_extract.csv":

**_Here are the most common citations by..._**

- Vehicle Make: ('TOYOT', 112)

- Vehicle Body Type: ('SUBN', 352) 

- Violation Description: ('PHTO SCHOOL ZN SPEED VIOLATION', 140)

- Registration State: ('NY', 779)

- Issue Date: (datetime.date(2016, 11, 14), 10)


