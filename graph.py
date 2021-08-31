import pandas as pd
data = pd.read_csv('sample.txt',sep='\s+',header=None)
data = pd.DataFrame(data)

import matplotlib.pyplot as plt
x = data[0]
y = data[1]
plt.bar(x, y,width = 0.8, color = ['red', 'green'])
plt.show()
