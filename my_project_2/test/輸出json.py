import json

file_path = 'output.txt'

try:
    # 打開並讀取 JSON 文件
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()

    print("成功讀取數據：")




    # 將數據分割為行
    lines = data.strip().split('\n')



    # 變數初始化
    result = {"Critical": [], "High": [],"Medium": [], "Low": []}
    current_severity = None



    # 遍歷每一行數據
    for  line in lines:
        
        line = line.strip()

        #不知是否精確匹配
        if line in ["Critical", "High", "Medium", "Low",]:
            current_severity = line
            
            #每換一個風險等級 元素數量就要歸0
            num=0

        elif 'aaaaaaaa' in line:
            line = line.replace('aaaaaaaa', '')

            #字典
            my_dict = {"name":line, "address":[]}
            
            #陣列 添加一個字典元素
            result[current_severity].append(my_dict)
            num+=1
            

        elif 'bbbbbbbb' in line:
            line = line.replace('bbbbbbbb', '')

            #風險等級陣列中的第N個字典元素新增id鍵值
            result[current_severity][num-1]["id"] = line

        elif 'cccccccc' in line:
            line = line.replace('cccccccc', '')

            #風險等級陣列中的第N個字典元素新增cvss鍵值
            result[current_severity][num-1]["cvss"] = line

        elif 'dddddddd' in line:
            line = line.replace('dddddddd', '')

            #風險等級陣列中的第N個字典元素中的address鍵 值為陣列
            #添加ip到陣列
            result[current_severity][num-1]["address"].append(line)
            
        else:
            pass
        



        


    # 輸出 JSON 到文件
    with open('output.json', 'w') as json_file:
        json.dump(result, json_file, indent=2)

    print("JSON data has been written to output.json")










except Exception as e:
    print(f"讀取文件時發生錯誤: {e}")







