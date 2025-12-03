import json
import zhconv

# 文件名配置
input_filename = 'titanic-notebook-0-87-8b5595.ipynb'
output_filename = 'titanic_simplified.ipynb'

def convert_notebook(input_path, output_path):
    print(f"正在读取文件: {input_path} ...")
    
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            notebook = json.load(f)
        
        # 遍历所有的单元格 (Cells)
        count = 0
        for cell in notebook['cells']:
            # 只处理 Markdown 单元格和代码单元格的内容
            if 'source' in cell:
                new_source = []
                for line in cell['source']:
                    # 使用 zhconv 进行简繁转换 ('zh-cn' 代表简体中文)
                    converted_line = zhconv.convert(line, 'zh-cn')
                    new_source.append(converted_line)
                    if converted_line != line:
                        count += 1
                cell['source'] = new_source
        
        # 保存新文件
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, ensure_ascii=False, indent=1)
            
        print(f"✅ 转换完成！已处理 {count} 行文本。")
        print(f"新文件已保存为: {output_filename}")
        
    except FileNotFoundError:
        print(f"❌ 错误：找不到文件 '{input_path}'，请确认脚本和 .ipynb 文件在同一个目录下。")

if __name__ == '__main__':
    convert_notebook(input_filename, output_filename)