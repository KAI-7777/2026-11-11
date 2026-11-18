# Python 檔案操作：一步一步練習

這份教材會帶你練習讀取文字檔、寫入檔案、附加內容，以及讀取 CSV。請先準備好 Python，並在專案根目錄（`readFile.md` 所在的資料夾）執行範例。

## 練習檔案

- [`sample.txt`](./sample.txt)：文字檔，供讀取練習。
- [`students.csv`](./students.csv)：CSV 表格檔，供表格資料練習。

你可以在 VS Code 開啟終端機，確認目前位置是專案根目錄，再輸入：

```bash
python --version
```

若你的環境使用 `python3`，請把下方指令中的 `python` 改成 `python3`。

## 第 1 步：讀取整個文字檔

`open()` 可以開啟檔案。用 `with` 開啟時，離開區塊後 Python 會自動關閉檔案。

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

- `"sample.txt"` 是檔案名稱；相對路徑會從你執行 Python 時的目前資料夾開始尋找。
- `"r"` 表示讀取（read）。
- `encoding="utf-8"` 可以正確處理中文文字。
- `read()` 會一次讀取整個檔案。

`sample.txt` 的內容如下：

```text
Python 檔案練習
今天開始學習讀取檔案。
檔案可以保存文字，讓程式之後再使用。
```

## 第 2 步：一行一行讀取

當檔案有很多行時，可以用迴圈逐行處理：

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip())
```

`rstrip()` 會移除每行結尾的換行符號，避免 `print()` 顯示出多餘的空行。若想把所有行放進串列，也可以使用 `readlines()`：

```python
with open("sample.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines)
```

每個元素通常會保留行尾的 `\n`。若只想讀一行，可以使用 `file.readline()`。

## 第 3 步：建立並寫入文字檔

以下程式會在目前資料夾建立 `my_notes.txt`，並寫入兩行文字：

```python
with open("my_notes.txt", "w", encoding="utf-8") as file:
    file.write("這是我的第一個檔案。\n")
    file.write("我正在練習 Python 寫檔。\n")
```

- `"w"` 表示寫入（write）。
- 如果檔案不存在，Python 會建立它。
- **如果檔案已存在，`"w"` 會清除舊內容再寫入。** 練習時請留意檔名。
- `\n` 表示換行。

寫入後，可以用第 1 步的方式讀取 `my_notes.txt`，確認內容。

## 第 4 步：在檔案最後附加內容

若要保留舊內容並加在檔案最後，請使用 `"a"`（append）：

```python
with open("my_notes.txt", "a", encoding="utf-8") as file:
    file.write("這一行是後來附加的。\n")
```

再次讀取 `my_notes.txt`，確認新的一行出現在最後。和 `"w"` 不同，`"a"` 不會先清除舊內容。

## 第 5 步：使用 pathlib 組合檔案路徑

當程式檔案和資料檔放在不同資料夾時，可以使用標準函式庫 `pathlib` 處理路徑：

```python
from pathlib import Path

data_path = Path("sample.txt")
print(data_path.exists())  # 檢查檔案是否存在

content = data_path.read_text(encoding="utf-8")
print(content)
```

`Path("sample.txt")` 一樣是相對於目前執行資料夾。`exists()` 回傳 `True` 代表路徑存在；若要從 Python 程式檔所在位置找檔案，可在 `.py` 檔中使用：

```python
from pathlib import Path

script_folder = Path(__file__).resolve().parent
data_path = script_folder / "sample.txt"
print(data_path.read_text(encoding="utf-8"))
```

`__file__` 是目前 `.py` 檔的位置，因此這段適合放在 `.py` 檔中執行，不適合直接貼到互動式 Python 終端機。

## 第 6 步：讀取 CSV 表格

CSV 是常見的表格文字格式。使用 Python 內建的 `csv` 模組讀取時，請開啟 `newline=""`：

```python
import csv

with open("students.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["score"])
```

`DictReader` 會使用 CSV 第一列的欄位名稱，因此每一筆資料可以用 `row["name"]`、`row["score"]` 取得。CSV 讀進來的值是文字；需要數字時可以轉型：

```python
score = int(row["score"])
```

## 練習題

請先自己完成，再看提示：

1. 讀取 `sample.txt`，並計算檔案共有幾行。
2. 建立 `journal.txt`，寫入一句今天學到的內容。
3. 再執行一次附加模式，為 `journal.txt` 多加一行；確認舊內容仍在。
4. 讀取 `students.csv`，算出所有學生的平均分數。

提示：

```python
# 計算行數：可以把 file.readlines() 存起來，再使用 len(...)
# 平均分數：先建立 total 和 count，逐筆加總後用 total / count
```

## 常見問題

- **找不到檔案（`FileNotFoundError`）**：確認檔案名稱、大小寫，以及執行程式時所在的資料夾。可以用 `Path.cwd()` 查看目前資料夾。
- **中文顯示不正常**：開啟文字檔時指定 `encoding="utf-8"`。
- **為什麼要用 `with`？** 它會在區塊結束時自動關閉檔案，避免忘記關閉。
- **讀取、寫入、附加有什麼差別？** `"r"` 讀取；`"w"` 寫入並覆蓋舊內容；`"a"` 保留舊內容並在最後附加。

## 完成檢查

- [ ] 能讀取 `sample.txt` 並印出內容。
- [ ] 能用迴圈逐行讀取檔案。
- [ ] 能建立自己的文字檔，並分辨 `"w"` 和 `"a"`。
- [ ] 能用 `csv.DictReader` 讀取學生資料。
