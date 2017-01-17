import random

NUM = random.randint(1, 10)

print('数を当ててください。(1〜10の中にあります）')

while True:
  print('入力：', end='')
  n = int(input())
  if n == NUM:
    break;
  if n > NUM:
    print('もっと小さな数です')
  else:
    print('もっと大きな数です')
print('あたりです!おめでとうございます!')
