#!/usr/bin/python3
if __name__ == "__main__":
    import importlib

    module = importlib.import_module("hidden_4")

    names = []
    for name in dir(module):
        if not name.startswith("__"):
            names.append(name)

    names.sort()

    for name in names:
        print(name)
