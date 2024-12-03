import pandas as pd

# 讀取 CSV 文件
input_file = 'add_2_translate_column.csv'
output_file = 'cleaned_data.csv'

try:
    # 加載 CSV 文件
    df = pd.read_csv(input_file, encoding='utf-8-sig')
    print("成功讀取數據")

    # 欄位清單，這些欄位將被刪除
    columns_to_remove = ['Synopsis', 'Description', 'Solution', 'See Also', 'Plugin Output', 'nessus_url']

    # 確保這些欄位存在於 DataFrame 中
    existing_columns_to_remove = [col for col in columns_to_remove if col in df.columns]

    if not existing_columns_to_remove:
        print("未找到需要刪除的欄位。")
    else:
        # 刪除指定欄位
        df = df.drop(columns=existing_columns_to_remove)
        print(f"已刪除以下欄位：{existing_columns_to_remove}")

        # 將處理後的數據保存為新文件
        df.to_csv(output_file, index=False, encoding='utf-8-sig')
        print(f"數據已輸出至 {output_file}")

except FileNotFoundError:
    print(f"找不到文件：{input_file}")
except Exception as e:
    print(f"發生錯誤：{e}")
