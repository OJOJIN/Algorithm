member = set()
find = set()

a, b = map(int, input().split())

for i in range(0, a):
    member.add(input())

for i in range(0, b):
    find.add(input())

ans = sorted(list(member & find))

print(len(ans))

for i in ans:
    print(i)
