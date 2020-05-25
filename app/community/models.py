from django.db import models
from django.conf import settings
# Importamos los usuarios.
from users.models import CustomUser
import uuid

# Create model to Community ...................................................................


class Community(models.Model):
    """Represent a Community object"""
    codeCommunity = models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                     verbose_name='ID')
    titleCommunity = models.CharField(max_length=255)
    dateCommunity = models.DateField(auto_now_add=True)
    descriptionCommunity = models.CharField(max_length=10000)
    user = models.ForeignKey(
        CustomUser, related_name='Communitys', on_delete=models.PROTECT)

    class Meta:
        ordering = ['codeCommunity', 'dateCommunity']

    def __str__(self):
        return 'The Community was created as: {}'.format(self.nameCommunity)
