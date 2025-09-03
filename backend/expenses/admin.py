from django.contrib import admin
from .models import Category, Expense, ExpenseDocument

admin.site.register(Category)
admin.site.register(Expense)
admin.site.register(ExpenseDocument)
