# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 14:29:06 2021

@author: pc
"""

import numpy as np



array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(array)
print(array.shape) # 15, or 15,1

a = array.reshape(3,5)
print(a)
print("shape: {0}".format(a.shape))
print("dimension: ", a.ndim) #dizi boyutu
print("data type: ",a.dtype.name) # >>out: int32
print("size: ",a.size) # >>out: 15
print("type: ",type(a))

array1 = np.array([
    [1,2,3,4,5],
    [3,6,9,8,8],
    [3,6,9,8,8],
    ])

b = np.zeros((3,4)) # 3 row and 4 colum
print(b)

# %% relocation -> yer ayırma
"""relocation işlemini maliyetli işlemlerde maliyeti azaltmak için kullanırız
örneğin dizimize append() methoduyle eleman eklemek dizimiz çok büyükse uylamayı yoracaktır
bu yüzden append() methodu yerine dizimize zeros() gibi methodlarla relocation işlemi uygularız
ve dizimize eklenen yeni değerleri istediğimiz şekilde ihtiyacımız doğrultusunda güncelleriz"""
zeros = np.zeros((3,4))
print(zeros)
zeros[0,0] = 5
print(zeros)

ones = np.ones((3,3))
print(ones)

empty = np.empty((3,3))
print(empty)

range_array = np.arange(10,50,5)
print(range_array) #out 1 (one) dimension -> [10 15 20 25 30 35 40 45]


x = np.linspace(10,50,20) #10 dan 50'ye kadar 20'li dizi oluşturur.
print(x)

# %%

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)
print(a-b)
print(a**2)

print(np.sin(a))
print(a<2)


a = np.array([[1,2,3,],[4,5,6]])
b = np.array([[1,2,3,],[4,5,6]])

print(a)
print(b)

# element wise product tüm elemanlar karşılıklı çarpılır matris çarpımı değildir
print(a*b)

# matrix product
# a.dot(b)  dizi boyutları eşit olduğundan hataverir bu yüzden b'nin transpozu alınır
print(a.dot(b.T))


# exponential -> üstel
print(np.exp(a)) 

# random
a = np.random.random((5,5))
print(a)

print(a.sum())
print(a.max())
print(a.min())


# colonları toplar
print(a.sum(axis=0)) 

# satırları toplar
print(a.sum(axis=1)) 


# kare kök alma
print(np.sqrt(a))

# kare alma
print(np.square(a))


# iki diziyi toplama a+a
print(np.add(a,a))
print(np.add(a,a) == a+a)


# %% indexing and slicing -> indeksleme ve dilimleme

array = np.array([1,2,3,4,5,6,7])  # vektör dimension = 1 tek boyutlu demek
print(array)

print(array[0])
print(array[:])

reverse_array = array[::-1]
print(reverse_array)

print("\n")

array1 = np.array([np.arange(1,6),np.arange(6,11)])
print("shape:",array1.shape)
array1 = np.array(np.arange(1,11)).reshape(2,5)
print(array1)

# row = 1 and collum = 0
print(array1[1,0]) 


# index'i 1 olan colonu alma
print(array1[:,1])


# sadece 2. datırı yani 1. indexdeki kolonları getirir
print(array1[1,:])


# satırlardan 1. index'i ve colonlardan 2. ile 4. index arasındakileri getir 
# 4. index dahildeğil
print(array1[1,2:4])


# dizinin son satırını alma
print(array1[-1,:])

# dizinin son kolonunu alma
print(array1[:,-1:])


# %% 
# shape manipulation
array = np.arange(1,10).reshape(3,3)
print(array)

# flatten -> düzleştirme #diziyi vektöre çevirir
a = array.ravel()
print(a)

array2 = a.reshape(3,3)
print(array2)


array_Transpose = array2.T
print(array_Transpose)


# !!!!!!!!!! resize() and reshape
print("\n\n\n ****** resize() and reshape() ******")
"""
iki methodda aynı işi yapar fakat 
    reshape() ile yapılan yeniden buyutlandırma
işlemi uygulanılan değişkenin değerini değiştirmez sadece geriye yeni
yeni boyutlandırılmış veriyi return eder döner ve bizde bu değeri yeni 
yeni tanımladığımız bir değişkene atarız fakat
    rezize() methodunda yeniden buyutlandırma işlemi uygulanılan değişken 
bu değişiklikten etkilenir return etmez direk değişkenimiz etkilenir
"""

array = np.arange(1,7).reshape(3,2)
print(array,"\n \n")


array.reshape(2,3)
print("array.reshape(2,3) \n",array)

array.resize(2,3)
print("array.resize(2,3) \n",array)


# %%
# stacking arrays -> iki diziyi birleştirme

array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])

# vertical
# array([[ 1, 2],
#        [ 3, 4],
#        [-1,-2],
#        [-3,-4]])

arrayV = np.vstack((array1,array2))
print(arrayV)




# horizontal
#array([[1, 2,-1, -2],
#      [3, 4,-3, -4]])

arrayH = np.hstack((array1,array2))
print(arrayH)










