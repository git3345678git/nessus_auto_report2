import pandas as pd
import requests
from bs4 import BeautifulSoup

# 讀取 CSV 文件
input_file = 'add_url.csv'
output_file = 'add_2_translate_column.csv'

try:
    # 加載 CSV 文件
    df = pd.read_csv(input_file, encoding='utf-8-sig')
    print("成功讀取數據")

    # 確保 'nessus_url' 欄位存在
    if 'nessus_url' not in df.columns:
        print("欄位 'nessus_url' 不存在。")
    else:
        # 初始化新增的欄位
        df['description'] = ''
        df['solution'] = ''

        # 遍歷 URL 並抓取資料
        for idx, url in enumerate(df['nessus_url']):
            try:
                print(f"正在處理第 {idx + 1} 筆資料：{url}")
                response = requests.get(url, timeout=10)
                response.raise_for_status()  # 確保請求成功
                soup = BeautifulSoup(response.text, 'html.parser')

                # 抓取 description 和 solution
                description_element = soup.select_one(
                    'div > div > div:nth-of-type(2) > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div > div > div > div:nth-of-type(1) > section:nth-of-type(2)'
                )
                solution_element = soup.select_one(
                    '#__next > div > div.app__container > div > div > div.col-12.col-md-9.col-xl-10 > div.card > div > div > div > div > div.col-md-8 > section:nth-child(3)'
                )

                # 過濾不需要的標籤並提取文字
                def extract_content(element):
                    if element:
                        for h4 in element.find_all('h4'):
                            h4.decompose()  # 刪除 h4 標籤
                        return element.get_text(strip=True, separator='\n\n')
                    return 'N/A'

                # 處理內容
                description = extract_content(description_element)
                solution = extract_content(solution_element)

                # 更新 DataFrame
                df.at[idx, 'description'] = description
                df.at[idx, 'solution'] = solution

            except Exception as e:
                print(f"抓取 {url} 時出錯：{e}")
                df.at[idx, 'description'] = 'Error'
                df.at[idx, 'solution'] = 'Error'

        # 保存結果到新的 CSV 文件
        df.to_csv(output_file, index=False, encoding='utf-8-sig')
        print(f"數據已保存到 {output_file}")

except FileNotFoundError:
    print(f"找不到文件：{input_file}")
except Exception as e:
    print(f"發生錯誤：{e}")
