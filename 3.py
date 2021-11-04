
#어떤 수를 소수의 곱으로만 나타내는 것을 소인수분해라 하고, 이 소수들을 그 수의 소인수라고 합니다.
#예를 들면 13195의 소인수는 5, 7, 13, 29 입니다.

#600851475143의 소인수 중에서 가장 큰 수를 구하세요.

def solution(x):
    d = 2
    lst = []
    while d <= x:
        if x % d == 0:
            lst.append(d)
            x = x / d
        else:
            d = d+1

    return lst[-1]

solution(600851475143)


# 소인수분해 첫 방식
# 약수를 구해줄 필요가 없음에도 약수를 구해주는 과정이 포함되어 연산이 너무 오래걸린다.

N = int(input())

quotient = []
for i in range(2, N+1):
    if N%i == 0:
        quotient.append(i)

for j in quotient:
    while N % j == 0:
        N = N / j
        print(j)