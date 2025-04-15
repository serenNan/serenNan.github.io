import os
import re
from pathlib import Path

def extract_title_from_md(file_path):
    """从index.md文件中提取标题"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('title:'):
                    # 提取标题内容，去除引号和前后空格
                    title = line.split('title:')[1].strip().strip('"').strip("'").strip()
                    return title
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return None

def rename_folders(base_dir):
    """重命名文件夹为index.md中的标题"""
    for root, dirs, _ in os.walk(base_dir):
        for dir_name in dirs:
            dir_path = Path(root) / dir_name
            md_file = dir_path / "index.md"
            
            if md_file.exists():
                title = extract_title_from_md(md_file)
                if title:
                    try:
                        new_dir_name = title.replace('/', '_')  # 替换可能造成路径问题的字符
                        new_dir_path = Path(root) / new_dir_name
                        
                        if new_dir_path.exists():
                            print(f"Skipping: {new_dir_path} already exists")
                        else:
                            os.rename(dir_path, new_dir_path)
                            print(f"Renamed: {dir_path} -> {new_dir_path}")
                    except Exception as e:
                        print(f"Error renaming {dir_path}: {e}")

if __name__ == "__main__":
    base_directory = "post"  
    rename_folders(base_directory)