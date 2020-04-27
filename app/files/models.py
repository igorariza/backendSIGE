from django.db import models
from django.conf import settings
# Importamos los usuarios.
from users.models import TeacherUser
# Create models here........................................................................

# Model to the file in the evidences of the teachers........................................................................
class File(models.Model):
    """Represent a File object"""
    codeFile = models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                     verbose_name='ID')
    uploadOnFile = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='evidences/', blank=True)

    def __str__(self):
        return 'The File was created as: {}'.format(self.file.name)

# Model to the profile picture to the user........................................................................



#Create model to Evidence ...................................................................
class Evidence(models.Model):
    """Represent a Evidence object"""
    EVIDENCE_TYPE_CHOICES = (
      (1, 'degree'),
      (2, 'curriculum vitae'),
      (3, 'certified'),
      )
    
    codeEvidence = models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                     verbose_name='ID')
    nameEvidence = models.CharField(max_length=100, null = False)
    descriptionEvidence = models.CharField(max_length=255, null = False)
    teacher = models.ForeignKey(TeacherUser, related_name='evidences',on_delete=models.CASCADE)
    typeEvidence = models.PositiveSmallIntegerField(choices=EVIDENCE_TYPE_CHOICES)  
    file = models.OneToOneField(File, on_delete=models.CASCADE)

    class Meta:
        ordering = ['codeEvidence']
    
    
    def __str__(self):
        return 'The File was created as: {}'.format(self.nameEvidence) 