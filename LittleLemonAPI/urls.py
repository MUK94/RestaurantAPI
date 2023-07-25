from django.urls import path
from .views import MenuItemListView, SingleItemView, CartListView, OrderItemsListView, SingleOrderItemView, ManagerUsersView, DeliveryCrewUsersView

urlpatterns = [
    path('menu-items', MenuItemListView.as_view()),
    path('menu-items/<int:pk>', SingleItemView.as_view()),
    
    path('cart/menu-items', CartListView.as_view()),
    
    path('orders', OrderItemsListView.as_view()),
    path('orders/<int:pk>', SingleOrderItemView.as_view()),
    
    path('groups/manager/users', ManagerUsersView.as_view()),
    path('groups/delivery-crew/users', DeliveryCrewUsersView.as_view()),

]