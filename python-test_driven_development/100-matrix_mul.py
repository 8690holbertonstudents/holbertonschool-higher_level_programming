#!/usr/bin/python3
"""Module for matrix multiplication.
"""


def matrix_mul(m_a, m_b):
    """Function two matrix (and only matrix) and return
       the multiplication of these two matrix.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if not all(isinstance(row_a, list) for row_a in m_a) \
       or not all(isinstance(row_b, list) for row_b in m_b):
        raise TypeError(
            "m_a must be a list of lists or m_b must be a list of lists")

    if len(m_a) == 0 or all(len(row_a) == 0 for row_a in m_a) \
       or len(m_b) == 0 or all(len(row_b) == 0 for row_b in m_b):
        raise ValueError("m_a can't be empty or m_b can't be empty")

    msg1 = "m_a should contain only integers or floats "
    msg2 = "or m_b should contain only integers or floats"
    for row in m_a:
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(msg1 + msg2)

    for row in m_b:
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(msg1 + msg2)

    msg3 = "each row of m_a must be of the same "
    msg4 = "size or each row of m_b must be of the same size"
    if any(len(row_a) != len(m_a[0]) for row_a in m_a) \
       or any(len(row_b) != len(m_b[0]) for row_b in m_b):
        raise TypeError(msg3 + msg4)

    if not (len(m_a[0]) == len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for val in range(len(m_b[0]))] for val in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return (result)
