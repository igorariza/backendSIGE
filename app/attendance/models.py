from django.db import models
from users.models import User

# Create your models here.
class Attendance(models.Model):
    """This class is a model to represent in obj the class attendance"""
    attendance_date = models.DateTimeField(auto_now_add=True)
    attendance = models.BooleanField(default=False)
    user_id= models.ForeignKey(User, on_delete=models.PROTECT, related_name="user")