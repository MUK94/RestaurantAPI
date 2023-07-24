from django.urls import path
from .views import MenuItemListView, SingleItemListView


urlpatterns = [
    path('menu-items', MenuItemListView.as_view()),
    path('menu-items/<int:pk>', SingleItemListView.as_view()),
]