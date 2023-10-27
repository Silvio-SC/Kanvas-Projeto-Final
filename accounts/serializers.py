from rest_framework import serializers
from .models import Account
# from courses.serializers import CourseSerializer


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id',
            'username',
            'password',
            'email',
            'is_superuser',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True},
            # 'is_superuser': {'required': False}
        }

    def create(self, validated_data: dict) -> Account:
        superuser = validated_data.get('is_superuser')
        if superuser:
            return Account.objects.create_superuser(**validated_data)
        else:
            return Account.objects.create_user(**validated_data)
