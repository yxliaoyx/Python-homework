import numpy as np

np.random.seed(100)
X = np.random.rand(1000, 10)

K = np.dot(X, X.T)
d = np.diag(K)

D = np.power(d.reshape(1000, 1) + d.reshape(1, 1000) - 2 * K, 0.5)
print(D)

print((D < 2).sum() // 2)
print(len(D[D < 2]) // 2)

P = np.array(np.where(D < 2))
print(P)

D[range(len(D)), range(len(D))] = -1
print(np.argsort(D, axis=0)[1])

'''
計算矩陣 D，其中 D[i,j]表示第 i 個樣本與第 j 個樣本的歐幾里德距離。不要用迴圈指令計算。
不要用迴圈指令計算有多少對樣本間距離小於 2 ((i,j)與(j,i)是相同樣本對)
不要用迴圈指令計算矩陣 P，其中 P[i,0], P[i,1]表示樣本 P[i,0]與樣本 P[i,1]間距離小於 2。
不要用迴圈指令找到每個樣本最近的樣本的在 X 裡的列號(不可以是自己，若有兩個以上最近樣本則任選其中一個)
'''
