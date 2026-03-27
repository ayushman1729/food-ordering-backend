from django.db import models

# Create your models here.
class FoodItem(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.TextField()

    def __str__(self):
        return self.name
    
class Order(models.Model):
    food_item=models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"
        
