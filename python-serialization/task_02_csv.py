#!/usr/bin/python3*
"""
    Module To use serialisation in python.
"""
import json
import csv


def convert_csv_to_json(filename):
    """
        Function hat takes the CSV filename as its parameter
        and writes a JSON file.

        Args:
            filename: The CSV filename to read (data.csv).

        Returns:
            The output JSON file named "data.json".
    """
    try:
        with open(filename, mode="r", encoding="utf-8") as csv_file:
            csv_data = csv.DictReader(csv_file)
            csv_lines = []
            for lines in csv_data:
                csv_lines.append(lines)

        with open("data.json", mode="w", encoding="utf-8") as json_File:
            json.dump(csv_lines, json_File)
        return (True)

    except FileNotFoundError:
        return (False)
