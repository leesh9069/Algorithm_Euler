# 10 이하의 소수를 모두 더하면 2 + 3 + 5 + 7 = 17 이 됩니다.
#
# 이백만(2,000,000) 이하 소수의 합은 얼마입니까?

def primelist(n):
    num_list = [True] * n
    sqr = int(n ** 0.5)
    for i in range(2, sqr+1):
        if num_list[i]:
            for j in range(2*i, n, i):
                num_list[j] = False

    new_list=[]
    for i in range(2, n):
        if num_list[i]:
            new_list.append(i)

    return sum(new_list)

print(primelist(2000000))