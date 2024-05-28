"""
WSGI 配置用于 djangoProject 项目。

它将 WSGI 可调用对象暴露为一个名为 ``application`` 的模块级变量。

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")

application = get_wsgi_application()
