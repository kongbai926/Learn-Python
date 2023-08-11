# 这是一个示例 Python 脚本。
import pymysql


class MyDatabase:
    # 数据库连接信息
    connect_information = {'host': "rm-cn-5yd36xt2s000a27o.rwlb.rds.aliyuncs.com",
                           'port': 3306,
                           'user': 'mysql_test1',
                           'password': '200110Zdp@',
                           'charset': 'utf8'
                           }

    def __init__(self, meth='POST'):
        # 连接数据库
        self.db = pymysql.connect(**self.connect_information)
        self.cursor = self.db.cursor()  # 创建游标对象
        self.CreateDBM()
        self.meth = meth  # 网页请求方式：注册\登录

    # 创建数据库
    def CreateDBM(self):
        try:
            dbname = 'userDataBase'
            sql = 'create database if not exists %s' % dbname  # 创建数据库
            self.cursor.execute(sql)
            sql = 'show databases'
            self.cursor.execute(sql)
            print('创建新的数据库后：', self.cursor.fetchall())  # 获取创建数据库后全部数据库
        except BaseException as error:
            print(error)
        finally:
            self.cursor.close()
            self.db.close()  # 关闭数据库相关连接

    # 连接创建的数据库
    def Connect_DataBase(self):
        dbname = input('数据库名称：\t')  # 数据库名称
        try:
            self.db = pymysql.connect(**self.connect_information, **{"database": dbname})
            self.cursor = self.db.cursor()
        except BaseException as err:
            print(err)

    # 关闭数据库连接
    def CloseDataBase(self):
        self.cursor.close()
        self.db.close()

    # 提交修改数据库SQL语句
    def Submit_DataBase(self):
        self.db.commit()

    # 创建数据表
    def CreateTable(self):
        self.Connect_DataBase()  # 连接到数据库

        table_name = '用户表'  # 数据表名称
        sql_command = 'create table if not exists %s (id int(10) not null auto_increment primary key, 用户名 varchar(20) not null, 密码 varchar(8) not null, 性别 varchar(2), 年龄 int(3))' % table_name
        try:
            self.cursor.execute(sql_command)  # 执行SQL语言
            print('数据表创建成功')
        except Exception as error:
            print(error)
        finally:
            self.CloseDataBase()

    def SelectData(self):
        """
        这里使用POST 与 GET 区别登录与注册两种请求方式。其中，POST代表注册，GET代表登录。在实际使用时可根据个人所需改变判断条件中的值。
        :return:
        """
        self.Connect_DataBase()
        if self.meth == 'POST':
            user_name = input("用户名：\t")  # 实际应该使用request.GET.get('username', None)获取页面username输入框中输入的用户名。为了测试方便，这里直接使用input方式获取
            user_password = input('密码：\t')
            user_xb = input('性别：\t')
            user_age = input('年龄：\t')

            sql_command = "insert into `用户表`( `用户名` , `密码` , `性别` , `年龄` )  values ('%s', '%s', '%s', %d)" % (user_name, user_password, user_xb, int(user_age))
            try:
                self.cursor.execute(sql_command)
                print('注册成功！')
                self.Submit_DataBase()
            except BaseException as err:
                print(err)
        elif self.meth == 'GET':
            user_name = input('用户名：\t')
            user_password = input('密码：\t')
            sql_command = "select * from `用户表` where `用户名` = '{}' and `密码` = {}".format(user_name, user_password)
            try:
                # print('SQL语句：', sql_command)
                lc = self.cursor.execute(sql_command)
                if not lc:
                    print('用户名或密码错误！')
                else:
                    print('登录成功')  # 此后代码可更换为登录部分的代码。这里已经查找出匹配的用户名与密码数据
            except BaseException as err:
                print(err)
        self.CloseDataBase()


if __name__ == '__main__':
    mydatabase = MyDatabase(meth='GET')
    # mydatabase.CreateTable()
    mydatabase.SelectData()  # 执行查询语句
