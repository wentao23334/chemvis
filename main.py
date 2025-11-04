 
# 位于: main.py (根目录)

# 1. 从 "工具箱" (src) 导入我们需要的特定工具
from src.data_handler import load_data
from src.plot_engine import draw_plot

# 2. 定义一个假的 "example.csv" 文件路径
# (我们稍后会创建这个文件)
EXAMPLE_DATA_FILE = "example.csv" 

def main():
    """
    项目的主入口函数
    """
    print("--- [Main] 启动项目... ---")
    
    # 步骤 1: 调用数据处理员
    data = load_data(EXAMPLE_DATA_FILE)
    
    # 步骤 2: 调用绘图引擎 (如果数据加载成功)
    if data is not None:
        draw_plot(data, output_filename="my_first_plot.png")
    
    print("--- [Main] 项目运行结束。 ---")

# ----------------------------------------------------
# 这是一个非常重要的 Python 惯例
# 它的意思是：“只有当这个 .py 文件被直接运行时，才执行 main() 函数”
# (如果它被其他脚本 import，则不执行)
# ----------------------------------------------------
if __name__ == "__main__":
    main()