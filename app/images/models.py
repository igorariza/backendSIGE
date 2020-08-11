from django.db import models
from secctions.models import Responses
# Create your models here.


class ImageResponse(models.Model):
    """Represent a image object in a response"""
    name = models.CharField(max_length=100, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    url = models.URLField(null=True, max_length=5000)
    response = models.ForeignKey(
        Responses, related_name="images", on_delete=models.CASCADE)


