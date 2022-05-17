# ST 表

## 介绍

ST 表是用于解决 **可重复贡献问题** 的数据结构。
> 可重复贡献问题：对于一个操作，重复计算一个值，答案不改变。

* $O(n\log{n})$ 建表
* $O(1)$ 查询
* 特殊的动态规划？

## 例题

### [AcWing 1274. 奶牛排队](https://www.acwing.com/problem/content/1276/)

```cpp
#include <iostream>

const int N = 50010;
int n, q;
int log_2[N], stmin[N][16], stmax[N][16];

void Init()
{
    for (int i = 2; i <= n; i++)
        log_2[i] = log_2[i >> 1] + 1;
    int h = log_2[n];
    for (int k = 1; k <= h; k++)
        for (int i = 1; i + (1 << k) - 1 <= n; i++)
        {
            stmin[i][k] = std::min(stmin[i][k - 1], stmin[i + (1 << k - 1)][k - 1]);
            stmax[i][k] = std::max(stmax[i][k - 1], stmax[i + (1 << k - 1)][k - 1]);
        }
}

int main()
{
    scanf("%d%d", &n, &q);
    for (int i = 1; i <= n; i++)
    {
        int in;
        scanf("%d", &in);
        stmin[i][0] = stmax[i][0] = in;
    }
    Init();
    while (q--)
    {
        int l, r;
        scanf("%d%d", &l, &r);
        int k = log_2[r - l + 1];
        int resmin = std::min(stmin[l][k], stmin[r - (1 << k) + 1][k]);
        int resmax = std::max(stmax[l][k], stmax[r - (1 << k) + 1][k]);
        printf("%d\n", resmax - resmin);
    }
    return 0;
}
```

### [P1890 GCD区间](https://www.luogu.com.cn/problem/P1890)

求最大公因数也是 RMQ 问题。

??? note "转移方程"

    ```cpp
    f[i][k] = gcd(f[i][k - 1], f[i + (1 << k - 1)][k - 1]);
    ```

### [P2048 [NOI2010] 超级钢琴](https://www.luogu.com.cn/problem/P2048)

**翻译**：找到区间和前 k 大的不同区间（区间长度在 $l \sim r$ 之间）。

???+ tip
    虽然 ST 表无法直接处理区间最大值，但若我们求出数列前缀和 $sum$，再固定区间的左端点……

对于一个左端点为 $left$ 的区间，其右端点 $right$ 可能在 $left + l - 1$ 至 $left + r - 1$ 之间。这样就可以用 ST 表求出 $\max{sum[right]}$。

定义一个结构体 `Chord`，`Chord::st` 表示区间左端点；`Chord::l, r` 表示区间右端点的合法范围；`Chord::pos` 表示当右端点是 `Chord::pos` 时，区间的美妙度最大。

再将所有的 `Chord` 存入一个大根堆中。每次取出根 $now$ 时，统计答案。由于 $now$ 的区间是 $st \sim pos$，为了不漏掉可能的答案，还需要在取出 $now$ 时将 `Chord(st, l, pos - 1)`、`Chord(st, pos + 1, r)` 放回堆中。

??? note "代码"

    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <queue>

    const int N = 500010;
    int n;
    int sum[N];
    int log_2[N], f[N][19];

    void Init()
    {
        for (int i = 2; i <= n; i++)
            log_2[i] = log_2[i >> 1] + 1,
            f[i][0] = i;
        int h = log_2[n];
        for (int k = 1; k <= h; k++)
            for (int i = 1; i + (1 << k) - 1 <= n; i++)
            {
                const int &left = f[i][k - 1], &right = f[i + (1 << k - 1)][k - 1];
                f[i][k] = sum[left] < sum[right] ? right : left;
            }
    }

    int Query(const int l, const int r)
    {
        int k = log_2[r - l + 1];
        const int &left = f[l][k], &right = f[r - (1 << k) + 1][k];
        return sum[left] < sum[right] ? right : left;
    }

    struct Chord
    {
        int st, l, r, pos;
        Chord(int __st, int __l, int __r) : st(__st), l(__l), r(__r) { pos = Query(l, r); }
        const bool operator<(const Chord &b) const
        {
            return sum[pos] - sum[st - 1] < sum[b.pos] - sum[b.st - 1];
        }
    };

    int main()
    {
        int k, l, r;
        scanf("%d%d%d%d", &n, &k, &l, &r);
        for (int i = 1; i <= n; i++)
        {
            scanf("%d", &sum[i]);
            sum[i] += sum[i - 1];
        }
        Init();
        std::priority_queue<Chord> Q;
        for (int i = 1; i + l - 1 <= n; i++)
            Q.push(Chord(i, i + l - 1, std::min(i + r - 1, n)));

        long long ans = 0;
        while (k--)
        {
            Chord now = Q.top();
            Q.pop();
            ans += sum[now.pos] - sum[now.st - 1];
            if (now.l <= now.pos - 1)
                Q.push(Chord(now.st, now.l, now.pos - 1));
            if (now.pos + 1 <= now.r)
                Q.push(Chord(now.st, now.pos + 1, now.r));
        }
        printf("%lld\n", ans);
        return 0;
    }
    ```

### [P3295 [SCOI2016]萌萌哒](https://www.luogu.com.cn/problem/P3295)
