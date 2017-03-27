from collections import defaultdict
import random

def make_score_lists():
  (STUDENT_COUNT, MAX, MIN, n) = (range(1, 3000), 198, 0, 0)
  score_list = [(random.randint(MIN, MAX) * 5) for i in STUDENT_COUNT]
  return score_list

def make_rank_dict(score_list):
  rank_dict = defaultdict(int)
  for score in score_list: rank_dict[round(score/100)] += 1
  print(rank_dict)
  return rank_dict

def calc_mode(score_list):
    rank_dict = make_rank_dict(score_list)
    rank_mode = max(rank_dict.values())
    for key, value in rank_dict.items():
      if value == rank_mode: return [key*10, key*10+10]

score_list = make_score_lists()
print("もっとも人数が多かったスコア幅は{0[0]} 〜 {0[1]}点代でした。".format(calc_mode(score_list)))
