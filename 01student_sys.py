#while true
#1.学生信息保存在字典里面
#2.所有学生信息保存在列表里面
#3.打印提示
#4.用户输入
#5.拿到用户输入的结果
#6.根据结果选择要做的事情，及选择要调用的函数
#7.搜索展示全部、搜索一个学生，增加，修改，删除信息

student_list = [{'name':'Major','age':23,'stu_num':10000}]
def print_info():
    print('*'*20)
    print('欢迎来到学生管理系统')
    print('1.展示全部学生')
    print('2.搜索一个学生')
    print('3.增加一个学生')
    print('4.修改一个学生')
    print('5.删除一个学生')
    print('6.退出')
    print('*'*20)
    user_input = input('>>>>请选择序号：')
    return user_input

# 展示全部学生
def show_all_stu():
    for stu in student_list:
        print(stu)

# 搜索一个学生
def search_stu():
    user_input_name = input('>>>>请输入学生名字：')
    stu_exist = False
    for stu in student_list:
        if stu['name'] == user_input_name:
            stu_exist = True
            print(stu)
    if stu_exist == False:
        print('您要搜索的学生不存在')

#新增一个学生
def add_stu():
    stu_name = input('>>>>请输入要添加的学生姓名：')
    stu_age = input('>>>>请输入要添加的学生年龄：')
    stu_num = input('>>>>请输入要添加的学生学号：')
    new_stu = {'name':stu_name,'age':stu_age,'num':stu_num}
    student_list.append(new_stu)
    print('学生：{}信息添加成功！'.format(stu_name))

#修改一个学生
def modify_stu():
    stu_name = input('>>>>请输入要修改的学生姓名：')
    stu_exist = False
    for stu in student_list:
        if stu['name'] == stu_name:
            stu_age = input('请输入修改后的年龄：')
            stu_num = input('请输入修改后的学号：')
            stu['age'] = stu_age
            stu['num'] = stu_num
            stu_exist = True
            print('学生：{}信息已更新成功！'.format(stu_name))
    if not stu_exist:
        print('您要修改的学生不存在')

# 删除一个学生
def del_stu():
    stu_name = input('>>>>请输入您要删除的学生姓名：')
    stu_exist = False
    for stu in student_list:
        if stu['name'] == stu_name:
            student_list.remove(stu)
            stu_exist = True
            print('学生：{}信息已删除成功！'.format(stu_name))
    if not stu_exist:
        print('您要删除的学生不存在')


def main():
    while True:
        user_input = print_info()
        if user_input in ['1','2','3','4','5','6']:
            if user_input == '1': #展示所有学生
                show_all_stu()
            elif user_input == '2': #查看一个学生
                search_stu()
            elif user_input == '3': #增加一个学生
                add_stu()
            elif user_input == '4': #修改一个学生
                modify_stu()
            elif user_input == '5': #删除一个学生
                del_stu()
            elif user_input == '6': #退出程序
                print('再见')
                break
        else:
            print('输入错误，请重新输入')
main()