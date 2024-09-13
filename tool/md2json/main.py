# main.py
import os
from md_to_html import md_to_html
from html_to_json import html_to_json

# 设置输入和输出文件路径 md_to_html
input_file_path = "tool/md2json/README.md"
output_file_path = "tool/md2json/output.html"

# 调用函数并传递参数
md_to_html(input_file_path, output_file_path)


# 设置输入和输出文件路径 html_to_json
keywords = "tool/md2json/exclude_keywords.txt"
to_json_file = output_file_path

# 调用函数并传递参数
html_to_json(keywords, to_json_file)

os.remove(output_file_path)

if os.path.exists(output_file_path):
    print("缓存文件未删除")
else:
    print("缓存文件已删除")
