import math
numbers = [-3, -5, 1, 4]
print(list(map(lambda x: 1  / (1  + math.exp(-x)), numbers)))