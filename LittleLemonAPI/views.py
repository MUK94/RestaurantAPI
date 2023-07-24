from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from .models import MenuItem, Cart, Order, OrderItem
from .serializers import MenuItemSerializer, CartSerializer, OrderSerializer, OrderItemSerializer
from rest_framework.permissions import BasePermission

# MENU ITEM VIEWS
class MenuItemListView(generics.ListCreateAPIView):
    queryset =  MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    permission_classes = [IsAuthenticated]
    
class SingleItemListView(generics.RetrieveAPIView):
    queryset =  MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    permission_classes = [IsAuthenticated]


# CART VIEW
class CartListView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
    permission_classes = [IsAuthenticated]


# ORDER ITEM SERIALIZER
class OrderItemsListView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
    permission_classes = [IsAuthenticated]