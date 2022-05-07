# ST 表

ST 表是用于解决 **可重复贡献问题** 的数据结构。
> 可重复贡献问题：对于一个操作，重复计算一个值，答案不改变。

## [P3865 【模板】ST 表](https://www.acwing.com/problem/content/1276/)

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

## [P1890 GCD区间](https://www.luogu.com.cn/problem/P1890)

求最大公因数也是 RMQ 问题。

```cpp
#include <cstdio>

const int N = 1000010;
int n, f[N][20], log_2[N];

int Gcd(int a, int b)
{
    while (b != 0)
    {
        int __t = a % b;
        a = b;
        b = __t;
    }
    return a;
}

void Init()
{
    log_2[1] = 0;
    for (int i = 2; i <= n; i++)
        log_2[i] = log_2[i >> 1] + 1;

    int h = log_2[n];
    for (int k = 1; k <= h; k++)
        for (int i = 1; i + (1 << k) - 1 <= n; i++)
            f[i][k] = Gcd(f[i][k - 1], f[i + (1 << k - 1)][k - 1]);
}

int Query(const int l, const int r)
{
    int k = log_2[r - l + 1];
    return Gcd(f[l][k], f[r - (1 << k) + 1][k]);
}

int main()
{
    int q;
    scanf("%d%d", &n, &q);
    for (int i = 1; i <= n; i++)
        scanf("%d", &f[i][0]);
    Init();
    while (q--)
    {
        int l, r;
        scanf("%d%d", &l, &r);
        printf("%d\n", Query(l, r));
    }
    return 0;
}
```