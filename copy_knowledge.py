import os
import shutil

def flatten_index_to_knowledge(src_root, dst_root="/home/serenNan/Projects/Knowledges/my-blog-knowlege"):
    """将所有 index.md 复制到知识库目录，直接以父文件夹命名（扁平化）"""
    os.makedirs(dst_root, exist_ok=True)  # 确保目标目录存在
    
    for root, dirs, files in os.walk(src_root):
        if "index.md" in files:
            # 获取原文件路径和父目录名
            src_path = os.path.join(root, "index.md")
            parent_dir = os.path.basename(root)
            
            # 生成目标文件名（避免冲突）
            dst_filename = f"{parent_dir}.md"
            dst_path = os.path.join(dst_root, dst_filename)
            
            # 复制文件
            shutil.copy2(src_path, dst_path)
            print(f"✅ 已复制: {src_path} -> {dst_path}")

if __name__ == "__main__":
    src_dir = "post"
    if os.path.isdir(src_dir):
        flatten_index_to_knowledge(src_dir)
        print(f"🎉 所有文件已扁平化复制到 {os.path.abspath('knowledge')}/")
    else:
        print("❌ 错误：输入的路径无效！")