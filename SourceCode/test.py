def comb(level, start, temp):
    if level == 3:
        print(temp)
        return

    for s in range(start+1, 8):
        comb(level+1, s, temp+[arr[s]])

# arr = [i for i in range(8)]
# comb(0, -1, [])

# 조합의 경우 오름차순으로 정렬된 리스트 중에서 이후의 범위만 대상으로 함


def perm(level, temp):
    global visited
    if level == 3:
        print(temp)
        return

    for i in range(8):
        if visited & (1<<i): continue
        visited += 1 << i
        perm(level+1, temp+[arr[i]])
        visited -= 1 << i

# arr = [i for i in range(8)]
# visited = 0
# perm(0, [])

# 순열은 arr 리스트 전범위를 대상으로 함, 이미 선택된 원소를 구분하기 위해 visited 사용
# 비트연산자, visited 리스트, if not in ~, append & pop 등 자기 스타일에 따라 코드형태가 달라지곤 함


def subset(level, temp):
    if level == 3:
        print(temp)
        return

    subset(level+1, temp)
    subset(level+1, temp+[arr[level]])

# arr = [i for i in range(8)]
# subset(0, [])