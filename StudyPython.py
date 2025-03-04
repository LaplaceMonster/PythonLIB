import os

L = list(range(100))
print(L[0:10])
print(L[10:20])
print(L[0::5])
L=[x*x for x in range(1,11) if x%2==0]
print(L)