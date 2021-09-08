# 一个背包，往里装东西，重量向量w，价值向量v，如果你的容量为C，求你能装入背包的最大价值

# 每个东西只能选择一次
def pack1(w, v, C):
    dp = [[0 for _ in range(C + 1)] for _ in range(len(w) + 1)]
    for i in range(1, len(w) + 1):
        for j in range(1, C + 1):
            if j < w[i - 1]:  # 如果剩余容量不够新来的物体 直接等于之前的
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i - 1])
    return dp[len(w)][C]


# 空间复杂度优化
def pack1_update(w, v, c):
    # 它是先得到第一行的值，存到dp中，然后再直接用dp相当于就是上一行的值，所以下面必须用逆序
    # 否则dp[j-w[i-1]]可能会用到你本行的值，从大到小就不会
    dp = [0 for _ in range(c + 1)]
    for i in range(1, len(w) + 1):
        for j in reversed(range(1, c + 1)):  # 这里必须用逆序
            if w[i - 1] <= j:
                dp[j] = max(dp[j], dp[j - w[i - 1]] + v[i - 1])
    return dp[c]


# 每个东西能选择多次 完全背包问题
def pack2(w, v, C):
    dp = [[0 for _ in range(C + 1)] for _ in range(len(w) + 1)]
    for i in range(1, len(w) + 1):
        for j in range(1, C + 1):
            if j < w[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - w[i - 1]] + v[i - 1])
    return dp[len(w)][C]


def pack2_update(w, v, c):
    dp = [0 for _ in range(c + 1)]
    for i in range(1, len(w) + 1):
        for j in (range(1, c + 1)):
            if w[i - 1] <= j:
                dp[j] = max(dp[j], dp[j - w[i - 1]] + v[i - 1])
    return dp[c]


# 3 重背包问题，给定物体可选择次数s
def pack3(w, v, s, c):
    dp = [0 for _ in range(c + 1)]
    for i in range(1, len(w) + 1):
        for j in reversed(range(1, c + 1)):
            for k in range(s[i - 1] + 1):
                if k * w[i - 1] <= j:
                    dp[j] = max(dp[j], dp[j - k * w[i - 1]] + k * v[i - 1])
    return dp[c]


if __name__ == "__main__":

    w = [2, 3, 4, 5]
    v = [3, 4, 5, 6]
    c = 8

    print(pack2(w, v, c))
