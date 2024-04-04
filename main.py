import numpy as np
from matplotlib import pyplot as plt
import random 

def step_function(x: float) -> float:
  return 1.0 if x >=0 else 0.0

def perceptron(weights: np.array, bias: float, x: np.array) -> float:
  calc = np.dot(weights, x) + bias
  return step_function(calc)

or_weights = np.array([random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)])

or_bias = -0.5

epochs = 10

l_rate = 0.1

yd = np.array([1, 1, 1, 0])

x = [ 
  np.array([1, 1]), 
  np.array([1, 0]), 
  np.array([0, 1]), 
  np.array([0, 0]),
]


for i in range(epochs):
  print("Epoch", i)
  print("Pesos", or_weights)
  print("Output:")
  for i in range(len(x)):
      y =  perceptron(or_weights, or_bias, x[i])
      error = yd[i] - y
      or_weights[0], or_weights[1]  = or_weights[0] + l_rate * x[i][0] * error, or_weights[1] + l_rate * x[i][1] * error
      print(y)
  print()
