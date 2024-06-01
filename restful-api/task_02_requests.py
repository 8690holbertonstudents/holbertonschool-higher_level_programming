#!/usr/bin/python3
"""
    Python sript to use HTTP requests and API JSONPlaceholder.
"""
import requests
import csv


def fetch_and_print_posts():
    """
        Function that fetches all post from JSONPlaceholder.

        Returns:
            Print all values of key "title" form a JSON dictionary.
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {r.status_code}")
    data = r.json()
    for key in data:
        print(key["title"])


def fetch_and_save_posts():
    """
        Function that fetches all post from JSONPlaceholder.

        Returns:
            Create a list of dictionaries and write key values
            "id", "title", and "body" in a csv file "posts.csv"
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {r.status_code}")
    data = r.json()
    my_list = []
    for key in data:
        my_dict = {"id": key["id"], "title": key["title"], "body": key["body"]}
        my_list.append(my_dict)

    with open("posts.csv", mode="w", encoding="utf-8") as csv_file:
        fields = ["id", "title", "body"]
        csv_data = csv.DictWriter(csv_file, fieldnames=fields)
        csv_data.writeheader()
        csv_data.writerows(my_list)
