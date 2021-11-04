# 소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.
#
# 이 때 10,001번째의 소수를 구하세요.

new_lst = []
num = 2
count = 0

while True:
    for i in range(2, num):
        result = True
        for j in range(2, i):
            if i % j == 0:
                result = False
            if result == True:
                new_lst.append(i)
                num += 1
                count += 1
                print(new_lst)
    if count == 100:
        break
        print(new_lst[-1])

def primelist(n):
  num_list = [1] * n
  sqr = int(n ** 0.5)
  for i in range(2, sqr+1):
    if num_list[i] == 1:
      for j in range(2*i, n, i):
        num_list[j] = 0

  return [i for i in range(2, n) if num_list[i] == 1]

print(primelist(20))