import numpy as np

x = np.arange(1, 101, dtype=int)
diff = x.sum()**2 - np.square(x).sum()
print(diff)
