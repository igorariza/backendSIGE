from django.db import models


# import to foreing models
from courses.models import AcademicCharge

# Create model  to a WorkSpace........................................................................


class WorkSpace(models.Model):
    """Represent a WorkSapace object"""
    codeWorkSpace = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nameWorkSpace = models.CharField(max_length=100, null=False)
    academicCharge = models.OneToOneField(AcademicCharge,
                                          on_delete=models.CASCADE)
    descriptionWorkSpace = models.CharField(max_length=255, null=False)

    def __str__(self):
        return 'The Work Space was created as: {}, with a code: {}'.format(
            self.nameWorkSpace,
            self.codeWorkSpace)
