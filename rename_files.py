import os

# 定义目录路径
dir_path = r"D:\AMR\AMRlianghua\structural-probes-master\structual-probe-amr\deberta-large\test"

# 获取目录中的所有文件
files = os.listdir(dir_path)

# 遍历文件并重命名
for file in files:
    # 只处理以deberta_amr_embeddings_开头且以.h5结尾的文件
    if file.startswith("deberta_amr_embeddings_") and file.endswith(".h5"):
        # 构建新的文件名，添加test_前缀
        new_file = f"test_{file}"
        # 构建完整的文件路径
        old_path = os.path.join(dir_path, file)
        new_path = os.path.join(dir_path, new_file)
        # 执行重命名
        os.rename(old_path, new_path)
        print(f"重命名: {file} -> {new_file}")

print("重命名完成！")
