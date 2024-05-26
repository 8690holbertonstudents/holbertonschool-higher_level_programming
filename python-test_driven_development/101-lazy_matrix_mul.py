#!/usr/bin/python3
"""Module for matrix multiplication with NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Function to multiply two matrix
       with numpy.
    """
    return (np.matmul(m_a,m_b))
