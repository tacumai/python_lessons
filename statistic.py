import math

# 合計を求める
def get_sum(data_list):
  sum = 0
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

# 偏差平方和を求める
def get_sum_square_deviation(data_list):
  avg = get_avg(data_list)
  result = 0
  for d in data_list:
    result += (d - avg)**2
  return math.sqrt(result)

# 標準偏差を求める
def get_standard_disp(data_list):
  disp = get_disp(data_list)
  return math.sqrt(disp)

# 共分散を求める
def get_covariance(data_lists):
  covariance = 0
  avg_x = get_avg(data_lists[0])
  avg_y = get_avg(data_lists[1])
  for (x, y) in zip(data_lists[0], data_lists[1]):
    diff_x = x - avg_x
    diff_y = y - avg_y
    diff_product = diff_x * diff_y
    covariance += diff_product
  return covariance

# 相関係数を求める
def get_correlation_coefficient(data_lists):
  covariance = get_covariance(data_lists)
  x = get_sum_square_deviation(data_lists[0])
  y = get_sum_square_deviation(data_lists[1])
  r = covariance / (x * y)
  return r

def collect_data():
  print('配列の要素数を入力してください（数字のみ）')
  ary_count = int(input())
  data_lists = []
  while True:
    print('{}つの数値を半角スペース区切りで入力してください'.format(ary_count))
    data = str(input())
    ary = list(map(int, data.split()))
    if len(ary) != ary_count:
      print('入力したデータの個数が異なります。もう一度やり直してください')
    else:
      data_lists.append(ary)
    if len(data_lists) == 2: break
  return data_lists

data_lists = collect_data()   # 必要なデータを集める
correlation_coefficient = get_correlation_coefficient(data_lists)  # 相関係数を求める
print('入力した二つのデータ群の相関係数は、 {} となりました。'.format(correlation_coefficient))  # 相関係数を出出力する
