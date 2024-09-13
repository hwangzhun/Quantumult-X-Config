# html_to_json.py
from bs4 import BeautifulSoup
import json
import re

def html_to_json(keywords, to_json_file):

    # 从文件中读取剔除关键词
    with open(keywords, 'r', encoding='utf-8') as f:
        exclude_keywords = [line.strip().lower() for line in f if line.strip()]


    # 读取 HTML 文件内容
    with open(to_json_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # 解析 HTML 内容
    soup = BeautifulSoup(html_content, 'lxml')

    # 定义正则表达式匹配第一个英文单词
    word_pattern = re.compile(r'[a-zA-Z]+')

    # 初始化数据字典和计数器
    data = {}
    file_count = 0

    # 查找所有的 <p> 标签
    for p_tag in soup.find_all('p'):
        # 提取 <p> 标签的文本并使用正则表达式查找第一个英文单词
        p_text = p_tag.get_text(strip=True)
        match = word_pattern.search(p_text)

        if match:
            # 获取第一个英文单词，作为文件名的一部分
            file_name = match.group(0)

            # 查找 <p> 标签下的所有 <a> 标签并提取链接
            links = []
            for a_tag in p_tag.find_all('a'):
                link_text = a_tag.get_text(strip=True)
                link_url = a_tag.get('href')

                # 跳过包含剔除关键词的链接
                if any(keyword.lower() in link_text.lower() for keyword in exclude_keywords):
                    continue

                links.append({
                    'text': link_text,
                    'url': link_url
                })

            if links:
                # 将分类及其链接添加到数据字典
                data[file_name] = links

                # 将每个分类的数据保存为单独的 JSON 文件
                json_data = json.dumps(links, ensure_ascii=False, indent=4)
                output_file_name = "tool/md2json/output/" + f"{file_name}.json"
                with open(output_file_name, 'w', encoding='utf-8') as json_file:
                    json_file.write(json_data)
            
                file_count += 1
                print(f"JSON 文件已保存为 {output_file_name}")

    print(f"总共处理了 {file_count} 个文件。")
    print("JSON 文件已经转换完成")