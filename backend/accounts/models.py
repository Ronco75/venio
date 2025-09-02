from django.db import models
from django.contrib.auth.models import User

class Couple(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name1 = models.CharField(max_length=100)
    name2 = models.CharField(max_length=100)
    wedding_date = models.DateField()
    wedding_time = models.TimeField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    venue_name = models.CharField(max_length=200)
    venue_address = models.CharField(max_length=300)
    venue_city = models.CharField(max_length=100)
    total_budget = models.DecimalField(max_digits=10, decimal_places=2)
    expected_guests = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name1} & {self.name2}"