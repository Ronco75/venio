from django.db import models
from accounts.models import Couple


class Group(models.Model):
        couple_id = models.ForeignKey(Couple, on_delete=models.CASCADE)
        group_name = models.CharField(max_length=100)
        group_description = models.CharField(max_length=200, null=True, blank=True)
        created_at = models.DateTimeField(auto_now_add=True)
        
        def __str__(self):
            return self.group_name
            

class Guest(models.Model):
    couple_id = models.ForeignKey(Couple, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    invited_count = models.IntegerField(default=1)
    confirmed_count = models.IntegerField(null=True, blank=True)
    rsvp_status = models.CharField(max_length=20, default='not_sent', null=True, blank=True)
    response_status = models.CharField(max_length=20, default='pending', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"