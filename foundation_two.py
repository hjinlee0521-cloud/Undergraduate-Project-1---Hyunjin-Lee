import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# #Numpy 1회차 
# #1차원 array
a1 = np.array([4, 5, 6, 4, 5])
# print(a1)
# print(type(a1))
# print(a1.shape) #1차원 배열
# print(a1[0], a1[1], a1[2], a1[3], a1[4])
# a1[0] = 4
# a1[1] = 5
# a1[2] = 6
# print(a1)

#2차원 array
a2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(a2)
# print(a2.shape)
# print(a2[0,1], a2[1,2])

#3차원 array
a3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
# print(a3)
# print(a3.shape)

#배열 생성 및 초기화
#zeros() --> 모든 요소를 0 으로 초기화
# np.zeros(10)
# print(np.zeros(10))

# np.ones((3,3))
# print(np.ones((3,3)))

# np.full((3,3), 1.5)
# print(np.full((3,3), 1.5))

# np.eye(3) #identity matrix 
# print(np.eye(3))

# np.tri(3) #삼각 매트릭스
# print(np.tri(3))

# np.zeros_like(a1)
# print(np.zeros_like(a1))

# np.ones_like(a2)
# print(np.ones_like(a2))

# np.full_like(a3, 10)
# print(np.full_like(a3, 10))

# print(np.arange(0, 30, 2))

# print(np.linspace(0, 1, 5))

# print(np.logspace(0.1, 1, 20))

# print(np.random.random((3, 3)))

# print(np.random.randint(0, 10, (3,3)))

# print(np.random.normal(0, 1, (3, 3)))

# print(np.random.rand(3, 3))

# print(np.zeros(20, dtype = bool))

# date = np.array('2026-03-08', dtype = np.datetime64)
# print(date)
# print(date + np.arange(12))

#배열 조회
def array_info(array):
    print(array)
    print("ndim:", array.ndim)
    print("shape:", array.shape)
    print("dtype:", array.dtype)
    print("size:", array.size)
    print("itemsize:", array.itemsize)
    print("nbytes:", array.nbytes)
    print("strides:", array.strides)

# array_info(a1)
# array_info(a2)
# array_info(a3)

#인덱싱
# print(a1[0])
# print(a1[-1])

# print(a2)
# print(a2[1,1])
# print(a2[-1, 0])

# print(a3)
# print(a3[1,2,0])

#slicing
# print(a1)
# print(a1[0:2])
# print(a1[0:])
# print(a1[::2]) #스텝이 2개씩
# print(a1[::-1])

#boolean indexing
# bi = [False, True, True, False, True]
# print(a1)
# print(a1[bi])

# print(a2)
# bi = np.random.randint(0, 2, (3,3), dtype = bool)
# print(bi)
# print(a2[bi])

# print(a1)
# print([a1[0], a1[2]])
# ind = [0, 2]
# print(a1[ind])


#배열 값 삽입
#1차원
# print(a1)
# b1 = np.insert(a1, 0, 10) #a1의 0번째 위치에 10을 넣어줘
# print(b1)
# print(a1)

#2차원
# print(a2)
# b2 = np.insert(a2, 1, 10, axis = 0)
# print(b2)

# c2 = np.insert(a2, 1, 10, axis = 1)
# print(c2)


#배열 값 수정
# a1[0] = 1
# a1[1] = 2
# a1[2] = 3
# print(a1)

# a1[:1] = 9
# print(a1)
# i = np.array([1, 3, 4])
# a1[i] = 0
# print(a1)
# a1[i] += 4
# print(a1)

# print(a2)
# a2[0,0] = 1
# a2[1,1] = 2
# a2[2,2] = 3
# a2[0] = 1
# print(a2)


#배열 값 삭제
# print(a1)
# b1 = np.delete(a1, 1)
# print(b1)

# print(a2)
# b2 = np.delete(a2, 1, axis = 0)
# print(b2)

# c2 = np.delete(a2, 1, axis = 1)
# print(c2)


#배열 복사
# print(a2)
# a2_sub_copy = a2[:2, :2].copy()
# print(a2_sub_copy)


#배열 변환
#배열 전치 및 축 변경
# print(a2)
# print(a2.T) #!!!Transpose A^T

