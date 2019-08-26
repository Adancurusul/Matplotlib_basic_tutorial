import matplotlib.pyplot as plt
import numpy as np
'''
本篇
主要将了基础的图标元素的写法
每一个用法均封装成基础函数方便有需要的初学者直接调用
也可以直接在末尾运行看每个函数的效果
'''
def plot():#plot趋势
    x = np.linspace(0.5,10,1000)#a,b均匀取100个数
    y = np.cos(x)
    y1 = np.random.randn(100)# 标准正态分布取100个



    plt.plot(x,y,ls="-",lw = 2,label = "plot figure")#linestyle中，-是连续的曲线，:是点，-.是点加线，--是中间空的线
    plt.legend()
    plt.show()



def scatter():#变量间关系
    x = np.linspace(0.5,100,1000)#a,b均匀取100个数
    y = np.random.randn(1000)
    plt.scatter(x,y,label = "scatter figure")#变量间关系
    plt.legend()
    plt.show()


def xlim():#x轴显示范围
    x = np.linspace(0.5,100,1000)#a,b均匀取100个数
    y = np.random.randn(1000)
    plt.scatter(x,y,label = "scatter figure")#变量间关系

    plt.legend()

    plt.xlim(0.05,100)
    plt.ylim(0.05,1)
    plt.show()
def xlabel():#xy标签
    x = np.linspace(0.5,10,1000)#a,b均匀取100个数
    y = np.cos(x)

    plt.plot(x,y,ls="-.",lw = 2,c="g",label = "plot figure")#plot趋势
    plt.legend()

    plt.xlabel("x  x")
    plt.ylabel("y  y")


    plt.show()

def grid():#绘制刻度线
    x = np.linspace(0.5,10,1000)#a,b均匀取100个数
    y = np.sin(x)




    plt.plot(x,y,ls="-.",lw = 2,c = "b",label = "plot figure")
    plt.legend()

    plt.grid(linestyle=":",color = "r")
    plt.show()

def axhline():#平行于x的参考线,xvhline反之
    x = np.linspace(0.5,10,1000)#a,b均匀取100个数
    y = np.sin(x)

    plt.plot(x,y,ls="-",lw = 2,c = "b",label = "plot figure")
    plt.legend()

    plt.axhline(y = 0.0,c="r",ls = "--",lw = 2)
    plt.axvline(x = 4.0,c="r",ls = "-.",lw = 2)

    plt.show()



def axvspan():#垂直于x的参考区域
    x = np.linspace(0.5,10,1000)#a,b均匀取100个数
    y = np.sin(x)
    plt.plot(x,y,ls="-",lw = 2,c = "b",label = "plot figure")
    plt.legend()

    plt.axhspan(ymin = 0.0,ymax = 0.5,facecolor = "y",alpha = 0.3)
    plt.axvspan(xmin = 4.0,xmax = 6.0,facecolor = "y",alpha = 0.3)

    plt.show()


def annotate():#内部细节指向
    x = np.linspace(0.5,10,1000)#a,b均匀取100个数
    y = np.sin(x)

    plt.plot(x,y,ls="-.",lw = 2,c="g",label = "plot figure")#plot趋势
    plt.legend()

    plt.annotate("max",xy = (np.pi/2,1.0),xytext=((np.pi/2)+1,.8),c ="b",arrowprops=
                 dict(facecolor='black', shrink=0.05))
    '''
    xy=(横坐标，纵坐标)  箭头尖端
    xytext=(横坐标，纵坐标) 文字的坐标，指的是最左边的坐标
    arrowprops= {
        facecolor= '颜色',
        shrink = '数字' <1  收缩箭头
    }
'''



    #plt.annotate('local max', xy=(2,1), xytext=(3,1.5),
     #       arrowprops=dict(facecolor='black', shrink=0.05))

    plt.show()

def text():#无指向形注释
    x = np.linspace(0.5,10,1000)#a,b均匀取100个数
    y = np.sin(x)

    plt.plot(x,y,ls="-.",lw = 2,c="g",label = "plot figure")#plot趋势
    plt.legend()

    plt.text(3.10,0.09,"y = sin(x)",weight="bold",color="b")
    plt.show()


def title():#标题的使用
    x = np.linspace(0.5,10,1000)#a,b均匀取100个数
    y = np.cos(x)

    plt.plot(x,y,ls="-.",lw = 2,c="g",label = "plot figure")#plot趋势
    plt.legend()
    plt.title("y=cos(x)")
    plt.show()

def legend():#可以改变文本图标的位置
    x = np.linspace(0.5,10,1000)#a,b均匀取100个数
    y = np.cos(x)

    plt.plot(x,y,ls="-.",lw = 2,c="g",label = "plot figure")#plot趋势
    plt.legend(loc = "lower left")
    plt.show()






