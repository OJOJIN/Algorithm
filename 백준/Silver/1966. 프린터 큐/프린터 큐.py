from sys import stdin
from collections import deque

T = int(stdin.readline())

while T > 0:
    T -= 1

    N, M = map(int, stdin.readline().split())

    doc = list(map(int, stdin.readline().split()))
    doc_que = deque(doc)

    target = [False for _ in range(N)]
    target[M] = True
    target_que = deque(target)

    max_prio = max(doc)
    ans = 0
    
    while True:
        # 맨 앞이 젤큰지 확인
        if doc_que[0] == max_prio:
            max_prio = 0
            doc_que.popleft()
            ans += 1
            # 타겟이였으면 break
            if target_que.popleft():
                break
        # 맨 앞이 젤 안크면 문서들이랑 내 타겟이 뭔지를 같이 돌리기
        else:
            doc_que.rotate(-1)
            target_que.rotate(-1)

        # 최대값 찾기
        for i in doc_que:
            max_prio = max(i, max_prio)

    print(ans)
