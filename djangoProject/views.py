from django.shortcuts import render
import datetime


def hello(request):
    context_name = 'hello world'
    views_name = "hello django"
    view_list = ["菜鸟教程1", "菜鸟教程2", "菜鸟教程3"]
    views_dict = {"name": "菜鸟教程", "age": 18}
    now = datetime.datetime.now()
    return render(request,
                  'hello.html',
                  {"name": views_name,
                   "hello": context_name,
                   "view_list": view_list,
                   "views_dict": views_dict,
                   "time": now})
