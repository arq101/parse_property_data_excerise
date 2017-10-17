#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from property_data_parser import PropertyDataParser


class TestPropertyDataParser(unittest.TestCase):

    def test_file_exists(self):
        prop_parser = PropertyDataParser('./test_data/test_data_1.csv')
        self.assertTrue(prop_parser._check_file_exists())

    def test_file_not_found(self):
        prop_parser = PropertyDataParser('./test_data/foo_bar.csv')
        with self.assertRaises(FileNotFoundError):
            prop_parser._check_file_exists()

    def test_csv_reader_object(self):
        prop_parser = PropertyDataParser('./test_data/test_data_1.csv')
        reader = prop_parser._read_csv_file()
        data_rows = sum(1 for row in reader)
        self.assertEqual(data_rows, 2)
        prop_parser.file_handle.close()

    def test_csv_reader_object_with_no_data_rows(self):
        prop_parser = PropertyDataParser('./test_data/test_data_4.csv')
        try:
            with self.assertRaises(ValueError):
                prop_parser._read_csv_file()
        finally:
            prop_parser.file_handle.close()

    def test_unexpected_number_of_columns_in_csv_file(self):
        prop_parser = PropertyDataParser('./test_data/test_data_5.csv')
        try:
            with self.assertRaises(ValueError):
                prop_parser._read_csv_file()
        finally:
            prop_parser.file_handle.close()

    def test_get_mean_price_in_w1f(self):
        prop_parser = PropertyDataParser('./test_data/test_data_1.csv')
        self.assertEqual(prop_parser.mean_price_in_postcode_w1f(), 1750000)

    def test_get_average_diff_between_detached_house_and_flat(self):
        prop_parser = PropertyDataParser('./test_data/test_data_2.csv')
        self.assertEqual(
            prop_parser.average_price_difference_between_detached_houses_and_flats(),
            88750)

    def test_top_10_percent_expensive_properties(self):
        prop_parser = PropertyDataParser('./test_data/test_data_3.csv')
        top_expensive = prop_parser.top_10_percent_expensive_properties()
        self.assertEqual(len(top_expensive), 1)
        self.assertEqual(top_expensive[0]['PROPERTY_REFERENCE'], '1')
        self.assertEqual(top_expensive[0]['PRICE'], '1000000')


if __name__ == '__main__':
    unittest.main(verbosity=2)


