import os
import re
import json
import requests

def parse_markdown_to_json(url, save_dir='rule data'):
    """
    将 Markdown 文件解析为 JSON 格式，并保存到指定目录

    Args:
        url (str): Markdown 文件的 URL
        save_dir (str, optional): 保存 JSON 文件的目录。默认值为 'file'。
    """

    # 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 创建文件保存目录
    save_dir = os.path.join(current_dir, save_dir)
    os.makedirs(save_dir, exist_ok=True)  # 如果目录已存在，则不会报错

    # 获取 Markdown 文件内容
    response = requests.get(url)
    markdown_content = response.text

    # 分割 Markdown 文件内容
    sections = markdown_content.split('\n\n')

    for i, section in enumerate(sections):
        if not section.strip():
            continue  # 跳过空白部分

        # 提取标题
        title_match = re.search(r'\b[A-Za-z]+\b', section)
        title = title_match.group(0).strip() if title_match else f"Untitled_{i}"

        # 提取链接
        links = re.findall(r'\[([^\]]+)\]\((https[^\)]+)\)', section)

        if not links:
            continue

        # 准备 JSON 数据
        data = {title: [{"name": name, "link": url} for name, url in links]}

        # 生成文件名并保存
        json_filename = os.path.join(save_dir, f"{re.sub(r'[\\/*?:"<>|]', '_', title)}.json")
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"生成了文件: {json_filename}")

# URL 
url = 'https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/README.md'
parse_markdown_to_json(url)