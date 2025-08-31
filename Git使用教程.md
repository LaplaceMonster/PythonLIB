# Git使用教程

## Git关联GitHub方法

### **1. 生成 SSH 密钥（如果没有的话）**

首先，检查是否已经有 SSH 密钥：

```
ls ~/.ssh/id_rsa.pub
```

如果已有 `id_rsa.pub`，可以跳过生成密钥步骤。否则，执行以下命令生成新的 SSH 密钥：

```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

- `-t rsa`：指定 RSA 算法
- `-b 4096`：指定 4096 位密钥长度
- `-C "your_email@example.com"`：用于标识 SSH 密钥（填 GitHub 绑定的邮箱）
  按 **Enter** 使用默认路径 (`~/.ssh/id_rsa`)，可选设置密码（也可留空）。

------

### **2. 添加 SSH 密钥到 SSH 代理**

启用 SSH 代理并添加密钥：

```
eval "$(ssh-agent -s)"  # 启动 SSH 代理
ssh-add ~/.ssh/id_rsa
```

------

### **3. 添加 SSH 密钥到 GitHub**

复制 SSH 公钥：

```
cat ~/.ssh/id_rsa.pub
```

然后：

1. 登录 GitHub
2. 进入 **Settings → SSH and GPG keys**
3. 点击 **New SSH key**
4. 粘贴 `id_rsa.pub` 内容并保存

------

### **4. 测试 SSH 连接**

运行：

```
ssh -T git@github.com
```

如果成功，会看到类似：

```
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```

------

### **5. 配置 Git 远程仓库**

#### **情况 1：已有本地仓库**

进入本地 Git 仓库：

```
cd /path/to/your/repo
```

修改远程地址为 SSH：

```
git remote set-url origin git@github.com:username/repository.git
```

检查是否修改成功：

```
git remote -v
```

#### **情况 2：新建 Git 仓库**

```
git init
git remote add origin git@github.com:username/repository.git
```

------

### **6. 推送代码**

```
git add .
git commit -m "Initial commit"
git push -u origin main  # 或者 master，取决于你的默认分支
```



## 本地仓库修改后如何同步到GitHub

```
cd /path/to/your/repo         # 进入你的本地仓库
git status                    # 查看修改的文件
git add .                     # 添加所有修改的文件到暂存区
git commit -m "Updated files" # 提交更改
git pull origin main          # 拉取远程仓库的最新更改
git push origin main          # 将本地更改推送到远程仓库

git checkout main #确保你在本地仓库的主分支上
git pull origin main
```

## 如何将GitHub仓库同步到本地仓库

```
#如果完全没有本地仓库则直接
git clone GitHub_repo

#如果要更新GitHub到本地则
git checkout main   #确保你在本地仓库的主分支上
git pull origin main  #从远程仓库拉取最新的更改
```
