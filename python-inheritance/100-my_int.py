#!/usr/bin/python3
"""
    Module to manipulate subclasses.
"""


class MyInt(int):
    """
        Subclass Myint inherit from class int.
    """

    def __eq__(self, other):
        """ function to override the default == operator
            Invert result.

        Args:
            other: The value passed to ==

        Returns:
            Return the opposite value.

        """
        return (not super().__eq__(other))

    def __ne__(self, other):
        """ function to override the default != operator
            Invert result.

        Args:
            other: The value passed to !=

        Returns:
            Return the opposite value.

        """
        return (not super().__ne__(other))
