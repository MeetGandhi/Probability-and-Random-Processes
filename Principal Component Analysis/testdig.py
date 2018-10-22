import pandas as pd
import sklearn
from sklearn import datasets
import numpy as np
import matplotlib as mt
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D

i=datasets.load_digits()
I=i['data']
I_=StandardScaler().fit_transform(I)
M_=np.mean(I_,axis=0)
Cov_Mat=(((I_-M_).T).dot(I_-M_))/(len(I_)-1)
E_Val,E_Vec=np.linalg.eig(Cov_Mat)

for d in E_Vec:
    np.testing.assert_array_almost_equal(1.0,np.linalg.norm(d))

E_L=[(np.abs(E_Val[j]),E_Vec[:,j]) for j in range(len(E_Val))]
E_L.sort(key=lambda x:x[0],reverse=True)

T=sum(E_Val)
PVar=[((i/T)*100) for i in sorted(E_Val, reverse=True)]
CPVar=np.cumsum(PVar)
plt.plot(PVar)
plt.ylabel('Percentage Explained Variance')
plt.xlabel('Principal Components')
plt.show()
plt.plot(CPVar)
plt.ylabel('Cumulative Explained Variance')
plt.xlabel('Principal Components')
plt.show()
e=input("\nEnter the desired number of reduced dimensions: ")
e=int(e)
E=np.hstack((E_L[s][1].reshape(len(I_[0]),1)) for s in range(e))
R=I_.dot(E)
print("\nResultant Dimensionally Reduced Data Vector: \n%s" %R)

if e==2:
    with plt.style.context('seaborn-whitegrid'):
        plt.figure()
        plt.scatter(R[:,0],R[:,1])
        plt.xlabel('Principal Component 1')
        plt.ylabel('Principal Component 2')
        plt.legend(loc='lower center')
        plt.tight_layout()
        plt.show()


if e==3:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    with plt.style.context('seaborn-whitegrid'):
        ax.scatter(R[:,0],R[:,1],R[:,2])
        ax.set_xlabel('Principal Component 1')
        ax.set_ylabel('Principal Component 2')
        ax.set_zlabel('Principal Component 3')
        plt.legend(loc='lower center')
        plt.tight_layout()
        plt.show()

RR=[0]*len(R)
if e==1:
    with plt.style.context('seaborn-whitegrid'):
        plt.figure()
        plt.scatter(R[:,0],RR)
        plt.xlabel('Principal Component 1')
        plt.legend(loc='lower center')
        plt.tight_layout()
        plt.show()
