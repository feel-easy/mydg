import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mydg.settings')
pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd)

import django

django.setup()

from configs.models import User, Config
from configs.utils import md5

user = User.objects.get_or_create(username='admin', sign=md5('admin123456'))
for i in range(100):
    Config.objects.get_or_create(
        user=user[0],
        nickname="管理员",
        title=f"测试配置{i}",
        desc=f"测试所加配置{i}",
        config="{}",
    )
