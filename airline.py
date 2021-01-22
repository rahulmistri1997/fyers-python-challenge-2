"""
CSV Reader for getting All unique Airport.Names , Max visits and Min visits

"""
# This code is 'PEP 8' Compliant and has been rated at 10.00/10 (Using pylint)

import json
import sys
import os

def resource_path(relative_path):
    """
    Get absolute path to resource . Used here to check if the file exists.
    """

    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path,relative_path)

def csvopen(filename):
    """
    Opening CSV file and returns a dictionary with unique airport names and their count.

    """

    unique_air = {} # Initializing a dict for storing the unique airport names

    with open(filename, mode='r') as csv_file:
        line_count = 0
        for row in csv_file:
            words = row.split(",") # Splitting every line in the CSV
            if line_count == 0:
                # left this here just to make the counter start from 0 and to add a count.
                # Because the first rows are just names
                # will be helpful if ever have to add CSV to DB using SQL.
                line_count += 1
                continue

            airport_name = words[1]+","+words[2]
            airport_name = airport_name.strip('"') # Removing extra quotes
            # Adding values in dictionary and if value is already present adding 1 to it.
            if airport_name not in unique_air:
                unique_air[airport_name] = 1
            else:
                unique_air[airport_name] += 1

            line_count += 1

        return unique_air

def tojson(uniq_dict):
    """
    Converts the unique dictionary to json and prints it.

    """
    dict_json = json.dumps(uniq_dict,indent=2)
    print("Output 1 : List of unique airport names, number of times in a json format\n")
    print(dict_json + "\n")

def maxcount(uniq_dict):
    """
    Prints the MAX (Name and count)

    """
    print("Output 2 : Airport is mentioned highest number of times and its count \n")
    highest_mention = max(uniq_dict, key=uniq_dict.get)
    print(f'{highest_mention}: {uniq_dict[highest_mention]} \n')

def mincount(uniq_dict):
    """
    Prints the MIN (Name and count)

    """
    print("Output 3 : Airport is mentioned lowest number of times and its count \n")
    lowest_mention = min(uniq_dict, key=uniq_dict.get)
    print(f'{lowest_mention}: {uniq_dict[lowest_mention]} \n')


# Checking if File exists or Not
input_filename = input("File name: ")
file = resource_path(input_filename)

if os.path.exists(file) and file.endswith('.csv'):
    unqiue_airport_name = csvopen(file)
    tojson(unqiue_airport_name)
    maxcount(unqiue_airport_name)
    mincount(unqiue_airport_name)
else:
    # Prints this error if the file doesn't exists
    print("\nFile doesn't exists, check if you are in the correct directory")
    print("And selected a file with extension of csv")
