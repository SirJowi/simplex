import numpy as np

q = np. array([3, -5, 2, -3, 1.])
for i in range(len(q)):
    if q[i] < 0:
        q[i] = np.inf

piv_r = np.argmin(q)

print(piv_r)