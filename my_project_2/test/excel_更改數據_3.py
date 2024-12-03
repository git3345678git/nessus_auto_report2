import pandas as pd

# 讀取 CSV 文件
file_path = 'data_raw.csv'

try:
    # 嘗試使用不同的編碼
    df = pd.read_csv(file_path, encoding='ISO-8859-1')
    print("成功讀取數據：")

    # 確認 'Host' 和 'Port' 欄位是否存在
    if 'Host' not in df.columns or 'Port' not in df.columns:
        print("欄位 'Host' 或 'Port' 不存在。")
    else:
        # 串接 'Host' 和 'Port' 欄位的值
        df['ip:port'] = df['Host'].astype(str) + ':' + df['Port'].astype(str)

    # 確認多個欄位是否存在
    required_columns = ['Host', 'Port', 'Plugin ID', 'Risk', 'Name', 'CVSS v2.0 Base Score', 'ip:port']

    # 初始化一個空列表來存儲缺失的欄位
    missing_columns = []

    # 檢查每個要求的欄位是否存在
    for col in required_columns:
        if col not in df.columns:
            missing_columns.append(col)  # 如果欄位不存在，將其加入缺失欄位列表

    # 如果有缺失的欄位，報告它們
    if missing_columns:
        print("以下欄位不存在：", missing_columns)
    else:
        # 去掉 'Risk' 欄位值為 None 的行
        df = df.dropna(subset=['Risk'])

        # 更新其他欄位的值
        df['Risk'] = '' + df['Risk'].astype(str)
        df['Name'] = 'aaaaaaaa' + df['Name']
        df['Plugin ID'] = 'bbbbbbbb' + df['Plugin ID'].astype(str)
        df['CVSS v2.0 Base Score'] = 'cccccccc' + df['CVSS v2.0 Base Score'].astype(str)
        df['ip:port'] = 'dddddddd' + df['ip:port']

        # 將更新後的 DataFrame 寫回 Excel 文件
        df.to_excel('updated_data_raw2.xlsx', index=False, engine='openpyxl')
        print("已成功更新 'ip:port' 欄位並保存為 'updated_data_raw2.xlsx'。")

except Exception as e:
    print(f"讀取文件時發生錯誤: {e}")
