#Author lpf
#usr/bin/src
"""
 
"""
import turtle
from svg_turtle import SvgTurtle
import svgwrite
 
# 定义大圆半径200,则小圆半径big_radius * 0.5, 假如内部最小圆半径为big_radius*0.15
big_radius = 200

 
def main():
    turtle.reset()
    turtle.shape("turtle")
    yin("black", "white", 1)
    yin("white", "black", -1)
    # from PIL import ImageGrab
 
    # img = ImageGrab.grab((497, 179, 1434, 974)) #根据内存进行截屏
    # img = ImageGrab.grabclipboard()
    # img.save('test.jpg', 'JPEG')
    turtle.ht()
 
 
def yin(big_fillcolor, inner_fillcolor, direction):
    """
    画一半阴阳八卦
    :param big_fillcolor:   外部大圆填充色
    :param inner_fillcolor: 内部小圆填充色
    :param direction: 1表示开始默认开始方向向右,-1表示开始默认开始方向向左
    :return:
    """
    turtle.pensize(3)
    # 设置pencolor和fillcolor
    turtle.color("black", big_fillcolor)
    # 开始填充
    turtle.begin_fill()
    # 画内半圆
    turtle.circle(big_radius / 2.0, 180)
    # 画外半圆
    turtle.circle(big_radius, 180)
    # 海龟箭头左转180度
    turtle.lt(180)
    # 反方向画内半圆,反方向画圆,半径前要加 -
    turtle.circle(-big_radius / 2.0, 180)
    # 结束填充
    turtle.end_fill()
    # 画笔抬起
    turtle.pu()
    # 从画笔当前位置开始画圆,因此需要减去内圆半径,y方向移动,x方向不变
    turtle.sety(direction * big_radius * (0.5 - 0.15))
    # 画笔放下
    turtle.pd()
    # 设置pencolor和fillcolor
    turtle.color(big_fillcolor, inner_fillcolor)
    # 开始填充内圆
    turtle.begin_fill()
    # 画内圆
    turtle.circle(big_radius * 0.15)
    # 结束填充内圆
    turtle.end_fill()
    # 画笔抬起
    turtle.pu()
    # 海龟箭头回到(0, 0)坐标
    turtle.goto(0, 0)
    # 画笔放下
    turtle.pd()
    # 海龟箭头左转180度
    turtle.lt(180)
 
    return "Done!"
 
 
if __name__ == '__main__':
    main()
    turtle.mainloop()