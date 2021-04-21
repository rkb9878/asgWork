from rest_framework import serializers

from manageAPI.models import User, Business, Products


class userRegisterS(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'password must match'})

        account.set_password(password)
        account.save()
        return account


class BusinessSerializers(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ['registrationNo', 'email', 'name', 'user']
        extra_kwargs = {
            'user': {'read_only': True}
        }


class productSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True}
        }

