# 첫수를 넣으세요  2
# 끝수를 넣으세요  4
# 배수를 넣으세요  3

# 2에서 4까지 3의배수의 합은 3입니다.

a = input("첫수를 넣으세요")
b = input("끝수를 넣으세요")
c = input("배수를 넣으세요")

aa = int(a)
bb = int(b)
cc = int(c)

sum = 0

for i in range(aa,bb+1):
    if i%cc == 0:
        sum += i
    
print("{}에서 {}까지 {}의배수의 합은 {}입니다.".format(aa,bb,cc,sum));
