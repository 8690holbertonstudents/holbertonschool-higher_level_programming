#!/usr/bin/python3*
"""
    Module To use serialisation in python.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
        Function that take a Python dictionary and
        a filename as parameters. It should serialize
        the dictionary into XML and save it to the given filename.

        Args:
            filename: The XML filename to create.
            dictionary: The Python dictionary to read.

        Returns:
            The output XML file named "data.xml".
    """
    root = ET.Element('data')
    for key, value in dictionary.items():
        tree = ET.SubElement(root, key)
        tree.text = value
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8')


def deserialize_from_xml(filename):
    """
        Function that ake a filename as its parameter,
        read the XML data from that file,
        and return a deserialized Python dictionary.

        Args:
            filename: The XML file as input.

        Returns:
            A Python dictionnary.
    """
    My_dict = {}
    tree = ET.parse(filename)
    root = tree.getroot()
    for child in root:
        My_dict[child.tag] = child.text
    return (My_dict)
