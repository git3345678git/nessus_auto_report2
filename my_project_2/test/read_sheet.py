import pandas as pd

# 文件路徑和工作表名稱
file_path = 'updated_data_raw2.xlsx'  # 替換為你的 Excel 文件路徑
sheet_name = 'MyCustomSheet'  # 替換為你要讀取的工作表名稱
output_file = 'output.txt'  # 輸出的文本文件名稱

# 要排除的值
exclude_values = ["總計", "列標籤"]  # 替換為你想排除的值

try:
    # 讀取指定的工作表
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    # 讀取 A 欄，並去掉 NaN 值
    a_column = df.iloc[:, 0].dropna()  # 取得 A 欄數據並移除 NaN

    # 打開文件進行寫入
    with open(output_file, 'w') as f:
        for value in a_column:
            # 如果值不在排除的列表中，則寫入文件
            if value not in exclude_values:
                f.write(f"{value}\n")  # 每個值單獨一行

    print(f"A 欄數據已成功輸出到 '{output_file}'，並排除指定的值。")

except FileNotFoundError:
    print(f"錯誤: 找不到文件 '{file_path}'。請檢查路徑是否正確。")
except ValueError:
    print(f"錯誤: 工作表 '{sheet_name}' 不存在。請檢查工作表名稱。")
except Exception as e:
    print(f"其他錯誤: {e}")
