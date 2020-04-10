from django.db import models


# Create models here........................................................................

class EducationalInstitution(models.Model):
    """Represent a Education institutional object"""
    nameIE = models.CharField(max_length=100, null=True, unique=True)
    nitIE = models.CharField(max_length=100, null=True, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return 'The IE was created as: {}'.format(self.nameIE)


class Headquarters(models.Model):
    """Represent a Headquarters object"""
    nameHeadquarters = models.CharField(max_length=255)
    daneHeadquarters = models.CharField(max_length=255)
    codeIE = models.ForeignKey(EducationalInstitution,
                               on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return 'The Headquarters was created as: {}, with a DANE: {}'.format(
            self.nameHeadquarters,
            self.daneHeadquarters)
