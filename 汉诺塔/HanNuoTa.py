import turtle
from MainWindow import *
global step
step=0
def drawpoles():  #画柱子
    global pole_number
    def drawpole(k):
        t.color("black")
        t.penup()
        t.pensize(10)
        t.speed(300)
        t.goto(300*(k-1),100)
        t.down()
        t.goto(300*(k-1),-100)   #设置柱子的位置，根据k来使这个盘子均匀放置，美观
        t.goto(300*(k-1)+40,-100)
        t.goto(300*(k-1)-40,-100)
    t=turtle.Turtle()
    t.hideturtle()  #隐藏箭头显示
    for i in range(pole_number):
        drawpole(i)

def drawplates(n):   #在这里的话，要考虑到有几个盘子，来画盘子，区分盘子的大小是关键。
#然后我思考了一下，汉诺塔三根柱子，八个盘子的话移动要移动差不多255次，再往上就很复杂很多步了，所以这里我做的程序最高层数设定为八层比较合适
    plates=[turtle.Turtle() for i in range(n)]
    for i in range(n):
        plates[i].penup()
        plates[i].shape("square")
        #plates[i].hideturtle()
        plates[i].shapesize(1,9-i)
        plates[i].goto(0,-90+20*i)
        #plates[i].showturtle()
    return plates

#下一步，考虑算法，然后移动盘子，具体如何移动，用递归算
#在递归过程中可以得出下一步要从哪个柱子上的盘子移动到哪个柱子，但是要实现盘子移动的动画得要知道柱子上面盘子的编号
#由此考虑，把柱子上面的盘子用三个栈来存储比较好

class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return len(self.items)==0
    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def pop(self):
        return self.items.pop()
    def push(self,item):
        self.items.append(item)


def PoleStack():
    pole_stack=[Stack() for i in range(3)]
    return pole_stack

def hanoi(plates,pole_stack,n,a,b,c):
    if n>0:
        hanoi(plates,pole_stack,n-1,a,c,b)
        move(plates,pole_stack,a,b)
        pole_stack[b].push(pole_stack[a].pop())
        hanoi(plates,pole_stack,n-1,c,b,a)

def move(plates,pole_stack,fp,tp):
    global step
    ismove=pole_stack[fp].peek()
    plates[ismove].speed(3)
    plates[ismove].goto((fp-1)*300,150)
    plates[ismove].goto((tp-1)*300,150)
    height=pole_stack[tp].size()
    plates[ismove].goto((tp-1)*300,-90+20*height)
    step+=1
    print(step)



turtle.setup(1000,600,0,0)
drawpoles()
plates=drawplates(n)
poles=PoleStack()

for i in range(n):
    poles[1].push(i)
hanoi(plates,poles,n,1,2,0)

print("汉诺塔移动完成")
turtle.Screen().exitonclick()      #防止一运行完窗口就自动关闭了

