#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

from property_data_parser import PropertyDataParser


def main():
    parser = argparse.ArgumentParser(
        description='Parses property data from a CSV file')
    parser.add_argument(
        '-f', dest='file', type=str, required=True,
        help="specify path to csv file")
    args = parser.parse_args()
    parser = PropertyDataParser(args.file)

    mean_property_price_w1f = parser.mean_price_in_postcode_w1f()
    print(">> Mean property prices in postcode outward W1F: £{:,.2f}\n".format
          (mean_property_price_w1f))

    avg_diff_detached_vs_flats = \
        parser.average_price_difference_between_detached_houses_and_flats()
    print(">> Average property price difference between detached houses "
          "and flats: £{:,.2f}\n".format(avg_diff_detached_vs_flats))

    print(">> Top 10% most expensive properties ...")
    top_expensive_properties = parser.top_10_percent_expensive_properties()
    print("{0:18} {1:18} {2:18} {3:18} {4:18} {5:18} {6:18} {7:18} "
          "{8:18}".format('PROPERTY_REFERENCE', 'BEDROOMS', 'PRICE',
                          'BATHROOMS', 'HOUSE_NUMBER', 'ADDRESS', 'REGION',
                          'POSTCODE', 'PROPERTY_TYPE'))
    for i in top_expensive_properties:
        print("{0:18} {1:18} {2:18} {3:18} {4:18} {5:18} {6:18} {7:18} "
              "{8:18}".format(i['PROPERTY_REFERENCE'], i['BEDROOMS'],
                              i['PRICE'], i['BATHROOMS'], i['HOUSE_NUMBER'],
                              i['ADDRESS'], i['REGION'], i['POSTCODE'],
                              i['PROPERTY_TYPE']))


if __name__ == '__main__':
    main()
