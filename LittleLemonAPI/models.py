from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField()
    
    def __str__(self) -> str:
        return self.title
    
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    featured = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return self.title
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuItem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    class Meta:
        unique_together = ('menuItem', 'user')
    
        
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='delivery_crew', null=True)
    status = models.BooleanField(db_index=True, default=0)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.user
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menuItem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    class Meta:
        unique_together = ( 'order', 'menuItem')
    
    def __str__(self) -> str:
        return self.order