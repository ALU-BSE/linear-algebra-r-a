# import pandas as pd
# import numpy as np

# Load data
#data = pd.read_csv('path/to/data')

# Example arrays
Prices = [[300, 500],
          [1000, 120.85]]

Array2 = [200, 100]

# Calculate the result
Ans = []
# (300*200 + 500*100) as an example calculation

#The completed multiplication logic
for i in range(len(Prices)):
    row_sum = 0
    for j in range(len(Prices[0])):
       row_sum += Prices[i][j] * Array2[j] #This line calculates the total cost for all items in the ith row of the Prices list and accumulates it in row_sum.
    Ans.append(row_sum) #This adds the total cost for "i"th row to the "Ans" list so that it can be accessed later.
    pass
print(Ans)

NAMES:-RURANGWA Prince
      -IRAKOZE Amandine
