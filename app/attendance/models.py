from django.db import models
from users.models import CustomUser
from forum.models import Feed

# Create your models here.


class Attendance(models.Model):
    """This class is a model to represent in obj the class attendance"""
    attendance_date = models.DateTimeField(auto_now_add=True)
    attendance = models.BooleanField(default=False)
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT, related_name="user")
    forum_feed_id = models.ForeignKey(
        Feed, on_delete=models.PROTECT, related_name="attendance")