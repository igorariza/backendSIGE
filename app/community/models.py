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
        return 'The Community was created as:'


class Addfile(models.Model):
    """Represent a Resource object"""
    codefile = models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                verbose_name='ID')
    post = models.OneToOneField(
        Community, related_name='file', on_delete=models.CASCADE)
    file = models.FileField(upload_to='Community/', blank=True)


class Replay(models.Model):
    """Represent a Resource object"""
    codereplay = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT)
    comment = models.CharField(max_length=5000)
    datereplay = models.DateTimeField(auto_now_add=True)
    replay = models.ForeignKey(
        Community, related_name='replays', on_delete=models.CASCADE)

    def __str__(self):
        return 'The replay was created with code: {}'.format(self.codereplay)
