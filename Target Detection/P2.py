import numpy as np

N=input("Enter N:")
N=int(N)

S=np.random.rand(N,1)*10

X=np.random.rand(N,1)*10

if np.matmul(X.transpose(),S) > 0.5*(np.matmul(S.transpose(),S)):
    print("Target Detected!")
    print("Sent Signal:\n",S)
    print("Received Signal:\n",X)
else:
    print("Target not Detected!")
    print("Sent Signal:\n",S)
    print("Received Signal:\n",X)
    
    
        

