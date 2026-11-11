# Python 檔案操作：一步一步練習

這份教學會帶你讀取文字檔、逐行讀取、建立檔案、追加內容，並處理常見的檔案錯誤。請先確認同一個資料夾中有範例檔 [sample.txt](./sample.txt)。

## 開始前：確認檔案位置

Python 使用「目前工作資料夾」尋找相對路徑。請在終端機切換到放有 `sample.txt` 的資料夾，再啟動 Python 或執行程式。若使用 Jupyter Notebook，工作資料夾可能和 Notebook 檔案所在位置不同。

```python
from pathlib import Path

print("目前工作資料夾：", Path.cwd())
print("找到範例檔：", Path("sample.txt").exists())
```

如果第二行印出 `False`，代表 Python 正在其他資料夾尋找檔案。請確認終端機的資料夾，或將 `sample.txt` 放到目前工作資料夾。

## 第 1 步：讀取整個檔案

用 `Path.read_text()` 讀取文字檔。指定 `encoding="utf-8"` 可以正確處理範例中的中文。

```python
from pathlib import Path

text = Path("sample.txt").read_text(encoding="utf-8")
print(text)
```

你會看到範例檔中的內容。`read_text()` 回傳的是字串 (`str`)；檔案最後的換行也會保留在字串裡。

## 第 2 步：用 `open()` 和 `with` 讀取

`open()` 是 Python 內建的檔案操作方式。初學時請搭配 `with` 使用：離開區塊後，檔案會自動關閉。

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

print(text)
```

- `"r"` 表示讀取 (read)。
- `encoding="utf-8"` 指定文字編碼。
- `file.read()` 讀取檔案的全部內容。

## 第 3 步：逐行讀取

若檔案很大，逐行處理通常比一次讀完整個檔案更合適。

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")
```

`line` 每次會取得一行，通常也包含該行結尾的換行字元。`print(..., end="")` 避免 `print()` 再額外加一個換行。

如果想將每一行存成清單：

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines)
```

清單中的每個項目通常會保留行尾的 `\n`。若只想去除行尾換行，可使用 `line.rstrip("\n")`。

## 第 4 步：建立並寫入檔案

下面的程式會建立 `my_notes.txt`，並寫入兩行文字：

```python
from pathlib import Path

Path("my_notes.txt").write_text(
    "我的第一份檔案\n我正在練習 Python。\n",
    encoding="utf-8",
)
```

再次讀取它來確認結果：

```python
print(Path("my_notes.txt").read_text(encoding="utf-8"))
```

> **注意：** `write_text()` 會建立不存在的檔案，但如果檔案已存在，原本內容會被覆蓋。練習前請確認檔案中沒有要保留的內容。

也可以用 `open()` 寫入：

```python
with open("my_notes.txt", "w", encoding="utf-8") as file:
    file.write("這是第一行\n")
    file.write("這是第二行\n")
```

`"w"` 表示寫入 (write)，同樣會覆蓋既有內容。

## 第 5 步：追加內容，不覆蓋

若想在檔案結尾加上內容，使用追加模式 `"a"`：

```python
with open("my_notes.txt", "a", encoding="utf-8") as file:
    file.write("這是後來追加的一行\n")
```

`"a"` 表示追加 (append)。每執行一次就會多加一行，所以重複執行會得到重複內容。

## 第 6 步：處理檔案不存在

讀取不存在的檔案會發生 `FileNotFoundError`。可以在確定要提供友善訊息時處理這種情況：

```python
from pathlib import Path

path = Path("missing.txt")

try:
    text = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"找不到檔案：{path}")
else:
    print(text)
```

保留錯誤訊息有助於發現檔名或路徑拼錯的問題；不要在不清楚錯誤原因時直接忽略例外。

## 第 7 步：選擇適合的路徑寫法

`Path("sample.txt")` 是相對路徑，從目前工作資料夾開始尋找。也可以組合資料夾和檔名：

```python
from pathlib import Path

data_folder = Path("data")
sample_path = data_folder / "sample.txt"
print(sample_path)
```

`/` 在這裡是 `pathlib` 提供的路徑組合方式，不是字串相加。請先確認該路徑下真的有檔案。

## 自我練習

1. 讀取 `sample.txt`，並印出整個內容。
2. 逐行印出 `sample.txt`，每行前面加上 `> `。
3. 建立 `practice.txt`，寫入你今天學到的一件事，再讀取它確認內容。
4. 在 `practice.txt` 結尾追加一句話，然後再讀取一次。
5. 把檔名改成不存在的檔案，觀察錯誤；再試著用第 6 步處理它。

### 小提示

- 第 2 題可用 `print("> " + line, end="")`。
- 第 3 題可以用 `Path("practice.txt").write_text(...)`。
- 第 4 題可以使用 `open(..., "a", encoding="utf-8")`。
- 寫入時記得明確指定 `encoding="utf-8"`。

## 快速整理

| 目的 | 寫法 |
|---|---|
| 讀取整個文字檔 | `Path("檔名").read_text(encoding="utf-8")` |
| 讀取並逐行處理 | `with open("檔名", "r", encoding="utf-8") as file:` |
| 建立或覆寫檔案 | `Path("檔名").write_text(文字, encoding="utf-8")` |
| 追加內容 | `with open("檔名", "a", encoding="utf-8") as file:` |

初學時記住三件事：使用 `with` 管理檔案、文字檔指定 UTF-8、寫入 `"w"` 會覆蓋而 `"a"` 會追加。
