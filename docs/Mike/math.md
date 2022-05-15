## 初等数论
#### 同余式
- **基本概念**
$a \equiv b \pmod m$
简记为 $a \equiv b (m)$
- **一些性质**
$a \equiv b (m) \to a - b \equiv 0(m) \to a \times k \equiv b \times k(m)$
设 $d$ 满足 $d\ |\ m$，$\to a \equiv b(m)$
- **同余类、剩余系**
	- 同余类：由对于模 $n$ 同余的所有整数组成的这个集合称为同余类。
	- 完全剩余系:设 $m \in Z^+，若r_0,r_1,...r_{m-1}$ 为m个整数，并且两两模m不同余，则 $r_0,r_1,\dots r_{m-1}$ 叫作模m的一个完全剩余系。
	- 简单剩余系:设 $m \in Z^+，若r_1,...r_{\phi(n)}$ 为 $\phi(n)$ 个整数，并且均与 $m$ 互质，则 $r_1,...r_{\phi(n)}$ 叫作模 $m$ 的一个简单剩余系。

#### 欧拉定理和欧拉函数
欧拉函数：

- **概念**

- **求法**：线性筛
```cpp
int phi[N], primes[N], v[N];
phi[1] = 1;
for (int i = 2; i <= n; i++)
{
	if (!v[i]) v[i] = i, primes[++cnt] = i, phi[i] = i - 1;
	for (int j = 1; j <= cnt; j++)
	{
		if (v[i] > primes[j]) break;
		v[primes[j] * i] = primes[j];
		phi[i * primes[j]] = (i % primes[j]) ? (primes[j] - 1) * phi[i] : primes[j] * phi[i];
	}
}
```

欧拉定理：

- **证明** （简单剩余系）

- **推论：**
$a ^ {b} \equiv a ^{b \mod \phi(n)}\pmod n$
	- 证明

