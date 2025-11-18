from django.contrib.auth.hashers import make_password
from .models import Users

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Users
        fields = ['email', 'fullname', 'password']

    def create(self, validated_data):
        validated_data['passwordhash'] = make_password(validated_data.pop('password'))
        validated_data['role'] = 'User' 
        return super().create(validated_data)

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)