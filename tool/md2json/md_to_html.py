# md_to_html.py
import mistune
from custom_renderer import CustomRenderer

def md_to_html(input_file_path, output_file_path):
        
    # # 指定同级目录下的
    # input_file_path = "tool/md2json/README.md"
    # file_path = "tool/md2json/cache"

    # 使用自定义的渲染器创建 markdown 解析器
    markdown = mistune.create_markdown(renderer=CustomRenderer())

    # 读取 markdown 文件内容
    with open(input_file_path, 'r', encoding='UTF-8') as file:
        markdown_content = file.read()

    # 使用 mistune 解析 markdown，生成 AST（抽象语法树）
    ast = markdown(markdown_content)

    # # 打印输出的 HTML 数据
    # print(ast)

    # 保存为 HTML 文件
    with open(output_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(ast)

    print(f"Markdowm 已转换为 HTML 文件,已保存为 {output_file_path}")