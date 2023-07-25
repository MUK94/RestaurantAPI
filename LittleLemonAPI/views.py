from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group
from .models import MenuItem, Cart, OrderItem
from .serializers import MenuItemSerializer, CartSerializer, OrderItemSerializer, UserDetailSerializer


# MENU ITEM VIEWS
class MenuItemListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MenuItemSerializer
    
    queryset =  MenuItem.objects.all()
    
    ordering_fields = ['price']
    search_fields = ['title', 'category__title']
    
class SingleItemView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MenuItemSerializer
    
    queryset =  MenuItem.objects.all()
    
    
# CART VIEW
class CartListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user)

    # Implement HTTP methods here POST DELETE
    def post(self, request):
        # Add menu item to the card for current user
        menuItem_id = request.data['menuItem']
        quantity = request.data['quantity']
        unit_price = request.data['unit_price']
        price = request.data['price']

        if not menuItem_id:
            return Response({'error': 'Menu item ID id required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            menuItem = MenuItem.objects.get(id=menuItem_id)
        except MenuItem.DoesNotExist:
            return Response({'error': 'Menu item not found'}, status=status.HTTP_404_NOT_FOUND)
        
        cartItem = Cart(user=request.user, menuItem=menuItem, quantity=quantity, unit_price=unit_price, price=price)
        cartItem.save()
        
        serializer = CartSerializer(cartItem)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def delete(self, request):
        user = self.request.user
        Cart.objects.filter(user=user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ORDER ITEM SERIALIZER
class OrderItemsListView(generics.ListCreateAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
    
    queryset = OrderItem.objects.all()
    
    
    
class SingleOrderItemView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]
    
    queryset = OrderItem.objects.all()
    

class ManagerUsersView(generics.ListCreateAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Check if user is manager
        if not self.request.user.groups.filter(name='Manager').exists():
            return User.objects.none()

        # Return all user managers
        return User.objects.filter(groups__name='Manager')
    
    def post(self, request):
        # Check if user is manager
        if not self.request.user.groups.filter(name='Manager').exists():
            return Response({'error': 'You are not authorized to add a user'}, status=status.HTTP_403_FORBIDDEN)
        
        username = request.data['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'error': 'User not Found.'}, status=status.HTTP_404_NOT_FOUND)
        

        
        managerGroup = Group.objects.get(name='Manager')
        user.groups.add(managerGroup)
        
        return Response({'message': f'User {user.username} added to the Manager Group'}, status=status.HTTP_201_CREATED)
    
    
class DeliveryCrewUsersView(generics.ListCreateAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Check if user is manager
        if not self.request.user.groups.filter(name='Manager').exists():
            return User.objects.none()

        # Return all user managers
        return User.objects.filter(groups__name='Delivery Crew')
    
    def post(self, request):
        # Check if user is manager
        if not self.request.user.groups.filter(name='Manager').exists():
            return Response({'error': 'You are not authorized to add a user'}, status=status.HTTP_403_FORBIDDEN)
        
        username = request.data['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'error': 'User not Found.'}, status=status.HTTP_404_NOT_FOUND)
        
        deliveryCrew = Group.objects.get(name='Delivery Crew')
        user.groups.add(deliveryCrew)
        
        return Response({'message': f'User {user.username} added to the Delivery Crew Group'}, status=status.HTTP_201_CREATED)