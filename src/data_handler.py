import pandas as pd

def load_data(filepath):
    """
    从指定路径加载 CSV 文件
    
    参数：
    filepath (str): .csv 文件的路径
    
    返回：
    pandas.DataFrame: 加载的数据
    """
    print(f"--- [Data Handler] 正在从 {filepath} 加载数据... ---")
    try:
        # 使用 pandas 读取 csv
        data = pd.read_csv(filepath)
        print("--- [Data Handler] 数据加载成功。 ---")
        return data
    except FileNotFoundError:
        print(f"--- [Data Handler] 错误：找不到文件 {filepath} ---")
        return None
    except Exception as e:
        print(f"--- [Data Handler] 加载数据时出错: {e} ---")
        return None