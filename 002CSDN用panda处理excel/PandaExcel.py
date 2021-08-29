import pandas as pd
from openpyxl import load_workbook

path = r"C:\Users\Carl\Desktop\JavaPython\MiniProjectPython\data.xlsx"
df1 = pd.read_excel(path,sheet_name='Sheet1')
df2 = pd.read_excel(path,sheet_name='Sheet2')

# panda中 shape是返回tuple行x列（全表），df.ix是选取某一列，df.iloc选取m~n-1行
for i in range(df1.shape[0]):
    data_time = df1.iloc[i,0]
    data_number = df1.iloc[i,1]

    #找到表2中对应的日期 并存在新dictionary dataloc里面
    data_loc = df2[df2['日期'] == data_time].index.tolist()
    #在日期的右侧（也就是1列） 输入对应的数据
    df2.iloc[data_loc[0], 1] = data_number

#填补上所有空的值为0
df2['销售件数'] = df2['销售件数'].fillna(value = 0)

#防止覆盖已有数据,所以要读取再重新写入
book = load_workbook(path)
writer = pd.ExcelWriter(path,engine='openpyxl')
writer.book = book
writer.sheets = dict((ws.title,ws)for ws in book.worksheets)

df2.to_excel(writer,"Sheet2",columns=['日期', '销售件数'],index = False)
writer.save()
