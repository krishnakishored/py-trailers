from numpy import *
from numpy.random import * #for randn
from numpy.linalg import inv

from KalmanFilter import *
#time step of mobile movement
dt = 0.1
# Initialization of state matrices
X = array([[0.0], [0.0], [0.1], [0.1]])
#print("X:{} ".format(X))
P = diag((0.01, 0.01, 0.01, 0.01))
#print("P:{} ".format(P))

A = array([[1, 0, dt , 0], [0, 1, 0, dt], [0, 0, 1, 0], [0, 0, 0,1]])
#print("A:{} ".format(A))

#Q = eye(X.shape()[0])
Q = eye(X.shape[0])
#print("X.shape[0]:{}".format(X.shape[0]))
#print("Q:{}".format(Q))
B = eye(X.shape[0])
#print("B:{}".format(B))

U = zeros((X.shape[0],1))
#print("U:{}".format(U))

# Measurement matrices
Y = array([[X[0,0] + abs(randn(1)[0])], [X[1,0] + abs(randn(1)[0])]])
#print("Y:{}".format(Y))

H = array([[1, 0, 0, 0], [0, 1, 0, 0]])
#print("H:{}".format(H))

R = eye(Y.shape[0])
#print("R:{}".format(R))

# Number of iterations in Kalman Filter
N_iter = 5 #50
# Applying the Kalman Filter
for i in arange(0, N_iter):
 (X, P) = kf_predict(X, P, A, Q, B, U)
 (X, P, K, IM, IS, LH) = kf_update(X, P, Y, H, R)
 print("#################################################")
 print("X:{}".format(X))
 print("P:{}".format(P))
 # print("K:{}".format(K))
 # print("IM:{}".format(IM))
 # print("IS:{}".format(IS))
 # print("LH:{}".format(LH))


 Y = array([[X[0,0] + abs(0.1 * randn(1)[0])],[X[1, 0] + abs(0.1 * randn(1)[0])]])
 #print("Y:{}".format(Y))
