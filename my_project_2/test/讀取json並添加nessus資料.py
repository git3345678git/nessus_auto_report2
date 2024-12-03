import json
import requests
from bs4 import BeautifulSoup


def extract_content(element):
    # 過濾不要的標籤

    for h4 in element.find_all('h4'):
        h4.decompose()  # 刪除 h4 標籤

    content = element.get_text(strip=True, separator='\n\n')
    # print(content)
    return content






def get_nessus_data(url):

    try:
        response = requests.get(url)
        
        # 檢查請求是否成功
        response.raise_for_status()  # 如果狀態碼不是 200，會引發 HTTPError
        
        nessus_dict={}

        # 判斷是否有跳轉
        if response.history:
            nessus_dict["redirection"] = 'true'
            print("有經過跳轉")
        # 解析 HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 根據結構使用 CSS 選擇器
        description_element = soup.select_one('div > div > div:nth-of-type(2) > div > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div > div > div > div:nth-of-type(1) > section:nth-of-type(2)')
        solution_element = soup.select_one('#__next > div > div.app__container > div > div > div.col-12.col-md-9.col-xl-10 > div.card > div > div > div > div > div.col-md-8 > section:nth-child(3)')

        

        # 獲取說明內文
        if description_element:
            # 過濾不要的標籤
            description_content = extract_content(description_element)
            nessus_dict['description'] = description_content
        else:
            print("未找到說明元素。")

        # 獲取解決方案內文
        if solution_element:
            # 過濾不要的標籤
            solution_content = extract_content(solution_element)
            nessus_dict['solution'] = solution_content
        else:
            print("未找到解決方案元素。")

        return nessus_dict

    except requests.HTTPError:
        print("網頁不存在或無法訪問。")
    except Exception as e:
        print(f"發生錯誤: {e}")








# 1. 從檔案中讀取 JSON 數據
with open('output.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 2. 在字典中遍歷所有鍵，並新增鍵值
for risk_level, items in data.items():
    for item in items:


        url = f"https://zh-tw.tenable.com/plugins/nessus/{item["id"]}"

        nessus_dict= get_nessus_data(url)


        item.update(nessus_dict)  # 替換為你想要的鍵和值

# 3. 輸出修改後的字典
# print(json.dumps(data, indent=2, ensure_ascii=False))

# 4. 如果需要將修改後的字典寫入新的檔案
with open('output_2.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
