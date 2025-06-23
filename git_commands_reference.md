# Git 常用命令详解手册

本手册整理了日常开发中常用的 Git 命令、用法说明和示例，适合初学者和开发者查阅。

---

## 1. 仓库初始化与配置

### 初始化本地仓库
```bash
git init
```
> 在当前目录初始化一个新的 Git 仓库。

### 配置用户名和邮箱
```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```
> 设置全局用户名和邮箱，提交时会用到。

---

## 2. 远程仓库操作

### 添加远程仓库
```bash
git remote add origin <远程仓库地址>
```
> 关联远程仓库，常用别名 origin。

### 查看远程仓库
```bash
git remote -v
```
> 显示所有远程仓库地址。

### 修改远程仓库地址
```bash
git remote set-url origin <新地址>
```

### 删除远程仓库
```bash
git remote remove origin
```

---

## 3. 文件操作

### 查看当前状态
```bash
git status
```
> 查看工作区和暂存区的状态。

### 添加文件到暂存区
```bash
git add <文件名>
git add .
```
> 添加单个或所有更改的文件到暂存区。

### 移除文件
```bash
git rm <文件名>
```
> 从版本库和工作区删除文件。

---

## 4. 提交与历史

### 提交更改
```bash
git commit -m "提交说明"
```
> 将暂存区内容提交到本地仓库。

### 查看提交历史
```bash
git log
git log --oneline --graph --all
```
> 查看详细或简洁的提交历史。

### 查看文件改动
```bash
git diff
```
> 比较工作区与暂存区、历史版本之间的差异。

---

## 5. 分支管理

### 查看分支
```bash
git branch
```

### 创建新分支
```bash
git branch <分支名>
```

### 切换分支
```bash
git checkout <分支名>
```

### 创建并切换新分支
```bash
git checkout -b <分支名>
```

### 合并分支
```bash
git merge <分支名>
```
> 将指定分支合并到当前分支。

### 删除分支
```bash
git branch -d <分支名>
```
> 删除本地分支。

---

## 6. 推送与拉取

### 推送到远程仓库
```bash
git push origin <分支名>
```
> 推送本地分支到远程仓库。

### 首次推送并建立跟踪
```bash
git push -u origin <分支名>
```

### 拉取远程分支
```bash
git pull origin <分支名>
```
> 拉取远程分支并合并到当前分支。

### 克隆远程仓库
```bash
git clone <远程仓库地址>
```
> 下载远程仓库到本地。

---

## 7. 撤销与回滚

### 撤销工作区修改
```bash
git checkout -- <文件名>
```

### 撤销暂存区修改
```bash
git reset HEAD <文件名>
```

### 回退到某次提交
```bash
git reset --hard <commit_id>
```
> 慎用，回退后不可恢复。

### 撤销某次提交（保留历史）
```bash
git revert <commit_id>
```

---

## 8. 标签管理

### 创建标签
```bash
git tag <标签名>
```

### 查看标签
```bash
git tag
```

### 推送标签到远程
```bash
git push origin <标签名>
```

---

## 9. .gitignore 文件

在 `.gitignore` 文件中列出不需要纳入版本控制的文件或文件夹，例如：
```
__pycache__/
*.pyc
.env
```

---

## 10. 常见问题与技巧

- **查看简洁历史**：`git log --oneline --graph --all`
- **查看远程分支**：`git branch -r`
- **强制推送（慎用）**：`git push -f origin <分支名>`
- **解决冲突**：合并时如有冲突，手动编辑冲突文件，`git add .` 后再提交。
- **查看帮助**：`git help <命令>`

---

如需更详细的命令说明或遇到具体问题，欢迎随时提问！ 