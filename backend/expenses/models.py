from django.db import models
from accounts.models import Couple
import random

def generate_random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

class Category(models.Model):
    couple_id = models.ForeignKey(Couple, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100)
    color_code = models.CharField(max_length=7, default=generate_random_color)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

class Expense(models.Model):
    couple_id = models.ForeignKey(Couple, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    vendor_name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    amount_remaining = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vendor_name

class ExpenseDocument(models.Model):
    expense_id = models.ForeignKey(Expense, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=100)
    file_path = models.FileField(upload_to='expense_documents/')
    file_type = models.CharField(max_length=10)
    file_size = models.IntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name