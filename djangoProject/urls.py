"""
djangoProject 项目的 URL 配置。

`urlpatterns` 列表将 URL 路由到视图。更多信息请参见：
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
示例：
函数视图
    1. 添加导入：  from my_app import views
    2. 添加 URL 到 urlpatterns：  path('', views.home, name='home')
基于类的视图
    1. 添加导入：  from other_app.views import Home
    2. 添加 URL 到 urlpatterns：  path('', Home.as_view(), name='home')
包含另一个 URL 配置
    1. 导入 include() 函数：  from django.urls import include, path
    2. 添加 URL 到 urlpatterns：  path('blog/', include('blog.urls'))
"""


from django.urls import path

from . import views

# urlpatterns = [
#     path('hello/', views.hello),
# ]

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]


