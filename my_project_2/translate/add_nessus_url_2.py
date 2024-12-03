import pandas as pd

# 讀取 CSV 文件
file_path = 'data_raw.csv'
output_file = 'add_url.csv'

try:
    # 加載 CSV 文件
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    print("成功讀取數據")

    # 移除空行和重複行
    df = df.dropna(how='all')  # 刪除完全空的行
    df = df[df['Plugin ID'].notna()]  # 確保 'Plugin ID' 欄位不為 NaN
    df = df.drop_duplicates()  # 刪除重複行

    # 確認 'Plugin ID' 欄位是否存在
    if 'Plugin ID' not in df.columns:
        print("欄位 'Plugin ID' 不存在。")
    else:
        # 串接 URL
        base_url = "https://zh-tw.tenable.com/plugins/nessus/"
        df['Plugin ID'] = df['Plugin ID'].astype(str).str.rstrip('.0')  # 修正浮點數問題
        df['nessus_url'] = base_url + df['Plugin ID']
        print("已新增欄位 'nessus_url'")

        # 檢查行數
        print(f"處理後的數據行數：{len(df)}")

        # 將處理後的數據保存為新文件
        df.to_csv(output_file, index=False, encoding='utf-8-sig')
        print(f"數據已輸出至 {output_file}")

except FileNotFoundError:
    print(f"找不到文件：{file_path}")
except Exception as e:
    print(f"發生錯誤：{e}")
