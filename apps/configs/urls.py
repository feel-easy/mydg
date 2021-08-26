
from django.urls import path


from . import views
app_name = 'configs'

urlpatterns = [
   path('', views.ConfigView.as_view(), name='index'),
]