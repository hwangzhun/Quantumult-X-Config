# extract_rule.py
import json
import requests

def extract_rule(rule_file, output_rule_file):
    try:
        # 读取 json 文件
        with open(rule_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 提取 link 列表
        links = data.get('link', [])

        # 打开对应的输出文件准备写入
        with open(output_rule_file, 'w', encoding='utf-8') as output_rule_file:
            for link in links:
                try:
                    # 请求每个链接中的规则内容
                    response = requests.get(link)
                    response.raise_for_status()
                    
                    # 将规则内容写入对应的输出文件，规则间用换行符隔开
                    output_rule_file.write(response.text + '\n\n')
                except requests.exceptions.RequestException as e:
                    print(f"无法获取链接 {link}: {e}")
    except Exception as e:
        print(f"处理文件 {rule_file} 时发生错误: {e}")