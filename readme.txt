1、新建项目 创建虚拟环境virtual venv
2、安装django模块 pip install django     (自动安装 pytz  sqlparse 模块)

使用mysql数据库,需要提前安装好 https://dev.mysql.com/downloads/windows  PyMySQL
3、安装mysql数据库驱动 pip install pymysql ，导入模块后加上 pymysql.install_as_MySQLdb() 为发挥最大数据库操作性能
4、创建Django项目 django-admin startproject mybog
   基本的server已经可以运行了, python manage.py runserver

5、创建app， python manage.py startapp blog

6、a.修改项目setting.py的全局配置，DATABASES 为mysql数据库，INSTALLED_APPS 增加新增的app名，
LANGUAGE_CODE = 'zh_Hans' TIME_ZONE = 'Asia/Shanghai'  DEBUG = True
TEMPLATES =
b.并在__init__.py中 import pymysql 、pymysql.install_as_MySQLdb()
c.修改urls.py的路由

7、给app应用添加数据models模型类表
8、生成数据迁移脚本文件 python manage.py makemigrations 执行数据库迁移 生成数据表 python manage.py migrate
9、生成数据库超级用户及密码  python manage.py createsuperuser
10、管理后台 admin.py
11、创建表单forms.py、视图views 前台调阅
12、定义模板 {% %} 提高效率

19、启动服务器  python manage.py runserver