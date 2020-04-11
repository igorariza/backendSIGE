from django.db import models


# Create models here........................................................................
class EducationalInstitution(models.Model):
    """Represent a Education institutional object"""
    codeIE = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nameIE = models.CharField(max_length=100, null=True, unique=True)
    nitIE = models.CharField(max_length=100, null=True, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return 'The IE was created as: {}, with a Nit {}'.format(self.nameIE, self.nitIE)


class Headquarters(models.Model):
    """Represent a Headquarters object"""
    codeHeadquarters = models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                         verbose_name='ID')
    nameHeadquarters = models.CharField(max_length=100)
    daneHeadquarters = models.CharField(max_length=100)
    codeIE = models.ForeignKey(EducationalInstitution,
                               on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return 'The Headquarters was created as: {}, with a DANE: {}'.format(
            self.nameHeadquarters,
            self.daneHeadquarters)