[例题](https://www.acwing.com/problem/content/223/)：
给定一个整数 $N$，请你求出 $\sum_{1 \le i \le N}\gcd(1, i)$的值。
$1 \le N \le 2^{31}$

#### 费马小定理:

$a^{p - 1} \equiv 1\pmod p$，当 $p$ 为素数时成立。

证明：欧拉定理的特殊情况。

**求逆元**

*费马检查配合二次探测定理：Miller Rabin算法

#### 威尔逊定理

- **证明**

- **应用**

例题：

给出素数 p，求 $q!\mod p$，其中 $q$ 为比 p 小的最大素数，$p \in [1, 10^9]$。

#### 裴蜀定理

一定 $\exists x, y\in Z\ \ s.t.\  a * x + b * y = \gcd(a, b)$ 成立。

- **证明**
	1. 演绎证明
	2. 递归证明
- **推论**

	- $a,b$ 互质的充分必要条件是存在整数 $x,y$ 使 $a * x + b * y=1$
    - 设 $a_1,a_2,a_3......a_n$ 为 $n$ 个整数，$d$ 是它们的最大公约数，那么存在整数$x_1......x_n$ 使得 $x_1*a_1+x_2*a_2+...x_n*a_n=d$ 。
    - $a \times x + b \times y = c$ 有解当且仅当 $c\ |\ \gcd(a, b)$
	- $abs(a \times x + b \times y)_{min} = c$
例题：

给定 $K$，$M$ 求一个最小的正整数 $x$,使得 $K^x\equiv 1\pmod M$，如果无解输出 -1 。

数据范围：$2\leq K$，$M\le 2\times 10^9$。

[LINK](https://www.luogu.com.cn/problem/P4861)
$TAG:$ 欧拉定理，裴蜀定理

#### 逆元

- **概念**

如果您到百度上搜索逆元，您会看到如下定义：（这里逆元素是逆元的全称）
```
    逆元素是指一个可以取消另一给定元素运算的元素
    										---百度百科
```

理解：

举个例子，如果一个数 $F$ 乘一个数 $a$ 后，再乘它的倒数 $\frac {1} {a}$，相当于没有乘 $a$，换句话说，我们乘上 $\frac {1} {a}$ 后，取消了代数式 $F$ 乘 $a$ 后值增大的影响。

不难发现这符合逆元的定义，故我们可以说一个数和其倒数互为乘法逆元。除此之外，我们还能发现一个数和其相反数互为加法逆元等等……

- **应用：除法取模**
$a \div b \equiv a \times inv(b) \pmod m$
- **求法：**
	- 扩欧算法
    - 费马小定理（注意：仅在 p 为质数时成立）
    - 线性递推:
		$inv[i] = (p - \frac{p}{i}) \times inv(p\ mod\ i)\ mod\ p$
    	- 证明
```cpp
inv[1] = fac[1] = inv[0] = fac[0] = 1;
for (int i = 2; i <= n; i++)
    inv[i] = (p - p / i) * inv[p % i] % p;
```

#### 扩展欧几里得算法
求解 $a \times x + b \times y = \gcd(a, b)$ 的一组特解 $(x_0, y_0)$。

- **通解**

对于形如 $a \times x + b  \times y = c, \gcd(a,b)\ |\ c$ 的方程来说：

它的特解为 $(x^{'} = x_0 \times \frac{c}{\gcd(a, b)}, y ^ {'} = y_0 \times \frac{c}{
\gcd(a,b)})$；

它的通解为 $(x'+ k \times \frac{b}{\gcd(a, b)}, y^{'} - k \times \frac{a}{\gcd(a, b)})$ 。

```cpp
void ex\gcd(int a, int b, int &x, int &y)
{
   if (b == 0)
       return void(x = 1), void(y = 0);
   ex\gcd(b, a % b, x, y);
   int z = x;
   x = y, y = z - y * (a / b);
}
```
#### CRT 中国剩余定理
假设整数 $m_1, m_2\dots m_n$ 两两互素，则对于任意的整数 $a_1, a_2 \dots a_n$ ，方程组

$$\begin{cases} x \equiv a_1\ ({\rm mod}\ m_1) \\ x\equiv a_2\ ({\rm mod}\ m_2) \\ ... \\ x \equiv a_n\ ({\rm mod}\ m_n)\end{cases}$$
存在整数解。

我们设 $M=\prod_{i=1}^{k}m_i$，$ M_i=\frac{M}{m_i}$，$M_it_i≡1\;\;(mod\;\;m_i)$。

可以构造出一个解$x=\sum_{i=1}^{k}a_iM_it_i$

- **证明** 展开即可。
```cpp
int a[], m[], M[];
int CRT()
{
	int MUL = 1, TJ = 0;
	for (int i = 1; i <= n; i++)
		MUL *= m[i], M[i] = MUL / m[i];
	for (int i = 1; i <= n; i++)
	{
		int x, y;
		ex\gcd(M[i], m[i], x, y);
		if (x < 0) x += m[i];
		TJ += x * M[i] * a[i];
	}
	return TJ;
}
```
- **应用：**
	- $square\ numbers$ 取模

## 组合数学

#### 可重集排列和可重集组合
![](https://cdn.luogu.com.cn/upload/image_hosting/w9gkg3ok.png)
##### 多重集的组合数
从 $n$ 个元素中选取 $m$ 个元素，同一元素允许重复选取，产生的组合数量为 $C_{n + m - 1}^{m - 1}$。

可重集排列：（多组组合）
将 $n$ 个元素分成 $k$ 组，产生的组合个数为

可重集组合： (不定方程的非负整数解)
$x_1 + x_2 + x_3 + \dots + x_n = m$
非负整数解的个数为：$C_{n + m - 1}^{m - 1}$

- **证明**

#### 鸽巢原理
![](https://cdn.luogu.com.cn/upload/image_hosting/w05insir.png)
**证明**

#### 错排列和圆排列
- 错排列
$一个人写了n封不同的信及相应的n个不同的信封，他把这n封信都装错了信封，问他的装法有多少种(有名的“装错信封问题”)$

抽象化的，有一个 $1 ~n$ 排列 $\{a_n\}$，$\forall i \in (1, n),\ a_i\neq i$, 问满足条件的排列有多少种。
[Practice](https://www.acwing.com/problem/content/232/)

- 圆排列： 圆排列的定义为：有 $n$ 个元素，将其排成一个圆，求不同的排法数。
$(n - 1)!$
**证明：**

**解题时区别于项链数**

#### 二项式定理
- **证明（分析法）**

#### 容斥原理
- **筛法公式**

$$
| \complement_S{A_1} \cap \complement_S{A_2} \dots \cap \complement_S{A_n} | = |S| - \sum_{1 \le i < j \le n} |A_i \cap A_j|+ \sum_{1 \le i < j < k \le n} |A_i \cap A_j \cap A_k| + (-1)^{n + 1} \times |A_1 \cap A_2 \dots \cap A_n|
$$
- 再探错排问题

#### 卡特兰数（……）
- **定义**

- **例子**
	- 欧拉剖分
	- 合法括号对
	-

#### 组合杂项

- 组合数的线性预处理
- 杨辉三角与组合数
- 组合数的性质
		1. 硬性规定：$C_n^0 = 1, 0! = 1, C_0^0 = 1$
		2. ${C}_n^0+{C}_n^1+{C}_n^2+\cdots+{C}_n^n=2^n $
		3. $C_n^{i + 1} = C_n^i + C_n^{i - 1}$
## 线性代数

#### 矩阵概念
![](https://cdn.luogu.com.cn/upload/image_hosting/6aq90t58.png)
$X$ 阶矩阵： 行数与列数都等于 $n$ 的矩阵称为 $n$ 阶矩阵或 $n$ 阶方阵。
单位矩阵：主对角线上的元素都为 $1$ ，其余元素均为 $0$ 的 $n$ 阶方阵称为 $n$ 阶单位矩阵，记为 $E$。
逆矩阵：设 $A$ 是一个 $n$ 阶矩阵，若存在另一个 $n$ 阶矩阵 $B$ ，使得： $A \times B = E$

矩阵的迹：
$n \times n$ 矩阵 $A$ 的对角元素之和称为矩阵A的迹( $trace$ ),记作 $tr(A)$:
![](https://bkimg.cdn.bcebos.com/formula/6f97cd92926c3bd38460d597dca38f83.svg)

#### 特殊矩阵

- **稀疏矩阵**
我们知道矩阵是一个由 $m$ 行和 $n$ 列组成的二维数据对象，因此一共有 $m \times n$ 个数值。当这个矩阵的绝大部分数值为零，且非零元素呈不规律分布时，则称该矩阵为稀疏矩阵（ $Sparse\ Matrix$ ）
与它相对的一个概念叫稠密矩阵，，那些非零数值占大多数元素的矩阵即是稠密矩阵（ $Dense\ Matrix$ ），

- **三角矩阵**
三角矩阵（ $Triangular\ Matrix$ ）分为上三角矩阵和下三角矩阵。
上三角矩阵（ $Upper\ Triangular\ Matrix$ ）是指主对角线以下元素全为0的矩阵，如：
![](https://www.zhihu.com/equation?tex=%5Cbegin%7Bpmatrix%7D+1+%26+3+%5C%5C+0+%26+2+%5C%5C+%5Cend%7Bpmatrix%7D+%2C+%5Cquad+%5Cbegin%7Bpmatrix%7D+2+%26+4+%26+5+%5C%5C+0+%26+6+%26+0+%5C%5C+0+%26+0+%263+%5Cend%7Bpmatrix%7D)
下三角矩阵（Lower Triangular Matrix）是指主对角线以上元素全为0的矩阵，如：
![](https://www.zhihu.com/equation?tex=%5Cbegin%7Bpmatrix%7D+1+%26+0+%5C%5C+4+%26+2+%5C%5C+%5Cend%7Bpmatrix%7D+%2C+%5Cquad+%5Cbegin%7Bpmatrix%7D+2+%26+0+%26+0+%5C%5C+0+%26+0+%26+0+%5C%5C+4+%26+6+%263+%5Cend%7Bpmatrix%7D)


- **对称矩阵**
对称矩阵（Symmetric Matrix）是指元素以主对角线为对称轴对应相等的矩阵，例如：
![](https://www.zhihu.com/equation?tex=%5Cbegin%7Bpmatrix%7D+1+%26+3+%5C%5C+3+%26+2+%5C%5C+%5Cend%7Bpmatrix%7D+%2C+%5Cquad+%5Cbegin%7Bpmatrix%7D+2+%26+5+%26+6+%5C%5C+5+%26+0+%26+7+%5C%5C+6+%26+7+%263+%5Cend%7Bpmatrix%7D)

#### 矩阵的初等变换
- 交换两行或两列
![](https://pic4.zhimg.com/v2-e9426c8380df62896a3cd6c9ce927883_b.webp)
- 用一个数 $K$ 乘以某一行
![](https://pic3.zhimg.com/v2-c0caf102be74316b9df45a89fbe918fa_b.webp)
- 用某个数乘以某一行加到另一行中去

#### 矩阵的加减乘和转置运算
矩阵的加减乘
![](https://cdn.luogu.com.cn/upload/image_hosting/5svg43de.png)

矩阵的转置运算
![](https://pic2.zhimg.com/v2-486fa661982257c614058c13a706bb05_r.jpg)



#### 线性方程组的高斯消元法

历年NOIP的数学题
考点：
式子简化