# print(a2.swapaxes(0, 1))


#배열 재구조화
# n1 = np.arange(1, 10)
# print(n1)
# print(n1.reshape(3, 3))

# print(n1[np.newaxis, :5])
# print(n1[:5, np.newaxis])


#배열 모양만 변경
# n2 = np.random.randint(0, 10, (2, 5))
# print(n2)
# n2.resize((5, 2))
# print(n2)

# n2.resize((3, 3))
# print(n2)

#배열 추가
# a2 = np.arange(1, 10).reshape(3, 3)
# print(a2)
# b2 = np.arange(10, 19).reshape(3, 3)
# print(b2)


# c2 = np.append(a2, b2, axis = 0)
# print(c2)

#배열 연결
# a1 = np.array([1, 3, 5])
# b1 = np.array([2, 4, 6])
# print(np.concatenate([a1, b1]))

# a2 = np.array([[1, 2, 3], [4, 5, 6]])
# print(np.concatenate([a2, a2]))
# print(np.concatenate([a2, a2], axis = 1))

# print(np.vstack([a2, a2]))
# print(np.hstack([a2, a2]))

# print(np.dstack([a2, a2]))
# print(np.stack([a2, a2]))

#배열 분리
# a1 = np.arange(0, 10)
# print(a1)
# b1, c1 = np.split(a1, [5])
# print(b1, c1)

# b1, c1, d1, e1, f1 = np.split(a1, [2, 4, 6, 8])
# print(b1, c1, d1, e1, f1)

# a2 = np.arange(1, 10).reshape(3, 3)
# print(a2)
# b2, c2 = np.vsplit(a2, [2])
# print(b2)
# print(c2)

#중요!!!!!!!!!!!! matrix에서 vector로 분리 가능
a2 = np.arange(1, 10).reshape(3, 3)
print(a2)
b2, c2 = np.hsplit(a2, [2])
print(b2)
print(c2)


#배열 연산
#브로드캐스팅
# a1 = np.array([1, 2, 3])
# print(a1)
# print(a1 + 5)

# a2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(a2)
# print(a1 + a2)

# b2 = np.array([1, 2, 3]).reshape(3, 1)
# print(b2)
# print(a1 + b2)


#산술 연산
# a1 = np.arange(1, 10)
# print(a1 + 1)
# print(np.add(a1, 10))
# print(a1 - 2)
# print(np.subtract(a1, 10))
# print(-a1)
# print(np.negative(a1))
# print(a1 * 2)
# print(np.multiply(a1, 2))
# print(a1 / 2)
# print(np.divide(a1, 2))
# print(a1 // 2)
# print(np.floor_divide(a1, 2))
# print(a1 ** 2)
# print(np.power(a1, 2))
# print(a1 % 2)
# print(np.mod(a1, 2))

# b1 = np.random.randint(1, 10, size = 9)
# print(a1)
# print(b1)
# print(a1 + b1)
# print(a1 - b1)
# print(a1 * b1)
# print(a1 / b1)
# print(a1 // b1)
# print(a1 ** b1)
# print(a1 % b1)

# a2 = np.arange(1, 10).reshape(3, 3)
# print(a2)
# b2 = np.random.randint(1, 10, size = (3, 3))
# print(b2)
# print(a2 + b2)
# print(a2 - b2)
# print(a2 * b2)
# print(a2 / b2)
# print(a2 // b2)
# print(a2 % b2)

# a1 = np.random.randint(-10, 10, size = 5)
# print(a1)
# print(np.abs(a1))

# print(a1)
# print(np.square(a1))
# print(np.sqrt(a1))


# a1 = np.random.randint(1, 10, size = 5)
# print(a1)
# print(np.exp(a1))
# print(np.exp2(a1))

#삼각함수
# t = np.linspace(0, np.pi, 3)
# print(t)
# print(np.sin(t))
# print(np.cos(t))
# print(np.tan(t))


# a2 = np.random.randint(1, 10, size = (3, 3))
# print(a2)
# # print(a2.sum(), np.sum(a2, axis = 0))

# print(a2.cumsum(), a2.cumsum(axis = 0))

#dot prods and matrix multiplications
# a2 = np.random.randint(1, 10, size = (3, 3))
# b2 = np.ones_like(a2)
# print(b2)
# print(np.dot(a2, b2))
# print(np.matmul(a2, b2))

