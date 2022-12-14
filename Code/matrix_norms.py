# -*- coding: utf-8 -*-
"""matrix_norms.ipynb

Author: @santiagoahl

Original file is located at
    https://colab.research.google.com/drive/1VIyjrCKsFQvR4S9Mone8HqYfXehmBpne
"""

import numpy as np
import pandas as pd

ords = ['fro', 'nuc', np.inf, -np.inf, -1, 1, -2, 2]

def compute_norms(matrix):
  norms = []
  for ord in ords:
    norm = np.linalg.norm(matrix, ord=ord)
    norms.append(norm)
  eig = list(np.linalg.eig(matrix)[0])
  eig = [np.absolute(e) for e in eig]
  eig.sort()
  norms += eig[0:10]
  return norms

def metrics(matrices):
  norms_list = []
  for matrix in matrices:
    matrix_norms = compute_norms(matrix)
    norms_list.append(matrix_norms)
  return norms_list
