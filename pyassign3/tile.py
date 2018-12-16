#!/usr/bin/env python3


"""tile.py:puzhuan

__author__ = "Changrui"

__pkuid__  = "1800011758"

__email__  = "706771104@qq.com"

"""

def puzhuan(m,n,a,b,ans,method,qiang):#铺砖函数
    count = 0
    q = 0
    for i in range(m*n):
        if qiang[i] == 0 and q == 0:#找出下一块没铺的墙
            pai = i//n + 1
            lie = i%n + 1
            q = 1
            if (pai + b - 1) <= m and (lie + a - 1) <= n:#判断横着铺是否超界
                for j in range(pai,pai + b):
                    for k in range(lie,lie + a):
                        if qiang[(j - 1)*n + k - 1] == 0:
                            count += 1
            if count == a*b:#判断能否横着铺
                l = []#l里放砖包括的墙号
                for j in range(pai,pai + b):
                    for k in range(lie,lie + a):
                        l.append((j - 1)*n + k - 1)
                        qiang[(j - 1)*n + k - 1] = 1
                method.append(l)#method为铺砖的一种方法
                if 0 not in qiang:
                    ans.append(method.copy())#ans为所有方法
                else:
                    puzhuan(m,n,a,b,ans,method,qiang)#递归
                for j in range(pai,pai + b):#把砖拿下来
                    for k in range(lie,lie + a):
                        qiang[(j - 1)*n + k - 1] = 0
                del method[-1]
            count = 0
            if (pai + a - 1) <= m and (lie + b - 1) <= n:#同理判断竖着铺
                for j in range(pai,pai + a):
                    for k in range(lie,lie + b):
                        if qiang[(j - 1)*n + k - 1] == 0:
                            count += 1
            if count == a*b:
                l = []
                for j in range(pai,pai + a):
                    for k in range(lie,lie + b):
                        l.append((j - 1)*n + k - 1)
                        qiang[(j - 1)*n + k - 1] = 1
                method.append(l)
                if 0 not in qiang:
                    ans.append(method.copy())   
                else:
                    puzhuan(m,n,a,b,ans,method,qiang)
                for j in range(pai,pai + a):
                    for k in range(lie,lie + b):
                        qiang[(j - 1)*n + k - 1] = 0
                del method[-1]
    return ans

def draw(m,n,a,b,method):#可视化
    import turtle
    t = turtle.Turtle()
    t.speed(3)
    t.color('blue')#画墙
    t.pensize(1)
    t.penup()
    t.goto(-20*n,-20*m)
    t.pendown()
    for i in range(m):#画横线和数字
        for j in range(n):
            t.forward(20)
            t.write(i*n + j)
            t.forward(20)
        t.penup()
        t.goto(-20*n,-20*m + (i + 1)*40)
        t.pendown()
    t.forward(40*n)
    t.left(90)
    t.penup()
    for i in range(n+1):#画竖线
        t.goto(-20*n + 40*i,-20*m)
        t.pendown()
        t.forward(40*m)
        t.penup()
    t.pencolor('black')
    t.pensize(5)
    for i in method:#画砖
        if i[-1] - i[0] == a*b - 1:
            t.goto(-20*n + 40*(i[0]%n), -20*m + 40*(i[0]//n))
            t.pendown()
            t.forward(40*b)
            t.right(90)
            t.forward(40*a)
            t.right(90)
            t.forward(40*b)
            t.right(90)
            t.forward(40*a)
            t.right(90)
            t.penup()
        else:
            t.goto(-20*n + 40*(i[0]%n), -20*m + 40*(i[0]//n))
            t.pendown()
            t.forward(40*a)
            t.right(90)
            t.forward(40*b)
            t.right(90)
            t.forward(40*a)
            t.right(90)
            t.forward(40*b)
            t.right(90)
            t.penup()
    turtle.done()
    
def main():#main函数
    m = int(input('请输入墙长'))
    n = int(input('请输入墙宽'))
    a = int(input('请输入瓷砖长'))
    b = int(input('请输入瓷砖宽'))
    qiang = [0]*m*n
    if m*n%(a*b) != 0:#判断能否铺
        print("无法铺瓷砖")
        return 
    else:
        ans = []
        method = []
        ans1 = []
        puzhuan(m,n,a,b,ans,method,qiang)
        for i in ans:#排除重复（正方形瓷砖或墙）
            if i not in ans1:
                ans1.append(i)
        print('共有%d种铺法'%len(ans1))
        for i in range(len(ans1)):
            print('第%d种'%(i+1),ans1[i])
            print('\n')
        shy = int(input('选择的方案1-%d：'%(i+2)))
        draw(m,n,a,b,ans1[shy-1])
    
if __name__ == '__main__':
    main()
