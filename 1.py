# 1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면?

three = []
for i in range(1,1000):
    if i % 3 == 0:
        three.append(i)
    elif i % 5 == 0:
        three.append(i)

print(sum(three))