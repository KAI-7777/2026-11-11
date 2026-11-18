# 👥 Git 多人協作完整指南
> 從入門到實際工作流程，詳細說明多人開發的操作方式

---

## 📌 目錄
1. [多人協作的核心概念](#-多人協作的核心概念)
2. [兩種主要協作模式](#-兩種主要協作模式)
3. [模式一：共同協作者（Collaborator）](#-模式一共同協作者collaborator)
4. [模式二：Fork & Pull Request](#-模式二fork--pull-request)
5. [分支策略（Branch Strategy）](#-分支策略branch-strategy)
6. [實際多人開發完整流程](#-實際多人開發完整流程)
7. [衝突（Conflict）處理詳解](#-衝突conflict處理詳解)
8. [Pull Request（PR）操作詳解](#-pull-requestpr操作詳解)
9. [Code Review 規範建議](#-code-review-規範建議)
10. [常見問題與最佳實踐](#-常見問題與最佳實踐)

---

## 🧠 多人協作的核心概念

多人協作的本質是：**大家共用同一個遠端 repo（GitHub），每個人在本地開發，透過 push/pull 同步進度。**

```
開發者 A（本地）
    ↕ push / pull
         GitHub（遠端 repo）← 所有人共用
    ↕ push / pull
開發者 B（本地）
```

### 為什麼需要「分支」？
如果大家都直接改 `main`，會互相覆蓋彼此的程式碼。
**正確做法：每個人在自己的分支開發，完成後再合併回 `main`。**

---

## 🔀 兩種主要協作模式

| 模式 | 適用情境 | 說明 |
|------|---------|------|
| **Collaborator（共同協作者）** | 公司內部小團隊、自己的專案 | 直接給予 repo 的 push 權限 |
| **Fork & Pull Request** | 開源專案、外部貢獻者 | 無法直接 push，需 fork 後提交 PR |

---

## 👤 模式一：共同協作者（Collaborator）

### 設定步驟（Repo 擁有者操作）
1. 進入 GitHub 的 repo 頁面
2. 點選 **Settings** → **Collaborators**
3. 點 **Add people**，輸入對方 GitHub 帳號
4. 對方收到邀請 Email，接受後即可 push

### 被邀請者的操作流程

```bash
# 1. 第一次：Clone 專案到本地
git clone https://github.com/擁有者帳號/專案名稱.git
cd 專案名稱

# 2. 建立自己的功能分支（不要直接改 main！）
git checkout -b feature/登入功能

# 3. 開始開發，完成後 add & commit
git add .
git commit -m "feat: 新增使用者登入頁面"

# 4. 上傳自己的分支到遠端
git push -u origin feature/登入功能

# 5. 在 GitHub 上建立 Pull Request，請求合併進 main
```

---

## 🍴 模式二：Fork & Pull Request

適合貢獻到**你沒有直接 push 權限**的專案（例如開源）。

```bash
# 1. 在 GitHub 上點 "Fork"，複製一份到自己帳號

# 2. Clone 自己 fork 的版本
git clone https://github.com/你的帳號/專案名稱.git
cd 專案名稱

# 3. 設定原始 repo 為 upstream（以便同步更新）
git remote add upstream https://github.com/原作者帳號/專案名稱.git

# 4. 建立分支、開發、commit、push（同上）
git checkout -b fix/修正某個bug
git add .
git commit -m "fix: 修正登入頁面驗證錯誤"
git push origin fix/修正某個bug

# 5. 到 GitHub 自己的 fork 頁面，點 "Compare & pull request"
#    向原作者的 repo 提交 PR

# 6. 同步原始 repo 的最新更新
git fetch upstream
git checkout main
git merge upstream/main
```

---

## 🌿 分支策略（Branch Strategy）

### Git Flow（標準團隊分支模型）

```
main        ──────────────────────────────────────► 正式上線版本
              ↑ merge                      ↑ merge
develop     ──────────────────────────────────────► 開發整合分支
              ↑ merge       ↑ merge
feature/A   ───────────►
feature/B               ──────────────────►
hotfix      （緊急修正，直接從 main 拉出，修完合回 main & develop）
```

| 分支 | 用途 |
|------|------|
| `main` | 只放穩定、已上線的版本，不直接在這裡開發 |
| `develop` | 整合各人的功能，測試通過再合進 main |
| `feature/xxx` | 每個新功能各一條分支，開發完成後合進 develop |
| `hotfix/xxx` | 緊急修正正式版 bug，修完同時合進 main 和 develop |
| `release/xxx` | 準備發布時的最終測試分支 |

### 簡化版（適合小團隊）
```
main        ──────────────────────────────────────► 正式版本
              ↑ PR merge    ↑ PR merge
feature/A   ───────────►
feature/B               ──────────────────►
```
只用 `main` + `feature` 分支，不需要 develop，小團隊最實用。

---

## 🛠️ 實際多人開發完整流程

### 情境：三人團隊開發一個網站

#### 👑 專案負責人（建立專案）
```bash
# 1. 建立專案並推上 GitHub
git init my-website
cd my-website
# ... 建立初始檔案 ...
git add .
git commit -m "init: 專案初始化"
git branch -M main
git remote add origin https://github.com/負責人/my-website.git
git push -u origin main

# 2. 在 GitHub 邀請 A、B 為 Collaborator
```

---

#### 👩‍💻 開發者 A（負責首頁）

```bash
# Step 1：Clone 專案
git clone https://github.com/負責人/my-website.git
cd my-website

# Step 2：確認目前 main 是最新的
git pull origin main

# Step 3：建立功能分支
git checkout -b feature/homepage

# Step 4：開發功能（持續 commit）
# ... 寫程式 ...
git add .
git commit -m "feat: 新增首頁 Hero 區塊"

# ... 繼續開發 ...
git add .
git commit -m "feat: 新增首頁導航列"

# Step 5：推上遠端
git push -u origin feature/homepage

# Step 6：到 GitHub 開 Pull Request
# Base: main ← Compare: feature/homepage
# 寫清楚這個 PR 做了什麼，請求隊友 Review
```

---

#### 👨‍💻 開發者 B（負責聯絡頁）

```bash
# 同時進行，不受 A 的影響
git clone https://github.com/負責人/my-website.git
cd my-website
git pull origin main
git checkout -b feature/contact-page

# ... 開發 ...
git add .
git commit -m "feat: 新增聯絡我們頁面"
git push -u origin feature/contact-page

# 開 Pull Request 請求合併
```

---

#### 🔄 每天開始工作前（同步最新進度）

```bash
# 切換到 main 分支
git checkout main

# 拉取最新進度（同事昨天 merge 的內容）
git pull origin main

# 切回自己的分支
git checkout feature/我的分支

# 把 main 的更新合併進來（避免分支差太多）
git merge main
# 或使用 rebase（歷史更乾淨）
git rebase main
```

---

#### ✅ PR 被 Merge 後的清理

```bash
# 切回 main 並拉取最新
git checkout main
git pull origin main

# 刪除已完成的功能分支（本地）
git branch -d feature/homepage

# 刪除遠端分支
git push origin --delete feature/homepage
```

---

## ⚔️ 衝突（Conflict）處理詳解

### 什麼時候會發生衝突？
當**兩個人修改了同一個檔案的同一行**，Git 不知道要保留誰的版本。

### 實際衝突範例

```bash
# A 和 B 都修改了 index.html 的第 10 行
# B 先 push 了，A 要 push 時：

git push
# ❌ 錯誤：rejected！

# 正確做法：先 pull
git pull origin main
```

此時衝突的檔案會長這樣：
```html
<<<<<<< HEAD          ← 這是你（A）的版本
<h1>歡迎光臨我們的網站</h1>
=======               ← 分隔線
<h1>Welcome to Our Website</h1>
>>>>>>> origin/main   ← 這是 B 的版本（遠端）
```

### 解決步驟

```bash
# Step 1：看哪些檔案有衝突
git status
# 顯示 "both modified: index.html"

# Step 2：打開衝突的檔案，手動選擇要保留的內容
# 刪除 <<<<<<< HEAD、=======、>>>>>>> 這些標記
# 決定最終版本（可以兩個都要）：
# <h1>歡迎光臨 Welcome to Our Website</h1>

# Step 3：解決後標記為已解決
git add index.html

# Step 4：完成合併 commit
git commit -m "merge: 解決首頁標題衝突"

# Step 5：推上去
git push
```

### 🛡️ 預防衝突的方法
1. **分工明確**：每人負責不同的檔案或模組
2. **頻繁 pull**：每天開始工作先 `git pull`
3. **小量 commit**：不要積累太多修改才推
4. **分支隔離**：用 feature branch，不直接改 main

---

## 📬 Pull Request（PR）操作詳解

PR 是「我想把我的分支合併進 main，請大家審查」的請求。

### 開 PR 的步驟（GitHub 網頁）

1. Push 你的分支後，GitHub 會自動顯示 **"Compare & pull request"** 按鈕
2. 填寫 PR 說明：
   ```
   ## 這個 PR 做了什麼？
   新增使用者登入功能，包含：
   - 登入表單 UI
   - JWT 驗證邏輯
   - 錯誤訊息顯示

   ## 如何測試？
   1. npm start
   2. 前往 /login
   3. 輸入帳號密碼測試

   ## 相關 Issue
   Closes #12
   ```
3. 指定 **Reviewer**（請誰來審查）
4. 點 **Create pull request**

### Reviewer 審查流程

```bash
# 在本地 checkout 對方的分支來測試
git fetch origin
git checkout feature/登入功能

# 在 GitHub 網頁上可以：
# - 對特定行程式碼留下 comment
# - 點 "Request changes" 要求修改
# - 點 "Approve" 同意合併
```

### PR 被要求修改後

```bash
# 在自己的分支繼續修改
git checkout feature/登入功能
# ... 修改程式碼 ...
git add .
git commit -m "fix: 根據 review 修正密碼長度驗證"
git push
# PR 會自動更新，不需要重開
```

---

## 📋 Code Review 規範建議

### 寫 PR 的人應該：
- ✅ 標題清楚說明做了什麼（`feat: 新增登入功能`）
- ✅ 說明為什麼這樣做，而不只是做了什麼
- ✅ PR 大小適中（建議每個 PR 不超過 400 行）
- ✅ 附上測試方式或截圖

### Reviewer 應該：
- ✅ 在 48 小時內完成 review
- ✅ 對事不對人（「這段邏輯可以這樣優化」而非「你寫錯了」）
- ✅ 區分 "必須修改" 和 "建議修改"
- ✅ 不懂的地方先問清楚再下結論

---

## 💡 常見問題與最佳實踐

### Q：我不小心 push 到 main 怎麼辦？
```bash
# 建立分支儲存目前狀態
git branch backup/我的修改

# 把 main 重置到合併前
git reset --hard HEAD~1

# 強制更新遠端（危險！確認沒人 pull 過）
git push --force origin main
```

### Q：同事的分支合進 main 後，我的分支要怎麼更新？
```bash
# 方法一：merge（保留完整歷史）
git checkout my-feature
git fetch origin
git merge origin/main

# 方法二：rebase（歷史更線性、乾淨）
git checkout my-feature
git rebase origin/main
```

### Q：如何查看同事做了哪些修改？
```bash
# 查看特定分支的 log
git log origin/feature/同事分支 --oneline

# 比較兩個分支的差異
git diff main..feature/同事分支

# 查看是誰修改了某一行
git blame 檔案名稱.js
```

### Q：怎麼知道目前遠端有哪些分支？
```bash
# 列出所有遠端分支
git branch -r

# 更新遠端分支資訊
git fetch --all
```

---

## 🎯 多人協作流程總結

```
每天開始工作
      ↓
git checkout main
git pull origin main        ← 同步最新進度
      ↓
git checkout -b feature/我的功能   ← 建立功能分支
      ↓
開發、測試
      ↓
git add . && git commit -m ""      ← 頻繁小量 commit
      ↓
git push origin feature/我的功能
      ↓
GitHub 開 Pull Request
      ↓
等待 Code Review
      ↓
（若有修改意見）修改 → push → PR 自動更新
      ↓
Reviewer Approve → Merge PR
      ↓
git checkout main && git pull      ← 同步剛 merge 的結果
git branch -d feature/我的功能     ← 刪除舊分支
      ↓
開始下一個功能 🔄
```

> **🏆 黃金守則：**
> 1. 永遠不要直接 commit 到 `main`
> 2. 每天開始工作先 `git pull`
> 3. 分支名稱要有意義（`feature/登入`、`fix/購物車bug`）
> 4. Commit 訊息要清楚說明做了什麼
> 5. PR 要小、要有說明、要有 Review
