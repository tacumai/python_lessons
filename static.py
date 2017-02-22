import math
data_sum = 0
print('データを半角スペース区切りで入力してください')
data = str(input())
data_list = data.split()

for d in data_list:
  data_sum += int(d)
data_avg = data_sum / len(data_list)
data_disp = 0
sum_double_deviation = 0

for d in data_list:
  sum_double_deviation += (int(d) - data_avg)**2

data_disp = sum_double_deviation / len(data_list)


print('スコアの合計は{sum}です。'.format(sum = data_sum))
print('スコアの平均点は{avg}です。'.format(avg = data_avg))
print('スコアの分散は{disp}です。'.format(disp = data_disp))
print('スコアの標準偏差は{standard_disp}です。'.format(standard_disp = math.sqrt(data_disp)))
