from toolbox_02450 import jeffrey_interval
from ex7_1_1 import *

# Compute the Jeffreys interval
alpha = 0.05
alpha = 0.01
[thetahatA, CIA] = jeffrey_interval(y_true, yhat[:,0], alpha=alpha)

print('knn (k=1)')
print("Theta point estimate", thetahatA, " CI: ", CIA)

### AddByMe (Gonzalo Mazzini)

[thetahatA, CIA] = jeffrey_interval(y_true, yhat[:,1], alpha=alpha)
print('knn (k=20)')
print("Theta point estimate", thetahatA, " CI: ", CIA)

[thetahatA, CIA] = jeffrey_interval(y_true, yhat[:,2], alpha=alpha)
print('knn (k=80)')
print("Theta point estimate", thetahatA, " CI: ", CIA)