#cross products
# x = [1, 2, 3]
# y = [4 ,5 ,6]
# print(np.cross(x, y))


#mean/standard dev/variance
# print(a2)
# print(np.mean(a2))
# print(np.mean(a2, axis = 0))
# print(np.mean(a2, axis = 1))

# print(np.std(a2))
# print(np.std(a2, axis = 0))
# print(np.std(a2, axis = 1))

# print(np.var(a2))
# print(np.var(a2, axis = 0))
# print(np.var(a2, axis = 1))

#min and max
# print(np.min(a2))
# print(np.min(a2, axis = 0))
# print(np.min(a2, axis = 1))

# print(np.max(a2))
# print(np.max(a2, axis = 0))
# print(np.max(a2, axis = 1))

#argmin & argmax --> 최소/최대 값의 위치(인덱스)
# print(np.argmin(a2))
# print(np.argmin(a2, axis = 0))
# print(np.argmin(a2, axis = 1))

#median
# print(np.median(a2))
# print(np.median(a2, axis = 0))
# print(np.median(a2, axis = 1))


#percentile
# a1 = np.array([0, 1, 2, 3])
# print(a1)
# print(np.percentile(a1, [0, 20, 40, 60 ,80, 100]))

#any
# a2 = np.array([[False, False, False], 
#                [False, True, True],
#                [False, True, True]])
# print(a2)
# print(np.any(a2))
# print(np.any(a2, axis = 0))
# print(np.any(a2, axis = 1))


#all
# a2 = np.array([[False, False, True], 
#                [True, True, True],
#                [False, True, True]])
# print(a2)
# print(np.all(a2))
# print(np.all(a2, axis = 0))
# print(np.all(a2, axis = 1))


#비교 연산자
# a1 = np.arange(1, 10)
# print(a1)
# print(a1 == 5)
# print(a1 != 5)
# print(a1 < 5)
# print(a1 <= 5)
# print(a1 > 5)
# print(a1 >= 5)

# a2 = np.arange(1, 10).reshape(3, 3)
# print(a2)
# print(np.sum(a2))
# print(np.count_nonzero(a2 > 5))
# print(np.sum(a2 > 5))
# print(np.sum(a2 > 5, axis=0))
# print(np.sum(a2 > 5, axis=1))

# a1 = np.array([1, 2, 3, 4, 5])
# print(a1)
# b1 = np.array([1, 2, 3, 3, 4])
# print(b1)
# print(np.isclose(a1, b1))


# a1 = np.array([np.nan, 2, np.inf, 4, -np.inf])
# print(a1)
# print(np.isnan(a1))
# print(np.isinf(a1))
# print(np.isfinite(a1))


#불리언 연산자
# a2 = np.arange(1, 10).reshape(3, 3)
# print(a2)

# print((a2 > 5) & (a2 < 8))
# print(a2[(a2 > 5) & (a2 < 8)])


#배열 정렬
# a1 = np.random.randint(1, 10, size=10)
# print(a1)
# print(np.sort(a1))
# print(a1)
# print(np.argsort(a1)) #위치 값
# print(a1)
# a1.sort()
# print(a1)

# a2 = np.random.randint(1, 10, size=(3, 3))
# print(a2)
# print(np.sort(a2))
# print(np.sort(a2, axis=0))
# print(np.sort(a2, axis=1))


# a1 = np.random.randint(1, 10, size=19)
# print(a1)
# print(np.partition(a1, 3)) #배열에서 가장 작은 k개를 반환 시켜줘


#배열 입출력
# a2 = np.random.randint(1, 10, size = (5, 5))
# np.save("a", a2)

# b2 = np.random.randint(1, 10, size = (5, 5))
# np.savez("ab", a2, b2)

# npy = np.load("a.npy")

# npz = np.load("ab.npz")
# # print(npz.files)
# # print(npz['arr_0'])
# # print(npz['arr_1'])


# print(a2)
# np.savetxt("a.csv", a2, delimiter=',', fmt='%.2e', header = 'c1, c2, c3, c4, c5')

# csv = np.loadtxt("a.csv", delimiter = ',')
# print(csv)










