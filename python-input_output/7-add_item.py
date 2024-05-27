#!/usr/bin/python3
"""
    Python script to use JSON.
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
args = sys.argv[1:]

try:
    data = load_from_json_file(filename)
    data += args
    save_to_json_file(data, filename)
except FileNotFoundError:
    data = []
    save_to_json_file(data, filename)
