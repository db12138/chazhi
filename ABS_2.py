# %%
import pandas as pd
import numpy as np
import matplotlib
matplotlib.rcParams['font.sans-serif']=['SimHei']
import matplotlib.pyplot as plt

# %%
def sort_numpy_rows_by_one_column(array,col_index):
    length = array.shape[0]
    for i in range(array.shape[0]):
        if array[i][0] == "":
            length = i
            break
    array = array[:length,:]

    sort_indices = array[:,col_index].argsort()
    return array[sort_indices]
    
def load_plot():
    all_data = pd.read_excel("插值数据.xlsx",keep_default_na=False) #header=None header 默认为0
    print(all_data.columns)
    # Index(['RMBS', 'Unnamed: 1', 'Unnamed: 2', '车贷ABS', 'Unnamed: 4', 'Unnamed: 5',
    #    '消金', 'Unnamed: 7', 'Unnamed: 8', '地产', 'Unnamed: 10', 'Unnamed: 11',
    #    '建筑', 'Unnamed: 13'],
    #   dtype='object')

    RMBS_data = all_data.loc[1:,['RMBS', 'Unnamed: 1']].to_numpy()
    RMBS_data = sort_numpy_rows_by_one_column(RMBS_data,0)

    RMBS = {}
    RMBS["加权期限"] = RMBS_data[:,0]
    RMBS["收益率"] = RMBS_data[:,1]

    
    chedaiABS_data = all_data.loc[1:,['车贷ABS', 'Unnamed: 4']].to_numpy()

    chedaiABS_data = sort_numpy_rows_by_one_column(chedaiABS_data,0)
    chedaiABS = {}
    chedaiABS["加权期限"] = chedaiABS_data[:,0]
    chedaiABS["收益率"] = chedaiABS_data[:,1]

    xiaojin_data = all_data.loc[1:,['消金', 'Unnamed: 7']].to_numpy()
    xiaojin_data = sort_numpy_rows_by_one_column(xiaojin_data,0)
    xiaojin = {}
    xiaojin["加权期限"] = xiaojin_data[:,0]
    xiaojin["收益率"] = xiaojin_data[:,1]

    dichan_data = all_data.loc[1:,['地产', 'Unnamed: 10']].to_numpy()
    dichan_data = sort_numpy_rows_by_one_column(dichan_data,0)
    dichan = {}
    dichan["加权期限"] = dichan_data[:,0]
    dichan["收益率"] = dichan_data[:,1]

    jianzhu_data = all_data.loc[1:,['建筑', 'Unnamed: 13']].to_numpy()
    jianzhu_data = sort_numpy_rows_by_one_column(jianzhu_data,0)
    jianzhu = {}
    jianzhu["加权期限"] = jianzhu_data[:,0]
    jianzhu["收益率"] = jianzhu_data[:,1]


    fig = plt.figure(figsize=(8,4))
    ax = fig.add_subplot(3,2,1)
    ax.set_title('RMBS')
    ax.set_xlabel('加权期限')
    ax.set_ylabel('收益率')
    ax.plot(RMBS["加权期限"],RMBS["收益率"],"r",marker="o",label="RMBS")


    ax = fig.add_subplot(3,2,2)
    ax.set_title('车贷ABS')
    ax.set_xlabel('加权期限')
    ax.set_ylabel('收益率')
    ax.plot(chedaiABS["加权期限"],chedaiABS["收益率"],"r",marker="o",label="车贷")
    
    ax = fig.add_subplot(3,2,3)
    ax.set_title('消金')
    ax.set_xlabel('加权期限')
    ax.set_ylabel('收益率')
    ax.plot(xiaojin["加权期限"],xiaojin["收益率"],"r",marker="o",label="消金")

    ax = fig.add_subplot(3,2,4)
    ax.set_title('地产')
    ax.set_xlabel('加权期限')
    ax.set_ylabel('收益率')
    ax.plot(dichan["加权期限"],dichan["收益率"],"r",marker="o",label="地产")

    ax = fig.add_subplot(3,2,5)
    ax.set_title('建筑')
    ax.set_xlabel('加权期限')
    ax.set_ylabel('收益率')
    print(jianzhu)
    ax.plot(jianzhu["加权期限"],jianzhu["收益率"],"r",marker="o",label="建筑")
    
    plt.show()

if __name__ == "__main__":
    load_plot()
