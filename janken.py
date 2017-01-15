import random

RESULT = {
  'drawn': 'the game is drawn...',
  'win': 'you are winner!',
  'lose': ' you are lose...'
}

PATTERN = ['グー', 'チョキ', 'パー']

def judge(you, machine):
  if (you == machine):
    return RESULT['drawn']
  elif ((you == 0 and machine == 1) or (you == 1 and machine == 2) or (you == 2 and machine == 0)):
    return RESULT['win']
  else:
    return RESULT['lose']

def valid(you):
  if not you in range(0, 3):
    print('間違った値を入力しています。もう一度やり直してください。')
    main()

def main():
  print('以下の数値のいずれかを入力してください。')
  print('0: グー,   1: チョキ,  2:パー')
  you = int(input())
  valid(you)
  machine = random.randint(0, 2)
  result = judge(you, machine)
  print('あなたは、{}'.format(PATTERN[you]))
  print('相手は、{}'.format(PATTERN[machine]))
  print(result)
  if (result == RESULT['drawn']):
    print('あいこです。もう一度勝負してください。')
    main()

main()
