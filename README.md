# Coding task to parse property data from csv file

The parser class is designed to read property data and produce the following output ...

* display the mean property price for properties belonging to a specific postcode
* display difference in	average	property prices between	detached houses	and	flats
* display the top 10% most expensive properties


## Execute the script

Designed to run with Python 3.5 using standard Python libraries.
```
eg.
$ python3 main.py -f ./property-data.csv


$ python3 main.py -h
usage: main.py [-h] -f FILE

Parses property data from a CSV file

optional arguments:
  -h, --help  show this help message and exit
  -f FILE     specify path to csv file

```

## Tests

Unit-tests can be run as:
```
python3 test_property_data_parser.py
```
or
```
python3 -m unittest test_property_data_parser.TestPropertyDataParser
```
