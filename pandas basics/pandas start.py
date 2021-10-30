# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 12:24:14 2021

@author: pc
"""

# 1) pandas hızlı ve etkili for dataframes
# 2) cvs and text dosyaları açıp inceleyip sonuçlarımızı bu dosya tiplerine rahat bir şelilde kaydedebilir.
# 3) pandas bizim işimizi kolaylaştırıyor for missing data
# 4) reshap yapıp datayı daha etkili bir şekilde kullanabiliriz
# 5) slicing indexing kolay
# 6) time series data analizinde çok yardımcı
# 7) herşeyden önemlisi hız pandas hız açısından optimize edilmiş hızlı bir kütüphane

import pandas as pd

dictionary = {"NAME":["ali","veli","kenan","hilal","ayşe","evren"],
              "AGE":[15,16,17,33,45,66],
              "WAGE":[100,150,240,350,110,220]}

dataFrame1 = pd.DataFrame(dictionary)

head = dataFrame1.head()
tail = dataFrame1.tail()


# %%
# pandas basic method


print(dataFrame1.columns) # -> tablo colum adlarını döner

# info() methodu
# info() methodo tablonuntürünü type'ını döner
# kaç adet veri olduğunu
# index sıralamasının kaçta başladığı ve kaçta bittiği
# herbir satıra sample denilir
# colum sayısını
print(dataFrame1.info()) # 


# colonların typlarını döner
print(dataFrame1.dtypes)



# describe() methodu
# data hakkında numerik sayısal kollonlar hakkında
# count -> veri sayısı
# mena -> ortalam
# std / standart devition -> 
# min and max
# %25, %50, %75 medyan değerleri
# %50 medyan değeri (sıralı verilerde ortanca değer)
print(dataFrame1.describe())



# %%
# indexing and slicing

print(dataFrame1["AGE"])
print(dataFrame1.AGE)

dataFrame1["yeni feature"] = [-1,-2,-3,-4,-5,-6]
print(dataFrame1["yeni feature"])

print(dataFrame1.loc[:,"AGE"])
print(dataFrame1.loc[:3,"AGE"])

print(dataFrame1.loc[:3,"NAME":"WAGE"])

print(dataFrame1.loc[:3,["AGE","NAME"]])


print(dataFrame1.loc[::-1,:])


# AGE'e kadar olan tüm satırları yazdır AGE kolonu dahil
print(dataFrame1.loc[:,:"AGE"])




print(dataFrame1.loc[:,"NAME"])
print(dataFrame1.iloc[:,0])  # i -> integer


# %%
# filtering data frame

filtre1 = (dataFrame1.WAGE > 200)
filtrelenmis_data = dataFrame1[filtre1]

filtre2 =  dataFrame1.AGE < 20

print(dataFrame1[filtre1 & filtre2])


print(dataFrame1[dataFrame1.AGE < 20])




# %% 
# List comprehension - anlamak


import numpy as np
# numpy ile maaş'ların ortalamasını hesaplama
ortalama_maas_np = np.mean(dataFrame1.WAGE)

# pandas ile maaş ortalama hesaplama
ortalama_maas = dataFrame1.WAGE.mean()


# maas_seviyesi adında bir kolon oluştur ve maaşı ortalamanın altında olan veriler için düşük, üstünde olanlar için yüksek yazdır.
dataFrame1["maas_seviyesi"] = [ "dusuk" if ortalama_maas > each else "yüksek" for each in dataFrame1.WAGE]


# dataFrame1 içindeki colon adlarının tümünü küçük harflerle yazılmış kelimelere dönüştür
dataFrame1.columns = [each.lower() for each in dataFrame1.columns]

dataFrame1.columns = [ each.split()[0]+"_"+each.split()[1] if(len(each.split())>1) else each for each in dataFrame1.columns]



# %%
# drop and concatenating (birleştirici)


# yeni_feature kolonunu tablodan kaldırı siler
# axis=1 bu drop() işleminin kolonlar geçerli olduğunu belirtir
# inplace=True drop() ilemi sonucu oluşan tabloyu değişkenimiz (dataFrame1) üzerine kaydeder bu "inplace=True" parametresini vermessek drop() methodu sonucu oluşacak yeni tavlo return edilir fakat değişkenimizin değerinde bir değişiklik olmaz
dataFrame1.drop(["yeni_feature"],axis=1,inplace=True)


data1 = dataFrame1.head()
data2 = dataFrame1.tail()

#vertical concatenating / dikey birleştirme satırları alt alta birleştirir
data_concat_v = pd.concat([data1,data2],axis=0)

# horizontel concatenating  / iki kolonu billeştirelim
maas = dataFrame1.wage
age = dataFrame1.age
data_concat_h = pd.concat([age,maas],axis=1)


# %%
# transforming data

dataFrame1["list_comp"] = [each*2 for each in dataFrame1.age]


# apply(custom_fuction())
def multiply(age):
    return age*2

dataFrame1["apply_methodu"] = dataFrame1.age.apply(multiply)
















