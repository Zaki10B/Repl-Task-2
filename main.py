import random

positive = ["hot", "summer", "hard", "dry", "simple", "light", "weak", "male", "sad", "win", "small", "ignore", "buy", "succeed", "reject", "prevent", "exclude"]

negetive = ["cold", "winter", "soft", "wet", "complex", "darkness", "strong", "female", "happy", "lose", "big", "pay attention", "sell", "fail", "accept", "allow", "include"] #17

score = 0
i = 0
for i in range(10):
  x = len(positive)
  y = len(negetive)
  word1 = random.randint(x)
  word2 = random.randint(x)
  print(positive[word1], "is to ",negetive[word1] , "as ", positive[word2], "is to...")
  answer = input("Answer: ")
  postitive = positive[:word1] + positive[word1+1: ]
  postitive = positive[:word2] + positive[word2+2: ]
  negetive = negetive[:word1] + negetive[word1: ]
  negetive = negetive[:word2] + negetive[word2: ]
  i += 1
  if answer == negetive[word2]:
    score += 1

print("your score is :%s " % i)
  