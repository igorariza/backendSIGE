from django.db import models

from users.models import TeacherUser
from institutions.models import Headquarters
# Create your models here.


# Create model  to a groups........................................................................
class Group(models.Model):
    """Represent a Group object"""
    """On staff user can be: morning | afternoon"""
    WORKINGDAY_TYPE_CHOICES = (
        (1, 'Morning'),
        (2, 'Afternoon'),
        (3, 'Nigth')
    )

    schoolyear = models.IntegerField(primary_key=True,
                                 serialize=False, verbose_name='ID')
    nameGroup = models.CharField(max_length=100, null=False)
    workingDay = models.PositiveSmallIntegerField(
        choices=WORKINGDAY_TYPE_CHOICES)
    managerGroup = models.OneToOneField(TeacherUser,
                                     on_delete=models.CASCADE)
    headquarter = models.ForeignKey(
        Headquarters, related_name='groups', on_delete=models.CASCADE)


    def __str__(self):
        return 'The Group was created as: {}, with a code-year: {}'.format(
            self.nameGroup,
            self.schoolyear)
