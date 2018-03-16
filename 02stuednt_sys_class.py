class StudentSystem:
    def __init__(self):
        self.student_list = [{'name':'Major_','age':18,'num':10000}]
    def print_info(self):
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

    def show_all_student_info(self):
        for stu in self.student_list:
            print(stu)
    
    def search_student(self):
        search_student_name = input('>>>>>请输入要搜索的学生姓名：')
        stu_exist = False
        for stu in self.student_list:
            if stu['name'] == search_student_name:
                stu_exist = True
                print(stu)
        if not stu_exist:
            print('>>>>您要查找的学生不存在')
    
    def add_student(self):
        name = input('>>>>请输入要增加的学生的姓名：')
        age = input('>>>>请输入要增加的学生的年龄：')
        num = input('>>>>请输入要增加的学生的学号：')
        new_student = {'name':name,'age':age,'num':num}
        self.student_list.append(new_student)
        print('>>>>新的学生{}添加成功'.format(name))

    def del_student(self):
        name = input('>>>>请输入要删除的学生的姓名：')
        stu_exist = False
        for stu in self.student_list:
            if stu['name'] == name:
                stu_exist = True
                self.student_list.remove(name)
                print('>>>>学生{}信息删除成功'.format(name))
        if not stu_exist:
            print('>>>>学生信息不存在')

    def modify_student_info(self):
        name = input('>>>>请输入要修改学生姓名：')
        stu_exist = False
        for stu in self.student_list:
            if stu['name'] == name:
                stu_exist = True
                stu['age'] = input('>>>>请输入要修改的学生年龄：')
                stu['num'] = input('>>>>请输入要修改的学生学号：')
                print('学生信息修改成功！')
        if not stu_exist:
            print('>>>>修改学生不存在')
        
    def main(self):
        while True:
             # 1.提示信息，让用户输入
             user_input = self.print_info()
             # 2.判断用户输入
             if user_input in ['1','2','3','4','5','6']:
                    #2.1 用户选择查看所有
                    if user_input == '1':
                        self.show_all_student_info()
                    #2.2 用户选择搜索学生
                    elif user_input == '2':
                        self.search_student()
                    #2.3 用户选择增加学生
                    elif user_input == '3':
                        self.add_student()
                    #2.4 用户选择删除学生
                    elif user_input == '4':
                        self.del_student()
                    #2.5 用户选择修改学生
                    elif user_input == '5':
                        self.modify_student_info()
                    #2.6 用户选择退出
                    elif user_input == '6':
                        print('>>>>再见，欢迎下次再来')
                        break

             else:
                 print('输入有误，请重新选择')

if __name__  == '__main__':
    student_sys = StudentSystem()
    student_sys.main()

