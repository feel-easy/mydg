from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Config
from .serializers import ConfigListSerializer, ConfigSerializer


class ConfigView(APIView):
   def get(self, request):
       config_list = Config.objects.all()  # 取所有数据
       serializer = ConfigListSerializer(config_list, many=True)  # 建立serializer实例
       return Response(serializer.data, status=status.HTTP_200_OK)  # 返回序列化内容

   def post(self, request):
       serializer = ConfigListSerializer(request.data)  # 从表单里取出内容
       if serializer.is_valid():  # 验证表单是否有问题, 就是调用了validate函数
           serializer.save()  # 没问题的话则保存对象
           return Response({"data": "创建完成"}, status=status.HTTP_201_CREATED)
       return Response({"error": "表单错误"}, status=status.HTTP_400_BAD_REQUEST)

class ConfigViewSet(ModelViewSet):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer