#!/usr/bin/python3
"""
    Module to create a custom class.
"""


class VerboseList(list):
    """
        Subclass named VerboseList that inherit from build-in list.
    """

    def append(self, new_obj):
        """
        Method to append a new element to a list.

        Args:
            new_obj: object added to the list.

        Returns:
            The object added. Print message when done.

        """
        super().append(new_obj)
        print(f"Added [{new_obj}] to the list.")

    def extend(self, new_objs):
        """
        Method to extend new elements to a list.

        Args:
            new_objs: objects added to the list.

        Returns:
            The objects added. Print message when done.

        """
        super().extend(new_objs)
        print(f"Extended the list with [{new_objs}] items.")

    def remove(self, obj):
        """
        Method to remove an object to a list.

        Args:
            obj: object to be removed.

        Returns:
            The object removed. Print message when done.

        """
        super().remove(obj)
        print(f"Removed [{obj}] from the list.")

    def pop(self, idx=None):
        """
        Method to remove an object to a list by index.

        Args:
            idx: the index object to be removed.

        Returns:
            The object removed. Print message when done.

        """
        if idx is None:
            popped = super().pop()
        else:
            popped = super().pop(idx)

        print(f"Popped [{popped}] from the list.")
