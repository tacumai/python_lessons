import random

lebel = int(input())

switch lebel
  when 0
    NUM = random.randint(1, 10)
    MAX_COUNT = 3
  when 1
    NUM = random.randint(1, 100)
    MAX_COUNT = 6
  when 2
    NUM = random.randint(1, 1000)
    MAX_COUNT = 10

COUNT = 0

while True:
  print('入力：', end='')
  n = int(input())
  COUNT += 1
  if n == NUM:
    break;
  if COUNT == MAX_COUNT:
    print('{}回失敗してしまいました。ゲームオーバーです。'.format(MAX_COUNT))
    exit()
  if n > NUM:
    print('もっと小さな数です')
  else:
    print('もっと大きな数です')

print('あたりです!おめでとうございます!')
print('{}回目の入力で一致しました。'.format(COUNT))
