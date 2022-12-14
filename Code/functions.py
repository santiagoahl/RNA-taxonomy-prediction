# -*- coding: utf-8 -*-
"""functions.ipynb

Author: @santiagoahl

Original file is located at
    https://colab.research.google.com/drive/1PgS1mng61oFn8G0rdqXqhYvhI4BxsoX3
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def get_data(taxonomy, df):
  """
  Input: Taxonomy name
  Output: 
    - data: List of ARN Chains for each taxonomy name
    - cod: List of unique codons of the taxonomy
  """
  data = df[df['Taxonomy']==taxonomy]['Codons']
  cod = []
  for b in data:
    cod+=b
  cod = list(set(cod))  # Select unique values
  return data, cod

def compute_codons(chain):
  """
  Input: ARN sequence string
  Output: ARN sequence of codons (List of 3-long-strings)
  """
  codons = [chain[i:i+3] for i in range(0, len(chain),3) if len(chain[i:i+3])==3]
  return codons

def prob(prev, post, chain):
  """
  Input: ARN chain sliced by codons and two codons.
  Params:
    - prev = str. Specific codon which stays at first position, this parameter is obligatory. 
    - post = str. Specific codon which stays at second position, this parameter is obligatory. 
    - chain = str. Sequence of codons
  Output:
    - probability = float32. Probability of the event "codon prev is observed before codon post"
  """
  occurrences = 0
  for cod_index in range(len(chain)-1):
    #print('\n ok \n')
    codon = chain[cod_index]
    next_codon = chain[cod_index+1]
    #print(type(codon), type(next_codon))
    #print(codon, next_codon)
    if (codon == prev) & (next_codon == post):
      occurrences+=1
    #print(occurrences)
  probability = occurrences/len(chain)
  #print('Prob ', str(prev)+'+'+str(post)+' :',occurrences/len(chain))
  return probability

def transition_matrix(chain, codons):
  """
  Input: ARN chains and codons of a unique taxonomy
  Output: Transition matrix as npArray
  """
  matches = {i:codons[i] for i in range(len(codons))}
  #print('\n', matches, '\n')
  #print(type(matches[0]))
  #print('hi')
  #print(len(range(len(chain))))
  mat = [[prob(matches[i], matches[j], chain) for j in range(len(codons))] for i in range(len(codons))]
  mat = np.array(mat)
  return mat

def taxonomy_transition_matrices(tax_data, codons):
  """
  Input: 
    - tax_data := Set of chains of an unique taxonomy
    - codons := Different types of codons founded
  Output: List of transition matrices
  """
  matrices = []
  i=1
  for chain in tax_data:  
    if i%20==0:
      print(str(i), '/', len(tax_data))
    i=i+1
    matrix = transition_matrix(chain, codons)
    matrices.append(matrix)
  return matrices

def normalize_data(data, min, max, mat=False):
  """
  Input: Data, min of data and max of data
  Output: Normalized data (MinMax normalization)
  """
  if mat == True:
    #In case you just want to normalize a single matrix
    data = list(np.array(data)/max)
    return data
  for tax in data.keys():
    for i in range(len(data[tax])):
      data[tax][i]=list(np.array(data[tax][i])/max)
  return data

def classify(model, max_scaler, std_scaler, arn_seq, taxonomies, codons):
  #1. compute codons
  #2. compute tr mat
  #3. Normalize tr mat
  #4. compute metrics
  #5. Normalize
  #6. Predict
  arn_cod_seq = compute_codons(arn_seq)
  tran_matrix = transition_matrix(arn_cod_seq, codons)
  normalized_matrix = normalize_data(tran_matrix, 0, 0.0232, mat=True)
  metrics = np.array(compute_norms(normalized_matrix)).reshape(1, -1)
  normalized_metrics = max_scaler.transform(metrics) #Refactor
  data = std_scaler.transform(normalized_metrics) #Refactor
  prediction = model.predict(data)[0]
  print('Predicted taxonomy: ', prediction)
