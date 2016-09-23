###django
是一个开放源代码的WEB应用框架，由PYTHON携程
#####1.django-admin.py startproject testdj 创建一个testdj项目
#####2.python manage.py runserver 运行启动项目
#####3.urls.py 这个文件起到路由的作用，view.py主要是服务器response处理逻辑使用，templates主要是模板
#####4.python manage.py startapp TestModel  创建一个应用，一个项目可以有多个项目，需要在INSTALLED_APPS加入

###表单
#####HTML表单是网站交互性的经典方式
#####{% for i in TutorialList %}
#####{{ i }}
#####{% endfor %}

#####获取当前网址：{{ request.path }}
#####获取当前参数：{{ request.GET.urlencode }}
<a href="{{ request.path }}?{{ request.GET.urlencode }}&delete=1">当前网址加参数 delete</a>


