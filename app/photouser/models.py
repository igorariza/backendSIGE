from django.db import models
from users.models import CustomUser
# Create your models here.



def get_upload_path(instance, filename):
    """Metodo para crear la ruta al archivo"""
    ie = instance.user.codeIE.nameIE
    sede = instance.user.codeHeadquarters.nameHeadquarters
    user = instance.user.documentIdUser

    return 'ProfilePrictures/'+"%s/%s/%s/%s" % (
        ie,
        sede,
        user,
        filename
        
    )
    

class ProfilePicture(models.Model):
    """Represent a Resource object"""
    codePhoto = models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                   verbose_name='ID')
    photo = models.ImageField(upload_to=get_upload_path, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.PROTECT)

    def __str__(self):
        return 'The Picture was created as: {}'.format(self.codePhoto)