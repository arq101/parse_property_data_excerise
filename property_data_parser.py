# -*- coding: utf-8 -*-

import csv
import os


class PropertyDataParser(object):
    """ Parses data from a csv file containing property information.
    """

    def __init__(self, filename):
        self.file_name = filename
        self.file_handle = None

    def _check_file_exists(self):
        if os.path.isfile(os.path.abspath(self.file_name)):
            return True
        else:
            print('>> Error: file "{}" not found!'.format(self.file_name))
            # then bail out
            raise FileNotFoundError

    def _read_csv_file(self):
        """ Reads and returns a reader object which will iterate over lines in
        the given csv file and maps the column names.

        This method also checks if the csv file has any rows of data and
        that the number of columns are as expected.

        Manually close the file handle
        """
        self._check_file_exists()
        self.file_handle = open(self.file_name)
        reader = csv.DictReader(self.file_handle)
        self._check_number_of_columns_in_csv_file(reader)
        try:
            reader.__next__()

            # csv reader obj will not refresh even if the file handle is
            # "seeked" to 0, so recreate reader obj
            self.file_handle.seek(0)
            reader = csv.DictReader(self.file_handle)
        except StopIteration:
            print('>> Error: file "{}" does not contain data!'.format(self.file_name))
            raise ValueError
        else:
            return reader

    def _check_number_of_columns_in_csv_file(self, csv_reader_obj):
        expected_columns = 9
        if len(csv_reader_obj.fieldnames) == expected_columns:
            return
        else:
            print('>> Error: expected {} columns, but found {}!'.format(
                expected_columns, len(csv_reader_obj.fieldnames)))
            raise ValueError

    def mean_price_in_postcode_w1f(self):
        """ Returns the mean property price where postcode starts with W1F.
        """
        reader = self._read_csv_file()
        property_prices = []
        for row in reader:
            if row['POSTCODE'].startswith('W1F'):
                property_prices.append(int(row['PRICE']))
        self.file_handle.close()
        return sum(property_prices) / len(property_prices)

    def average_price_difference_between_detached_houses_and_flats(self):
        """ Returns the difference in average property prices between
        detached houses	and	flats.
        """
        reader = self._read_csv_file()
        detached_house_prices = []
        flat_prices = []
        for row in reader:
            if row['PROPERTY_TYPE'] == 'Detached':
                detached_house_prices.append(int(row['PRICE']))
            elif row['PROPERTY_TYPE'] == 'Flat':
                flat_prices.append(int(row['PRICE']))
        self.file_handle.close()

        average_detached_price = \
            sum(detached_house_prices) / len(detached_house_prices)
        average_flat_price = sum(flat_prices) / len(flat_prices)
        return abs(average_detached_price - average_flat_price)

    def _count_rows_in_data_file(self):
        """ Simply counts the number of data rows in the csv file
        """
        reader = self._read_csv_file()
        row_count = sum(1 for row in reader)
        self.file_handle.close()
        return row_count

    def top_10_percent_expensive_properties(self):
        """ Returns a list of the top 10% most expensive properties
        """
        # determine the number or rows that represents 10%
        top_expensive_rows = round(self._count_rows_in_data_file() * 0.10)
        reader = self._read_csv_file()

        # convert string price to int for correct numerical sorting
        sorted_list = sorted(
            reader, key=lambda row: int(row['PRICE']), reverse=True)
        self.file_handle.close()
        return sorted_list[:top_expensive_rows]
