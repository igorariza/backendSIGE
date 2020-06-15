from django.db import models


# import to foreing models
from workspace.models import WorkSpace
from users.models import StudentUser, TeacherUser


# Create model  to a Secction........................................................................


class Secction(models.Model):
    """Represent a Secction object"""
    codeSecction = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nameSecction = models.CharField(max_length=100, null=False)
    descriptionSecction = models.CharField(max_length=5000)
    uploadOnSecction = models.DateTimeField(auto_now_add=True)
    workspaceSecction = models.ForeignKey(
        WorkSpace, related_name='secctions', on_delete=models.PROTECT)

    def __str__(self):
        return 'The Secction was created as: {}, with a code: {}'.format(
            self.nameSecction,
            self.codeSecction)


def get_upload_path(instance, filename):
    """Metodo para crear la ruta al archivo"""
    worckspace = instance.secctionResource.workspaceSecction.codeWorkSpace
    seccion = instance.secctionResource.codeSecction

    return 'Secctions/Resources/'+"%s/%s/%s" % (
        worckspace,
        seccion,
        filename
    )


class Resource(models.Model):
    """Represent a Resource object"""
    codeResouce = models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                   verbose_name='ID')
    secctionResource = models.ForeignKey(
        Secction, related_name='resources', on_delete=models.PROTECT)
    resource = models.FileField(upload_to=get_upload_path, blank=True)

    def __str__(self):
        return 'The Resource was created as: {}'.format(self.file.name)


class HyperLynks(models.Model):
    codeHyperLink = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    url = models.CharField(blank=True, max_length=500)
    secctionHyperlink = models.ForeignKey(
        Secction, related_name='lynks', on_delete=models.PROTECT)

    def __str__(self):
        return 'The Url was created with code: {}'.format(self.codeHyperLink)


def get_upload_response_path(instance, filename):
    """Metodo para crear la ruta al archivo"""
    worckspace = instance.secctionResponse.workspaceSecction.codeWorkSpace
    seccion = instance.secctionResponse.codeSecction
    student = instance.studentResponse.codeStudent
    return 'Secctions/Responses/'+"%s/%s/%s/%s" % (
        worckspace,
        seccion,
        student,
        filename
    )


class ResponseSecction(models.Model):
    """Represent a Resource Response object"""
    codeResponse = models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                    verbose_name='ID')
    secctionResponse = models.ForeignKey(
        Secction, related_name='responses', on_delete=models.PROTECT)
    response = models.FileField(upload_to=get_upload_response_path, blank=True)
    messageResponse = models.CharField(max_length=1000)
    dateResponse = models.DateTimeField(auto_now_add=True)

    studentResponse = models.ForeignKey(StudentUser, related_name='responses',
                                        on_delete=models.PROTECT)

    def __str__(self):
        return 'The Response was created as: {}'.format(self.file.name)


class Comment(models.Model):
    codeComment = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    teacherComment = models.ForeignKey(
        TeacherUser, on_delete=models.PROTECT)
    comment = models.CharField(max_length=500)
    dateComment = models.DateTimeField(auto_now_add=True)
    responseToComment = models.OneToOneField(
        ResponseSecction, on_delete=models.PROTECT)

    def __str__(self):
        return 'The Comment was created with code: {}'.format(self.codeComment)

