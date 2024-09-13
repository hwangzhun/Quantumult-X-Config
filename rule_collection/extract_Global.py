import json
import requests

# 读取 Global.json 文件
with open('Rule Collection/rule data/Global.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 提取 link 列表
links = data.get('link', [])

# 打开 Global.list 文件准备写入
with open('rule/Global.list', 'a', encoding='utf-8') as output_file:
    for link in links:
        try:
            # 请求每个链接中的规则内容
            response = requests.get(link)
            response.raise_for_status()
            
            # 将规则内容写入 Global.list，规则间用换行符隔开
            output_file.write(response.text + '\n\n')
        except requests.exceptions.RequestException as e:
            print(f"无法获取链接 {link}: {e}")
