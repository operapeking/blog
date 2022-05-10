# 双端队列

## 介绍
双端队列是指一个可以在队首/队尾插入或删除元素的队列。

双端栈就是双端队列，双端栈就是双端队列。

![1652081344918.png](https://pekingopera.ddns.net:81/i/2022/05/09/6278c2c6b0153.png)

## 应用
1. 以双端队列为底层容器构建栈
2. 以双端队列为底层容器构建队列
3. 0-1 BFS

??? note "0-1 BFS"
    边权值为可能有，也可能没有（由于 BFS 适用于权值为 1 的图，所以一般权值是 0 或 1），或者能够转化为这种边权值的最短路问题。
    ```cpp
    while (队列不为空) {
        int u = 队首;
        弹出队首;
        for (枚举 u 的邻居) {
            更新数据
            if (...)
                添加到队首;
            else
                添加到队尾;
      }
    }
    ```
    例如在走迷宫问题中，你可以花 1 个金币走 5 步，也可以不花金币走 1 步，这就可以用 0-1 BFS 解决。


## 例题
### [Codeforces 173B](http://codeforces.com/problemset/problem/173/B)

一个 $n \times m$ 的图，现在有一束激光从左上角往右边射出，每遇到 `#`，你可以选择光线往四个方向射出，或者什么都不做，问最少需要多少个 `#` 往四个方向射出才能使光线在第 $n$ 行第 $m$ 列往右边射出。

0-1 BFS

* 当前格子不为 `#` 时，直接将状态放在队列头。
* 为 `#` 时，不仅要将状态放在队列头，还要考虑是否要改变方向。由于改变方向后代价要加 1，所以要放在队列尾，这样就保证了队列的有序性（从前到后代价递增）。

??? note "代码"
    ```cpp
    #include <cstring>
    #include <deque>
    #include <iostream>

    using namespace std;

    const int N = 1010, INF = 0x3f3f3f3f;
    int n, m;
    char grid[N][N];
    int dist[N][N][4];
    int dx[] = {1, -1, 0, 0}; // 下、上、右、左
    int dy[] = {0, 0, 1, -1};

    struct Status
    {
        int x, y, dir;
        Status(const int _x, const int _y, const int _dir) : x(_x), y(_y), dir(_dir){};
    };

    deque<Status> q;

    void Front(const Status u, int d)
    {
        if (dist[u.x][u.y][u.dir] <= d)
            return;
        dist[u.x][u.y][u.dir] = d;
        q.push_front(Status(u.x, u.y, u.dir));
    }

    void Back(const Status u, int d)
    {
        if (dist[u.x][u.y][u.dir] <= d)
            return;
        dist[u.x][u.y][u.dir] = d;
        q.push_back(Status(u.x, u.y, u.dir));
    }

    int main()
    {
        cin >> n >> m;
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++)
                cin >> grid[i][j];

        memset(dist, 0x3f, sizeof(dist));

        Front(Status(n, m, 3), 0);

        while (!q.empty())
        {
            Status u = q.front();
            q.pop_front();
            int now = dist[u.x][u.y][u.dir];
            int nx = u.x + dx[u.dir], ny = u.y + dy[u.dir];
            if (1 <= nx && nx <= n && 1 <= ny && ny <= m)
                Front(Status(nx, ny, u.dir), now);
            if (grid[u.x][u.y] == '#')
                for (int i = 0; i < 4; i++)
                    if (i != u.dir)
                        Back(Status(u.x, u.y, i), now + 1);
        }
        if (dist[1][1][3] == INF)
            cout << -1;
        else
            cout << dist[1][1][3];
        return 0;
    }
    ```