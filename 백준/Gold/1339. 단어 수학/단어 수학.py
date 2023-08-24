from sys import stdin

N = int(stdin.readline())
words = []
word_priority = [[0, chr(i+65)] for i in range(26)]
ans = 0

for i in range(N):
    words.append(list(stdin.readline().rstrip()))
    words[i].reverse()

    for j in range(len(words[i])):
        word_priority[ord(words[i][j])-65][0] += pow(10, j)

word_priority.sort(reverse=True)

for i in range(10):
    ans += word_priority[i][0] * (9 - i)

print(ans)