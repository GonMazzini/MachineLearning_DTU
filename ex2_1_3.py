# exercise 2.1.3
# plot Variance Explained vs # PCs
# (requires data structures from ex. 2.2.1)

from ex2_1_1 import *

import matplotlib.pyplot as plt
from scipy.linalg import svd


# First SUBSTRACT THE MEAN !!! 
# Subtract mean value from data
Y = X - np.ones((N,1))*X.mean(axis=0)

# PCA by computing SVD of Y
U,S,V = svd(Y,full_matrices=False)

# np.shape(U)   (90,8)
# np.shape(S)   (8,)
# np.shape(V)   (8,8)

# Compute variance explained by principal components
rho = (S*S) / (S*S).sum() 

threshold = 0.9

# Plot variance explained
plt.figure()
plt.plot(range(1,len(rho)+1),rho,'x-')
plt.plot(range(1,len(rho)+1),np.cumsum(rho),'o-')
plt.plot([1,len(rho)],[threshold, threshold],'k--')
plt.title('Variance explained by principal components');
plt.xlabel('Principal component');
plt.ylabel('Variance explained');
plt.legend(['Individual','Cumulative','Threshold'])
plt.grid()
plt.show()

print('Ran Exercise 2.1.3')