# 약수 찾기. 소수 찾기와 비교
factors = [x for x in range(n+1)]

for i in range(2, n+1):
    if factors[i] == i: # 아직 약수를 본 적 없는 숫자
        for j in range(i*i, n+1, i):
            factors[j] = i # 최소 약수 표시
