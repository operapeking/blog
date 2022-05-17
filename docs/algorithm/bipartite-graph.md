# 二分图

## 介绍

### 定义

节点由两个集合组成，且两个集合内部没有边的图。

<img src="https://pekingopera.ddns.net:81/i/2022/05/12/627cee94ef390.png" width = "30%" />

* 所有的树都是二分图。
* 有偶数顶点个数的环是二分图。

???+ example
    给定许多班火车及许多车站，每辆火中途停靠的站不尽相同，问最少个数的车站集合使得每辆火车都停靠至少一个集合中的车站。以图论的观点来看，将火车和车站视为顶点，火车有停靠车站则连边，问题转化成是二分图的点覆盖问题。

### 等价条件

一个图是二分图**当且仅当**它：

* 不包含奇环作为子图。

* 着色数是 2。

## 应用

### [P3386 【模板】二分图最大匹配](https://www.luogu.com.cn/problem/P3386)

给定一个二分图，其左部点的个数为 $n$，右部点的个数为 $m$，边数为 $e$，求其最大匹配的边数。

#### 匈牙利算法

1. 首先选取一个未配对的点 $u$ ，枚举与 $u$ 相连的点 $v$。如果点 $v$ 未配对，则将 u 与 v 配对，这是便找到了一条增广路。如果点 $v$ 已经被配对，就试着让已与 $v$ 配对的点 $w$ 去配对其他点，让 $v$ 空闲出来。

2. 继续对左部剩下未配对过的点一一进行配对，直到所有的点都已经尝试完毕，找不到新的增广路为止。

时间复杂度 $O(nm)$

??? note "代码"

    ```cpp
    #include <cstdio>
    #include <bitset>
    
    const int N = 1010, M = 50010;
    int n, m, e;
    int idx, head[N], ver[M], nxt[M];
    
    void Add(int u, int v)
    {
        ver[++idx] = v;
        nxt[idx] = head[u];
        head[u] = idx;
    }
    
    int match[N];
    std::bitset<N> vis;
    bool Check(int u)
    {
        for (int i = head[u]; i; i = nxt[i])
        {
            int v = ver[i];
            if (vis[v])
                continue;
            vis[v] = true;
            if (!match[v] || Check(match[v]))
            {
                match[v] = u;
                return true;
            }
        }
        return false;
    }
    
    int main()
    {
        scanf("%d%d%d", &n, &m, &e);
        for (int i = 1; i <= e; i++)
        {
            int u, v;
            scanf("%d%d", &u, &v);
            Add(u, v);
        }
        int ans = 0;
        for (int i = 1; i <= n; i++)
        {
            vis.reset();
            if (Check(i))
                ans++;
        }
        printf("%d\n", ans);
        return 0;
    }
    ```

#### 网络流

将源点连上左边所有点，右边所有点连上汇点，容量皆为 $1$。原来的每条边从左往右连边，容量也皆为 $1$，最大流即最大匹配。

时间复杂度 $O(\sqrt{n}m)$

### [P1640 [SCOI2010]连续攻击游戏](https://www.luogu.com.cn/problem/P1640)

将其转化成二分图的最大匹配问题：所有属性 $\left[1,10000\right]$ 为左部点，所有武器为右部点，从 $1$ 开始尝试与武器匹配，直到不能再匹配为止。

??? note "代码"

    ```cpp
    #include <cstdio>
    #include <bitset>

    const int N = 1000010, M = 2000010;
    int idx, head[N], ver[M], nxt[M];

    void Add(int u, int v)
    {
        ver[++idx] = v;
        nxt[idx] = head[u];
        head[u] = idx;
    }

    int match[N];
    std::bitset<N> vis;
    bool Check(int u)
    {
        for (int i = head[u]; i; i = nxt[i])
        {
            int v = ver[i];
            if (vis[v])
                continue;
            vis[v] = true;
            if (!match[v] || Check(match[v]))
            {
                match[v] = u;
                return true;
            }
        }
        return false;
    }

    int main()
    {
        int n = 10000, e;
        scanf("%d", &e);
        for (int i = 1; i <= e; i++)
        {
            int to1, to2;
            scanf("%d%d", &to1, &to2);
            // Add(i, to1), Add(i, to2);
            // Add(to1, i), Add(to2, i);
        }
        int ans = 0;
        for (int i = 1; i <= n; i++)
        {
            vis.reset();
            if (Check(i))
                ans++;
            else
                break;
        }
        printf("%d\n", ans);
        return 0;
    }
    ```

### [P1963 [NOI2009] 变换序列](https://www.luogu.com.cn/problem/P1963)
