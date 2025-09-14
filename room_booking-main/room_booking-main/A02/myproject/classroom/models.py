from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RoomData(models.Model):
    room_code = models.CharField(max_length=6)
    room_name = models.CharField(max_length=10)
    room_capacity = models.IntegerField()
    available_hours = models.PositiveIntegerField(default=0)
    room_available = models.BooleanField()

    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room_user = models.ForeignKey(RoomData, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)
    hours = models.PositiveIntegerField(default=1)  

    def __str__(self):
        return f"{self.user.username} booked {self.room_user.room_name}"