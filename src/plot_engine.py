
import matplotlib.pyplot as plt
import os # 我们导入 os 来处理文件路径

def draw_plot(dataframe, output_filename="plot.png"):
    """
    根据给定的 DataFrame 绘制一个简单的折线图。
    
    参数:
    dataframe (pandas.DataFrame): 从 data_handler 加载的数据
    output_filename (str): 输出图像的文件名
    """
    if dataframe is None or dataframe.empty:
        print("--- [Plot Engine] 错误：没有数据，无法绘图。 ---")
        return

    print(f"--- [Plot Engine] 正在绘制数据... ---")
    
    try:
        # 假设我们想画第1列 vs 第2列
        # (注意: pandas 索引从0开始)
        x_column = dataframe.columns[0]
        y_column = dataframe.columns[1]

        plt.figure(figsize=(10, 6)) # 创建一个 10x6 英寸的画布
        plt.plot(dataframe[x_column], dataframe[y_column], marker='o') # 画折线图
        
        plt.title("ChemVis Plot") # 添加标题
        plt.xlabel(x_column) # 添加 X 轴标签
        plt.ylabel(y_column) # 添加 Y 轴标签
        plt.grid(True) # 显示网格
        
        # 定义 output 文件夹
        output_dir = "output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir) # 如果 output 文件夹不存在，就创建它
            
        save_path = os.path.join(output_dir, output_filename)
        
        plt.savefig(save_path) # 保存图像
        print(f"--- [Plot Engine] 绘图成功！图像已保存到 {save_path} ---")
        # plt.show() # 如果你想在脚本运行时弹出窗口显示图像，可以取消这行的注释

    except Exception as e:
        print(f"--- [Plot Engine] 绘图时出错: {e} ---")