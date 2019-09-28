import sys
from collections import defaultdict

N = int(sys.stdin.readline())
dic = [str(sys.stdin.readline().strip()) for _ in range(N)]

dic = set(dic)

alpha_dict = {}

for dic_element in dic:
    alpha_dict[dic_element] = len(dic_element)

sorted_len = sorted(alpha_dict.items(), key=lambda x: x[1])
sorted_alpha = defaultdict(lambda : -1)

for (word,length) in sorted_len:
    if sorted_alpha[length] == -1:
        sorted_alpha[length] = [word]
    else:
        sorted_alpha[length].append(word)
        
for (length,word) in sorted_alpha.items():
    if len(word)>1:
        sorted_alpha[length] = sorted(word)
        
for word in sorted_alpha.values():
    for w in word:
        print(w)