import random


def make_score_lists():
  STUDENT_COUNT = 3000
  MAX_SCORE = 198
  MIN_SCORE = 0
  n = 0
  score_lists = []
  while n < STUDENT_COUNT:
    score = random.randint(MIN_SCORE, MAX_SCORE) * 5
    score_lists.append(score)
    n += 1
  return score_lists

def make_rank_dict(score_lists):
  # 階級値をまとめたディクショナリー
  rank_dict = {
    '0-100': 0,
    '101-200': 0,
    '201-300': 0,
    '301-400': 0,
    '401-500': 0,
    '501-600': 0,
    '601-700': 0,
    '701-800': 0,
    '801-900': 0,
    '901-990': 0
  }
  for score in score_lists:
    if score in range(0, 101):
      rank_dict['0-100'] += 1
    elif score in range(101, 201):
      rank_dict['101-200'] += 1
    elif score in range(201, 301):
      rank_dict['201-300'] += 1
    elif score in range(301, 401):
      rank_dict['301-400'] += 1
    elif score in range(401, 501):
      rank_dict['401-500'] += 1
    elif score in range(501, 601):
      rank_dict['501-600'] += 1
    elif score in range(601, 701):
      rank_dict['601-700'] += 1
    elif score in range(701, 801):
      rank_dict['701-800'] += 1
    elif score in range(801, 901):
      rank_dict['801-900'] += 1
    else:
      rank_dict['901-990'] += 1
  return rank_dict

def calc_mode(score_lists):
    rank_dict = make_rank_dict(score_lists)
    rank_mode = max(rank_dict.values())
    for key, value in rank_dict.items():
      if value == rank_mode:
        return key

# 実際に実行している部分
score_lists = make_score_lists()
print("もっとも人数が多かったスコア幅は{}点代でした。".format(calc_mode(score_lists)))
