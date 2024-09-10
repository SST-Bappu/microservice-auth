from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Name: User list serializer
    """
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'date_joined')
    
    def create(self, validated_data):
        user = User(
            name=validated_data['name'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])  # This hashes the password
        user.save()
        return user
class RoleSerializer(serializers.ModelSerializer):
    """
    Name: Role list serializer
    """

    class Meta:
        model = User
        fields = ['id','name']

