from django.db import models

from users.models import (TeacherUser)
from institutions.models import (Headquarters)
# Create your models here.


# Create model  to a groups........................................................................

class Journey(models.Model):
    """Represent a Journey object"""
    codeJourney = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nameJourney = models.CharField(null=False,max_length=100, unique=True)

    def __str__(self):
        return 'The Journey was created as: {}, with a code: {}'.format(
            self.nameJourney,
            self.codeJourney)

class Group(models.Model):
    """Represent a Group object"""
    nameGroup = models.CharField(primary_key=True,
                                 serialize=False,max_length=100)
    journeyGroup =  models.ForeignKey(Journey,related_name='groups', on_delete=models.CASCADE)
    managerGroup = models.OneToOneField(TeacherUser,
                                     on_delete=models.CASCADE)
    headquarter = models.ForeignKey(
        Headquarters, on_delete=models.CASCADE)


    def __str__(self):
        return 'The Group was created as: {}, with a journey: {}'.format(
            self.nameGroup,
            self.journeyGroup)
        
