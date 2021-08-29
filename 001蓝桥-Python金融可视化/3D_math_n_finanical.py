from matplotlib.patches import Polygon

# 第一步是定义需要求取积分的函数
def func(x):
    return 0.5 * np.exp(x) + 1
# 第二步是定义积分区间，生成必需的数值
a,b = 0.5, 1.5
x = np.linspace(0,2)
y = func(x)
# 第三步，绘制函数图形
fig,ax = plt.subplots(figsize=(7,5))
plt.plot(x,y,'b',linewidth=2)
plt.ylim(ymin = 0)
# 第四步是核心，我们使用 Polygon 函数生成阴影部分（“补丁”），表示积分面积
Ix = np.linspace(a, b)
Iy = func(Ix)
verts = [(a,0)] + list(zip(Ix,Iy)) +[(b,0)]
poly = Polygon(verts, facecolor = '0.7', edgecolor = '0.5')
ax.add_patch(poly)

# 第五步是用 plt.text 和 plt.figtext 在图表上添加数学公式和一些坐标轴标签。LaTeX 代码在两个美元符号之间传递（ … ）。两个函数的前两个参数都是放置对应文本的坐标值

# python可以使用latex指令
plt.text(0.5 * (a + b), 1, r"$\int_a^b fx\mathrm{d}x$", horizontalalignment='center', fontsize=20)
# 在图像的上尽头和右侧尽头加入指令
plt.figtext(0.9, 0.075, '$x$')
plt.figtext(0.075, 0.9, '$f(x)$')

ax.set_xticks((a,b))
ax.set_xticklabels(('$a$','$b$'))
ax.set_yticks([func(a),func(b)])
ax.set_yticklabels(('$f(a)$','$f(b)$'))
plt.grid(True)

plt.show()

# ****3d 金融分析可视化 *********************************************************************
# 行权价格50-150
from mpl_toolkits.mplot3d import Axes3D
strike = np.linspace(50,150,24)
# 到期日在0.5-2.5之间
ttm = np.linspace(0.5,2.5,24)
# 转化为二维数组
strike, ttm = np.meshgrid(strike, ttm)

iv = (strike -100 ) **2 /(100*strike)/ ttm

fig = plt.figure(figsize = (9,6))
ax = fig.gca(projection = '3d')


surf = ax.plot_surface(strike, ttm, iv, rstride = 2, cstride=2, cmap = plt.cm.coolwarm, linewidth=0.5, antialiased = True)

ax.set_xlabel('strike')
ax.set_ylabel('time-to-maturity')
ax.set_zlabel('implied volatility')

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

# ****改变散点图*********************

fig = plt.figure(figsize = (8,5))
ax = fig.add_subplot(111,projection = '3d')
ax.view_init(30,60)

ax.scatter(strike, ttm, iv, zdir = 'z', s = 25, c = 'b', marker = '^')

ax.set_xlabel('strike')
ax.set_ylabel('time-to-maturity')
ax.set_zlabel('implied volatility')
plt.show()
