# 첫수를 넣으세요  2
# 끝수를 넣으세요  4
# 2에서 4까지의 합은 9입니다.

a = input("첫수를 넣으세요") 
b = input("끝수를 넣으세요") 

aa = int(a)
bb = int(b)

sum = 0
for i in range(aa,bb+1):
    sum += i

print("{}에서 {}까지의 합은 {}입니다.".format(aa,bb,sum))




