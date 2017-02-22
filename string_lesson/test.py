import sys

args = sys.argv

a = 'I want to manage my wallet.'

print(a.split())


b = 'hello, world!'
c = '''
パワハラで精神疾患になり働けなくなったなどとして、
漫画誌「{comic_title}」を発行していた出版社「{publisher}」（東京都渋谷区）
の男性従業員（４８）＝休職中＝が１３日、青林堂と社長らを相手取り、
慰謝料や未払い賃金計約２０００万円を求める訴えを東京地裁に起こした。(産経新聞)
'''
print(c.split())
# print(c.format(comic_title = args[1], publisher = args[2]))
