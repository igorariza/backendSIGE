from django.db import models
from courses.models import AcademicCharge
from users.models import CustomUser

# Create your models here.
class Feed(models.Model):
    """Represent a Feed object"""
    code_feed = models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                 verbose_name='ID')
    title_feed = models.CharField(max_length=255)
    date_feed = models.DateTimeField(auto_now_add=True)
    description_feed = models.CharField(max_length=10000)
    academic_charge = models.ForeignKey(
        AcademicCharge, related_name='forum', on_delete=models.CASCADE)
    user = models.ForeignKey(
        CustomUser, related_name='feeds', on_delete=models.PROTECT)


""" comentario para validar """

# metodo para crear la ruta en el s3 de manera dinamica
def get_upload_path(instance, filename):
    """Metodo para crear la ruta al archivo"""
    academic_charge = instance.feed_id.academic_charge.codeAcademicCharge
    user = instance.feed_id.user.documentIdUser

    return 'Feed/Resources/'+"%s/%s/%s" % (
        academic_charge,
        user,
        filename
    )


class File_forum(models.Model):
    """Represent a Resource object"""
    code_file = models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                 verbose_name='ID')
    feed_id = models.ForeignKey(
        Feed, related_name='infos', on_delete=models.CASCADE)
    resource = models.FileField(upload_to=get_upload_path, blank=True)


class Replay_feed_forum(models.Model):
    code_replay_feed = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT)
    comment = models.CharField(max_length=5000)
    dateComment = models.DateTimeField(auto_now_add=True)
    replay_feed = models.ForeignKey(
        Feed, related_name='replays',on_delete=models.CASCADE)

