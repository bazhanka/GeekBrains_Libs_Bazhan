import numpy as np
#1
a = np.array([[1,6],[2,8],[3,11],[3,10],[1,7]])
index = 0
col1 = []
col2 = []
mean_a = []
while index < len(a):
    col1.append(a[index][0])
    col2.append(a[index][1])
    index+=1
mean_a.append(np.mean(col1))
mean_a.append(np.mean(col2))
print(mean_a)
#2
a_centered = a-mean_a
print(a_centered)
#3
index_c = 0
col1_ = []
col2_ = []
while index_c < len(a_centered):
    col1_.append(a_centered[index_c][0])
    col2_.append(a_centered[index_c][1])
    index_c+=1
col1_c = np.array(col1_)
col2_c = np.array(col2_)
a_centered_sp = col1_c @ col2_c
print(a_centered_sp/(len(a_centered)-1))
#4
A = a
print(np.cov(A.T))