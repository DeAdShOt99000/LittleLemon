from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import MenuItem

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']

class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
        
# class BookingSerializer(ModelSerializer):
#     class Meta:
#         model = Booking
#         fields = '__all__'
