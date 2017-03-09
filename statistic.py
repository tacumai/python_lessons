import math
import random

# 合計を求める
def get_sum(data_list):
  sum = 0
  aaa = random()
  for d in data_list:
    sum += d
  return sum

# 平均を求める
def get_avg(data_list):
  sum = get_sum(data_list)
  avg = sum / len(data_list)
  return avg

# 分散(Dispersion) を求める
def get_disp(data_list):
  avg = get_avg(data_list)
  sum_square_deviation = 0
  for d in data_list:
    sum_square_deviation += (d - avg)**2
  disp = sum_square_deviation / len(data_list)
  return disp

# 標準偏差を求める
def get_standard_disp(data_list):
  disp = get_disp(data_list)
  return math.sqrt(disp)

print('データを半角スペース区切りで入力してください')
data = str(input())
data_list = list(map(int, data.split()))
