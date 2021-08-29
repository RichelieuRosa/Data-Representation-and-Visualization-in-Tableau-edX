import numpy as np
import matplotlib.pyplot as plt

# # np.random.seed(1000)
# # y = np.random.standard_normal(20)
# # print(y)

# # # step1 简单绘图
# # x = range(len(y))
# # plt.plot(x,y)
# # plt.show()

# # # step2 附加值绘图
# # # cumsum 是当前列之前的和加到当前列上
# # plt.plot(y.cumsum())
# # plt.show()

# # # step3 自定义绘图
# # # 定义图像大小
# # plt.figure(figsize=(7,4))
# # # 在后面增加颜色和粗细
# # plt.plot(y.cumsum(),'b',lw=1.5)
# # plt.plot(y.cumsum(),'ro')
# # # add grids
# # plt.grid(True)
# # # axis type - tight
# # plt.axis('tight')
# # plt.xlim(-1,20)
# # plt.ylim(np.min(y.cumsum())-1,
# # np.max(y.cumsum())+1)
# #
# # plt.xlabel('index')
# # plt.ylabel('value')
# # plt.title('A simple plot')
# # plt.show()

# # # step4 二维数据集 **** 全新数组******
# np.random.seed(2000)
# y = np.random.standard_normal((20,2)).cumsum(axis=0)
# #
# # # 在这里我们使用放大的刻度进行对比
# # y[:,0] = y[:,0] * 100;
# # plt.figure(figsize = (7,4))
# # plt.plot(y[:,0], lw = 1.5, label = '1st')
# # plt.plot(y[:,1], lw = 1.5, label = '2nd')
# # plt.plot(y,'ro')
# #
# # plt.grid(True)
# # plt.legend(loc = 0)
# # plt.axis('tight')
# # plt.xlabel('index')
# # plt.ylabel('value')
# # plt.title('A simple plot2')
# #
# # plt.show()

# # step5 多数据集的分析
# # fig, ax1 = plt.subplots()
# # plt.plot(y[:,0], 'b', lw=1.5, label='1st')
# # plt.plot(y[:,0], 'ro')
# #
# # plt.grid(True)
# # plt.legend(loc = 8)
# # plt.axis('tight')
# # plt.xlabel('index')
# # plt.ylabel('value 1st')
# # plt.title('A simple plot')
# #
# # ax2 = ax1.twinx()
# # plt.plot(y[:,1], 'g', lw=1.5, label = '2nd')
# # plt.plot(y[:,1], 'ro')
# # plt.legend(loc = 0)
# # plt.ylabel('value 2nd')
# #
# # plt.show()

# # step6 单独子图
# # plt.figure(figsize = (7,5))
# # plt.subplot(211)
# # plt.plot(y[:,0], 'b', lw=1.5, label='1st')
# # plt.plot(y[:,0], 'ro')
# #
# # plt.grid(True)
# # plt.legend(loc = 0)
# # plt.axis('tight')
# # plt.ylabel('value 1st')
# #
# # plt.title('A simple plot')
# #
# # plt.subplot(212)
# # plt.plot(y[:,1], 'g', lw=1.5, label = '2nd')
# # plt.plot(y[:,1], 'ro')
# #
# # plt.grid(True)
# # plt.legend(loc = 0)
# # plt.axis('tight')
# # plt.xlabel('index')
# # plt.ylabel('value 2nd')
# #
# # plt.show()

# # # step7 不同类型的子图
# # plt.figure(figsize = (9,4))
# #
# # plt.subplot(121)
# # plt.plot(y[:,0], lw =1.5, label ='1st')
# # plt.plot(y[:,0], 'ro')
# # plt.grid(True)
# # plt.legend(loc = 0)
# # plt.axis('tight')
# # plt.xlabel('index')
# # plt.ylabel('value')
# #
# # plt.title('1st data set')
# #
# # plt.subplot(122)
# # plt.bar(np.arange(len(y)), y[:,1], width = 0.5, color = 'g', label = '2nd')
# # plt.grid(True)
# # plt.legend(loc=0)
# # plt.axis('tight')
# # plt.xlabel('index')
# # plt.title('2nd data set')
# #
# # plt.show()

# # # step8 散点图 *** 新的数据集 ****
# y = np.random.standard_normal((1000,2))
# # 第三个数据集
# c = np.random.randint(0, 10, len(y))
# #
# # plt.figure(figsize = (7,5))
# # # plt.plot(y[:,0], y[:,1], 'ro')
# # plt.scatter(y[:,0],y[:,1], c=c, marker = 'o')
# # plt.colorbar()
# # plt.grid(True)
# # plt.xlabel('1st')
# # plt.ylabel('2nd')
# # plt.title('Scatter plot')
# # plt.show()

# # # step9 直方图
# # plt.figure(figsize = (7,4))
# # plt.hist(y, label = ['1st', '2nd'], stacked = True, bins = 20)
# # plt.grid(True)
# # plt.legend(loc=0)
# # plt.xlabel('value')
# # plt.ylabel('frequency')
# # plt.title('Histogram')
# # plt.show()

# # # step10 箱型图
# # fig,ax = plt.subplots(figsize = (7,4))
# # plt.boxplot(y)
# #
# # plt.grid(True)
# # plt.legend(loc=0)
# # plt.xlabel('dataset')
# # plt.ylabel('value')
# # plt.title('Boxplot')
# # plt.show()
