
from django.urls import path
from rest_framework.routers import DefaultRouter


from . import views
app_name = 'configs'

urlpatterns = [
   path('', views.ConfigView.as_view(), name='index'),
]

router = DefaultRouter()  # 可以处理视图的路由器
router.register('books', views.ConfigViewSet)  # 向路由器中注册视图集

urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中