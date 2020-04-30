from django.db import models


# import to foreing models
from workspace.models import WorkSpace

# Create model  to a Secction........................................................................


class Secction(models.Model):
    """Represent a Secction object"""
    codeSecction = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nameSecction = models.CharField(max_length=100, null=False)
    descriptionSecction = models.CharField(max_length=255)
    uploadOnSecction = models.DateTimeField(auto_now_add=True)
    workspaceSecction = models.ForeignKey(
        WorkSpace, related_name='secctions', on_delete=models.CASCADE)

    def __str__(self):
        return 'The Secction was created as: {}, with a code: {}'.format(
            self.nameSecction,
            self.codeSecction)


class Resource(models.Model):
    """Represent a Resource object"""
    codeResouce = models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                   verbose_name='ID')
    resource = models.FileField(upload_to='resources/', blank=True)
    secctionResource = models.ForeignKey(
        Secction, related_name='resources', on_delete=models.CASCADE)

    def __str__(self):
        return 'The Resource was created as: {}'.format(self.file.name)


class HyperLynks(models.Model):
    codeHyperLink = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    url = models.CharField(blank=True, max_length=500)
    secctionHyperlink = models.ForeignKey(
        Secction, related_name='lynks', on_delete=models.CASCADE)

    def __str__(self):
        return 'The Url was created with code: {}'.format(self.codeHyperLink)
