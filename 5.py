# 1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.
# 그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?

my_list = [i for i in range(1, 21)]

def solution(lst):

    def gcd(x, y):
        while True:
            x, y = y, x % y
            if y == 0:
                return x

    def lcm(x, y):
        return x * y // gcd(x, y)

    while True:
        lst.append(lcm(lst.pop(), lst.pop()))
        if len(lst) == 1:
            return lst[0]