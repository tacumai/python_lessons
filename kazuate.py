import random

NUM = random.randint(1, 10)
COUNT = 0

print('数を当ててください。(1〜10の中にあります）')

while True:
  print('入力：', end='')
  n = int(input())
  COUNT += 1
  if n == NUM:
    break;
  if n > NUM:
    print('もっと小さな数です')
  else:
    print('もっと大きな数です')
print('あたりです!おめでとうございます!')
print('{}回目の入力で一致しました。'.format(COUNT))
