#!/usr/bin/python3
"""
    Module to keeping track of interation in class.
"""


class CountedIterator:
    """
        A Class named CountedIterator. To extends the built-in
        iterator obtained from the iter function.
    """

    def __init__(self, some_iterable):
        """
        Initialize the CountedIterator object.

        Args:
            some_iterable: An iterable object.

        """
        self.iterator = iter(some_iterable)
        self.counter = 0

    def get_count(self):
        """Method to return the current value of the counter.

        Returns:
            Number of iteration(s).
        """
        return (self.counter)

    def __next__(self):
        """Method to override the __next__ method.

        Returns:
            The next item to iterate.

        Raises:
            raise the StopIteration exception if no
            more items to iterate.
        """
        item = next(self.iterator)
        self.counter += 1

        if self.counter == 0:
            raise StopIteration

        return (item)
