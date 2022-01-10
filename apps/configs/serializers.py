from rest_framework import serializers
from .models import Config, User
from .utils import md5


class ConfigListSerializer(serializers.ModelSerializer):  # ModelSerializer和model相对应
   # 需要魔改的字段, 配合get_user_like食用
   user_like = serializers.SerializerMethodField(read_only=True)

   # 新增的数据库里没有的, 自定义的字段
   username = serializers.CharField(write_only=True)
   sign = serializers.CharField(write_only=True)

   """
   此函数用于配合SerializerMethodField, 具体就是xxx前面加上一个get_, 这样就可以对字段进行个性化设置, 如+1什么的
   """
   def get_user_like(self, obj):
       return obj.user_like.all().count()

   """
   此函数用于验证表单是否有问题,  没问题返回attrs, 否则raise serializers.ValidationError()
   """
   def validate(self, attrs):
       if md5(attrs['username'] + "123456") != attrs["sign"]:  # 验证签名
           raise serializers.ValidationError("用户签名错误")
       return attrs

   """
   此函数用于重载save, 建议在此处写上保存入数据库操作, 后面有用
   """
   def save(self, **kwargs):
       user = User.objects.get_or_create(username=self.validated_data["username"], sign=self.validated_data["sign"])[0]
       Config.objects.get_or_create(  # 存储配置
           user=user,
           nickname=self.validated_data["nickname"],
           title=self.validated_data["title"],
           desc=self.validated_data["desc"],
           config=self.validated_data["config"],
       )

   class Meta:
       # 设置对于model
       model = Config

       # 用于表示所有的出现的字段
       fields = ('uid', 'nickname', 'title', 'desc', 'config', 'user_like', 'last_download', 'username', 'sign')
       # 此字段用于设置fields的权限 read_only: 只有get里有   write_only: 只有post里有
       extra_kwargs = {
           "uid": {"read_only": True},
           "user_like": {"read_only": True},
           "last_download": {"read_only": True},
       }

class ConfigSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Config
        fields = '__all__'


