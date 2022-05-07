# Git 快速入门
Git 是一个开源的分布式版本控制系统，用于敏捷高效地处理任何或小或大的项目。

### 创建仓库
| 命令        | 说明                                   |
| :---------- | :------------------------------------- |
| `git init`  | 初始化仓库                             |
| `git clone` | 拷贝一份远程仓库，也就是下载一个项目。 |

### 提交与修改
| 命令                      | 说明                                     |
| :------------------------ | :--------------------------------------- |
| `git add filename`        | 添加文件到暂存区                         |
| `git status`              | 查看仓库当前的状态，显示有变更的文件。   |
| `git diff`                | 比较文件的不同，即暂存区和工作区的差异。 |
| `git commit -m 'message'` | 提交暂存区到本地仓库。                   |
| `git reset`               | 回退版本。                               |
| `git rm`                  | 删除工作区文件。                         |
| `git mv`                  | 移动或重命名工作区文件。                 |

### 提交日志
| 命令               | 说明                                 |
| :----------------- | :----------------------------------- |
| `git log`          | 查看历史提交记录                     |
| `git blame filename` | 以列表形式查看指定文件的历史修改记录 |

### 远程操作
| 命令         | 说明               |
| :----------- | :----------------- |
| `git remote` | 远程仓库操作       |
| `git fetch`  | 从远程获取代码库   |
| `git pull`   | 下载远程代码并合并 |
| `git push`   | 上传远程代码并合并 |

## 实例


### 登录到 GitHub

```bash
ssh-keygen -t rsa -C "youremail@example.com" # 不要输入 passphrase
```

命令生成的 `~/.ssh/id_rsa.pub` 即为公钥，复制里面的内容。

在浏览器中登录 GitHub，打开 [添加 SSH keys 页面](https://github.com/settings/keys)

??? note "截图"
    ![Github Settings](https://pekingopera.ddns.net:81/i/2022/05/07/62768d8ee5980.png)

点击右上角 `New SSH key` 后，将内容复制到 Key 里（Title 为备注名）

??? note "截图"
    ![New SSH key](https://pekingopera.ddns.net:81/i/2022/05/07/62768ef4c9946.png)

为了验证是否成功，输入以下命令：

```bash
ssh -T git@github.com
```

如果输出 `Hi someone! You've successfully authenticated, but GitHub does not provide shell access.` 则添加成功。


### 添加仓库

先在 Github 上 [新建一个仓库](https://github.com/new)，如 `git-test`。
??? note "截图"
    ![new repo](https://pekingopera.ddns.net:81/i/2022/05/07/627690e2dcedd.png)

创建完成后就可以添加仓库了。
```bash
mkdir git-test                     # 创建测试目录
cd git-test/                       # 进入测试目录
echo "# Git 测试" >> README.md     # 创建 README.md 文件并写入内容

git init                                  # 初始化
git add README.md                         # 添加文件
git commit -m "添加 README.md 文件"        # 提交并备注信息


git remote add origin git@github.com:yourusername/git-test.git # 添加远程仓库
git push -u origin master
```