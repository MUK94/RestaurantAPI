from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, MenuItem, Cart, Order, OrderItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class MenuItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'featured', 'category']

        
class CartSerializer(serializers.ModelSerializer):
    menuItem = MenuItemSerializer()
    
    class Meta:
        model = Cart
        fields = ['id', 'user', 'menuItem', 'quantity', 'unit_price', 'price']
        
    
class OrderItemSerializer(serializers.ModelSerializer):
    menuItem = MenuItemSerializer(read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'menuItem', 'quantity', 'unit_price', 'price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'items', 'delivery_crew', 'status', 'total', 'date']
    

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
      
        
