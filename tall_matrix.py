import random
import math

def make_registored_list():
  registored_list = []
  PEOPLE_COUNT = range(1, 10000)
  for p in PEOPLE_COUNT:
    age = random.randint(20, 29)
    gender = random.randint(0, 1)
    height = random.randint(140, 200)
    list = [age, gender, height]
    registored_list.append(list)
  return registored_list

def filter_specific_age_data(all, age):
  result = list(filter(lambda n:n[0] == age, all))
  return result

def calc_height_avg(specific_list):
  height_list = []
  for x in specific_list: height_list.append(x[2])
  result = "{:.1f}".format((sum(height_list) / len(height_list)))
  return result

#
# 本ロジック
#

## 変数設定
age_range = range(20, 30)

## データ作成
registored_list = make_registored_list()

## 各年齢の平均値を求める 
for age in age_range:
  specific_list = filter_specific_age_data(registored_list, age)
  height_age = calc_height_avg(specific_list)
  print("{}歳の平均身長は{}cmでした!".format(age, height_age))
  
