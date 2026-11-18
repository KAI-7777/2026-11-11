# 🚀 Git & GitHub 完整指令參考手冊
> 適合軟體工程師新手入門學習

---

## 📌 目錄
1. [Git 核心概念](#-git-核心概念)
2. [安裝與初始設定](#-安裝與初始設定)
3. [建立與追蹤專案](#-建立與追蹤專案)
4. [暫存區操作（add）](#-暫存區操作add)
5. [提交操作（commit）](#-提交操作commit)
6. [查看狀態與紀錄](#-查看狀態與紀錄)
7. [連接 GitHub 遠端倉庫](#-連接-github-遠端倉庫)
8. [上傳到 GitHub（push）](#-上傳到-githubpush)
9. [從 GitHub 下載（pull / clone）](#-從-github-下載pull--clone)
10. [分支操作（branch）](#-分支操作branch)
11. [合併與衝突解決](#-合併與衝突解決)
12. [進階技巧](#-進階技巧)
13. [常見錯誤與解決方式](#-常見錯誤與解決方式)
14. [完整上傳流程速查](#-完整上傳流程速查)

---

## 🧠 Git 核心概念

Git 是一個**分散式版本控制系統**，幫助你追蹤程式碼的每一次變更。

```
工作目錄 (Working Directory)
  ↓ git add
暫存區 (Staging Area / Index)
  ↓ git commit
本地倉庫 (Local Repository)
  ↓ git push
遠端倉庫 (Remote Repository，例如 GitHub)
```

| 術語 | 說明 |
|------|------|
| Repository (repo) | 存放所有程式碼和版本歷史的地方 |
| Commit | 一次版本快照，記錄你這次做了什麼修改 |
| Branch | 分支，讓你可以平行開發不同功能 |
| Merge | 把兩個分支的修改合併在一起 |
| Clone | 把遠端的 repo 完整複製到本地 |
| Push | 把本地 commit 上傳到遠端 |
| Pull | 把遠端最新修改下載並合併到本地 |
| Fork | 在 GitHub 上複製別人的 repo 到自己帳號 |

---

## ⚙️ 安裝與初始設定

### 安裝 Git
- **Windows**：下載 [https://git-scm.com](https://git-scm.com)
- **Mac**：`brew install git`
- **Linux**：`sudo apt install git`

### 確認版本
```bash
git --version
# 輸出範例：git version 2.43.0
```

### 設定你的身份（必做！這會出現在每次 commit 中）
```bash
# 設定使用者名稱
git config --global user.name "你的名字"

# 設定 Email（要與 GitHub 帳號一致）
git config --global user.email "you@example.com"

# 查看目前設定
git config --list
```

---

## 📁 建立與追蹤專案

```bash
# 在現有資料夾初始化 Git（建立 .git 資料夾）
git init

# 或者：從 GitHub 複製一個現有專案
git clone https://github.com/使用者名稱/專案名稱.git
```

---

## 📦 暫存區操作（add）

`git add` 把你修改的檔案加入「暫存區」，準備好下次 commit。

```bash
# 新增單一檔案
git add 檔案名稱.txt

# 新增特定副檔名的所有檔案
git add *.js

# 新增目前資料夾內所有修改（最常用）
git add .

# 新增所有修改（包含子資料夾）
git add -A

# 互動式選擇要加入的內容
git add -p
```

---

## 💾 提交操作（commit）

`git commit` 把暫存區的內容永久記錄為一個版本。

```bash
# 提交並寫上說明（必要！）
git commit -m "新增登入功能"

# 合併 add + commit（只適用於已追蹤的檔案）
git commit -am "修正 bug"

# 修改上一次的 commit 訊息（還未 push 時才能用）
git commit --amend -m "修正後的說明"
```

> **💡 Commit 訊息建議格式：**
> ```
> 動詞 + 說明
> feat: 新增使用者登入功能
> fix: 修正密碼驗證錯誤
> docs: 更新 README
> ```

---

## 🔍 查看狀態與紀錄

```bash
# 查看目前工作區狀態（哪些檔案修改了、哪些在暫存區）
git status

# 查看 commit 歷史紀錄
git log

# 簡短版 log
git log --oneline

# 圖形化顯示分支
git log --oneline --graph --all

# 查看某個檔案的修改內容（尚未 add 的部分）
git diff 檔案名稱

# 查看暫存區與上次 commit 的差異
git diff --staged
```

---

## 🔗 連接 GitHub 遠端倉庫

### 在 GitHub 建立新 repo 後：
```bash
# 新增遠端倉庫（origin 是慣用名稱）
git remote add origin https://github.com/你的帳號/專案名稱.git

# 查看遠端設定
git remote -v

# 移除遠端設定
git remote remove origin

# 更改遠端網址
git remote set-url origin https://github.com/新帳號/新專案.git
```

---

## ⬆️ 上傳到 GitHub（push）

```bash
# 第一次上傳（設定追蹤分支）
git push -u origin main

# 之後每次上傳
git push

# 強制上傳（危險！覆蓋遠端，確認再用）
git push --force

# 上傳特定分支
git push origin 分支名稱
```

---

## ⬇️ 從 GitHub 下載（pull / clone）

```bash
# 下載遠端最新修改並合併（pull = fetch + merge）
git pull

# 只下載不合併
git fetch origin

# 完整複製一個專案到本地
git clone https://github.com/使用者/專案.git

# 複製到指定資料夾
git clone https://github.com/使用者/專案.git 我的資料夾名稱
```

---

## 🌿 分支操作（branch）

```bash
# 查看所有本地分支
git branch

# 查看所有分支（包含遠端）
git branch -a

# 建立新分支
git branch 新分支名稱

# 切換到某分支
git checkout 分支名稱

# 建立並立即切換（常用）
git checkout -b 新分支名稱

# 新版寫法（Git 2.23+）
git switch -c 新分支名稱

# 刪除分支
git branch -d 分支名稱

# 強制刪除（未合併的分支）
git branch -D 分支名稱
```

---

## 🔀 合併與衝突解決

```bash
# 把指定分支合併進目前分支
git merge 分支名稱

# Rebase（整理提交歷史，讓歷史更乾淨）
git rebase main

# 中止 rebase
git rebase --abort
```

### 解決衝突步驟：
1. `git pull` 或 `git merge` 後出現衝突
2. 打開衝突的檔案，會看到：
   ```
   <<<<<<< HEAD
   你的修改內容
   =======
   遠端的修改內容
   >>>>>>> origin/main
   ```
3. 手動選擇保留哪個版本，刪除標記符號
4. `git add .` → `git commit`

---

## 🛠️ 進階技巧

### 暫存修改（stash）
```bash
# 把目前未 commit 的修改暫時存起來
git stash

# 查看 stash 列表
git stash list

# 取回最新的 stash
git stash pop

# 取回特定 stash
git stash apply stash@{0}
```

### 撤銷操作
```bash
# 撤銷工作區的修改（還原到上次 commit 狀態）
git checkout -- 檔案名稱

# 把檔案從暫存區移出（不影響工作區）
git reset HEAD 檔案名稱

# 撤銷最後一次 commit（保留修改）
git reset --soft HEAD~1

# 完全撤銷最後一次 commit（修改也不要）
git reset --hard HEAD~1

# 建立一個「反向 commit」來撤銷（適合已 push 的情況）
git revert HEAD
```

### .gitignore
建立一個 `.gitignore` 檔案，讓 Git 忽略不需要追蹤的檔案：
```
# 忽略所有 .log 檔
*.log

# 忽略 node_modules 資料夾
node_modules/

# 忽略 .env 敏感設定檔
.env
```

---

## ❗ 常見錯誤與解決方式

| 錯誤訊息 | 原因 | 解決方式 |
|---------|------|---------|
| `fatal: not a git repository` | 沒有在 git 資料夾內 | `git init` 或切換到正確資料夾 |
| `Please tell me who you are` | 未設定身份 | `git config --global user.name/email` |
| `rejected` on push | 遠端有更新版本 | 先 `git pull`，再 `git push` |
| `CONFLICT` | 合併衝突 | 手動解決衝突後 `git add` + `git commit` |
| `detached HEAD` | 不在任何分支上 | `git switch main` 切回主分支 |

---

## 🎯 完整上傳流程速查

### 第一次建立新專案並上傳到 GitHub

```bash
# 1. 初始化
git init

# 2. 加入所有檔案
git add .

# 3. 第一次 commit
git commit -m "first commit"

# 4. 設定主分支名稱（GitHub 預設用 main）
git branch -M main

# 5. 連接 GitHub 遠端（先在 GitHub 網站建立 repo）
git remote add origin https://github.com/你的帳號/專案名稱.git

# 6. 上傳
git push -u origin main
```

### 之後每次更新

```bash
git add .
git commit -m "說明這次做了什麼"
git push
```

---

> **📌 記住最常用的三步驟：**
> ```bash
> git add .        # 加入所有修改
> git commit -m "" # 建立版本快照
> git push         # 上傳到 GitHub
> ```
