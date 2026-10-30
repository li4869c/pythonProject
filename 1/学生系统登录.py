#存储学生信息
i=[]
#修改学生信息 
def a5():
    name1 = input("请输入你的名字：")
    for usr1 in i:
        if name1 == usr1["名字"]:
            b1=input("请输入你要修改的年龄")
            b2=input("请输入你要修改的学号")
            usr1["年龄"]=b1
            usr1["学号"]=b2
            print("你已修改成功")
#删除学生信息
def a4():
    name1 = input("请输入你的名字：")
    for usr1 in i:
        if name1 == usr1["名字"]:
            i.remove(usr1)
            print("删除成功")
#查询该学生信息
def a3():
    name1 = input("请输入你的名字：")
    for usr1 in i:
        if name1 == usr1["名字"]:
            print(f"你的年龄:{usr1["年龄"]}和学号:{usr1["学号"]}")
# 界面显示函数
def id():
    print("=" * 10, "学生信息管理系统", "=" * 10)
    print("1.添加学生信息:")
    print("2.显示全体学生信息:")
    print("3.查询学生信息:")
    print("4.删除学生信息:")
    print("5.修改学生信息:")
    print("6.退出系统")#界面显示
#添加学生函数
def a1():
    global usr
    name = input("请输入你的名字：")
    age = input("请输入你的年龄：")
    number = input("请输入你的学号：")
    usr = {"名字": name, "年龄": age, "学号": number}
    i.append(usr)
    return i
#重复循环
while True:
    id()
    a=int(input("请输入你需要的功能:"))#选择功能用的
    if a==1:#
        print("您选择了【添加学生信息】")
        a1()
        print("添加成功",usr)
    elif a==2:#
        print("您选择了【显示学生信息】")
        for k in i:
            print(f"{k["名字"]}\t\t{k["年龄"]}\t\t{k["学号"]}")
    if a==3:
        print("您选择了【显示学生信息】")
        a3()
    if a==4:
        print("您选择了【删除学生信息】")
        a4()
    if a==5:
        print("您选择了【修改学生信息】")
        a5()
    if a==6:
        b=input("你确定要退出吗（yes or no）")
        #判断是否确认退出
        if b=="yes":
            print("你已退出成功")
            break
        else:
            id()
        #