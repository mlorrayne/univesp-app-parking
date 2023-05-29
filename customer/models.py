from django.db import models
from django.urls import reverse


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    number_plate = models.CharField(max_length=8)
    area_code = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=9)
    city = models.CharField(max_length=30)
    entry_time = models.DateTimeField(auto_now_add=True)
    departure_time =  models.TimeField(auto_now=False, auto_now_add=False)
    active = models.BooleanField(default=True)
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return reverse("customer:customer-update", kwargs={"id": self.id})
    
    def get_delete_url(self):
        return reverse("customer:customer-delete", kwargs={"id": self.id})
    
    class Meta:
        db_table = "customer"
    
