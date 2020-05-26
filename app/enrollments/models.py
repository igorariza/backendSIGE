from django.db import models
from groups.models import Group, Journey
from users.models import StudentUser

# Create your models here.
class Enrollment(models.Model):
    """Represent a Area object"""
    codeEnrollment = models.AutoField(auto_created=True, primary_key=True,
                                      serialize=False, verbose_name='ID')
    groupEnrollment = models.ForeignKey(
        Group, related_name='groups', on_delete=models.CASCADE)
    journeyEnrollment  = models.ForeignKey(
        Journey, related_name='journeys', on_delete=models.CASCADE)
    studentEnrollment = models.ForeignKey(
        StudentUser, on_delete=models.CASCADE)
    dateEnrollment = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return 'The Enrollments by the group {}, in the journey {} with a code of Enrrolment {}'.format(
            self.group, self.journey, self.codeEnrollment)
