# with open ('sample.txt',encoding='utf-8') as file: 
# # wite open (...) as file是Python處理檔案的語法 'sample.txt'是檔案名稱，encoding='utf=8'
#     for line in file :
#         print(line.rstrip())

with open ('sample.txt','r',encoding='utf-8') as file:  # 如果是要讀取的話中間有個'r'可以被省略 要改寫的話就是打'w' 要附加的話就是打'a'
# 等於就是說這整段只有'sample.txt'是開啟檔案名稱之外，其他都是固定的語法，基本上不太需要更改
    for line in file :
        print(line.rstrip())