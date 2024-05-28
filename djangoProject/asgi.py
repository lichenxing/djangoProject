"""

djangoProject 项目的 ASGI 配置。

它将 ASGI 可调用对象暴露为一个名为 ``application`` 的模块级变量。

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")

application = get_asgi_application()
