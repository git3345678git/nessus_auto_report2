import pandas as pd

# 讀取 Excel 文件中的工作表
sheet1 = pd.read_excel('我的比對數據.xlsx', sheet_name='old')
sheet2 = pd.read_excel('我的比對數據.xlsx', sheet_name='new')

# 清理列名
sheet1.columns = sheet1.columns.str.strip()
sheet2.columns = sheet2.columns.str.strip()

# 檢查列名
print("Sheet1 列名:", sheet1.columns.tolist())
print("Sheet2 列名:", sheet2.columns.tolist())

# 合併數據
merged = sheet1.merge(sheet2, on=['Plugin ID', 'Host', 'Port', 'Risk'], how='inner')

# 如果有匹配，輸出所有欄位
if not merged.empty:
    print("存在的數據：")
    print(merged)
else:
    print("沒有匹配的數據。")

# 如果需要，可以將結果寫入新的 Excel 文件
merged.to_excel('匹配結果.xlsx', index=False)