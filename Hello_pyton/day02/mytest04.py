# 홀/짝을 입력하시오 홀
# 나:홀
# 컴:홀
# 결과:승리
from random import random

mine = input("홀/짝을 입력하시오")
com = ""
result = ""

rnd = random()
if rnd > 0.5:
    com = "홀"
else:
    com = "짝"
    
if com == mine:
    result = "승리"
else :
    result = "패배"  

print("mine",mine)
print("com",com)
print("result",result)