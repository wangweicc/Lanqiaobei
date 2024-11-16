
from math import gcd

g = [[] for _ in range(21)]
for i in range(1, 22):
    for j in range(i+1, 22):
        if gcd(i, j) == 1:
            g[i-1].append(j-1)
            g[j-1].append(i-1)

state_num = 1 << 21
dp = [[0] * 21 for _ in range(state_num)]
dp[1][0] = 1

for i in range(state_num):
    for j in range(21):
        if i >> j & 1:
            for k in g[j]:
                if i >> k & 1:
                    dp[i][j] += dp[i^(1<<j)][k]

print(sum(dp[state_num-1])-dp[state_num-1][0])

print(881012367360)