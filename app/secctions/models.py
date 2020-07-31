from django.db import models
from django.utils import timezone
#
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
#
# import to foreing models
from workspace.models import WorkSpace
from users.models import StudentUser, TeacherUser


# Create model  to a Secction..........................................................


class Secction(models.Model):
    """Represent a Secction object"""
    codeSecction = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nameSecction = models.CharField(max_length=100, null=False)
    descriptionSecction = models.CharField(max_length=5000)
    uploadOnSecction = models.DateTimeField(auto_now_add=True)
    date_close = models.DateTimeField(
        default=timezone.now, blank=True, null=True)
    workspaceSecction = models.ForeignKey(
        WorkSpace, related_name='secctions', on_delete=models.PROTECT)
    image_found = models.CharField(
        max_length=5000, default='https://res.cloudinary.com/duyflkcyn/image/upload/v1595312014/SIGE/ActivitiesPhothos/3_talrgu.jpg',
        null=True)

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
        Secction, related_name='resources', on_delete=models.CASCADE)
    resource = models.FileField(upload_to=get_upload_path, blank=True)


class HyperLynks(models.Model):
    codeHyperLink = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    url = models.CharField(blank=True, max_length=500)
    secctionHyperlink = models.ForeignKey(
        Secction, related_name='lynks', on_delete=models.CASCADE)


def get_upload_response_path(instance, filename):
    """Metodo para crear la ruta al archivo"""
    print("\nInstancia\n", instance, "\n\n")
    worckspace = instance.response_secction.secction_response.workspaceSecction.codeWorkSpace
    seccion = instance.response_secction.secction_response.codeSecction
    student = instance.response_secction.student_response_id
    return 'Secctions/Responses_New/'+"%s/%s/%s/%s" % (
        worckspace,
        seccion,
        student,
        filename
    )


class Responses(models.Model):
    """Represent a Resource Response object"""
    code_response = models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                     verbose_name='ID')
    secction_response = models.ForeignKey(
        Secction, related_name='response', on_delete=models.CASCADE)
    message_response = models.CharField(max_length=1000)
    date_response = models.DateTimeField(auto_now_add=True)
    student_response = models.ForeignKey(StudentUser, related_name='responses',
                                         on_delete=models.PROTECT)


class Homework(models.Model):
    """Represent a Resource Response object"""
    code_homework = models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                   verbose_name='ID')
    response_secction = models.ForeignKey(
        Responses, related_name='homework', on_delete=models.CASCADE)
    response_file = models.FileField(
        upload_to=get_upload_response_path, blank=True, null=True)


class ResponseSecction(models.Model):
    """Represent a Resource Response object"""
    codeResponse = models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                    verbose_name='ID')
    secctionResponse = models.ForeignKey(
        Secction, related_name='responses', on_delete=models.CASCADE)
    response = models.FileField(
        upload_to=get_upload_response_path, blank=True, null=True)
    messageResponse = models.CharField(max_length=1000)
    dateResponse = models.DateTimeField(auto_now_add=True)
    studentResponse = models.ForeignKey(StudentUser, related_name='response',
                                        on_delete=models.PROTECT)


class Comment(models.Model):
    codeComment = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    teacherComment = models.ForeignKey(
        TeacherUser, on_delete=models.PROTECT)
    comment = models.CharField(max_length=500)
    dateComment = models.DateTimeField(auto_now_add=True)
    responseToComment = models.OneToOneField(
        Responses, on_delete=models.CASCADE)
    score = models.FloatField(null=True)

    def __str__(self):
        return 'The Comment was created with code: {}'.format(self.codeComment)
