from django.db import models

class Tutorials(models.Model):
    """Represent a Area object"""
    codeTutorial = models.AutoField(auto_created=True, primary_key=True,
                                      serialize=False, verbose_name='ID')
    nameTutorial  = models.CharField(max_length=255)
    typeTutorial  = models.CharField(max_length=500)
    urlTutorial = models.CharField(max_length=500)
    likeTutorial = models.PositiveIntegerField()
    
    def __str__(self):
        return 'The Tutorial was created'.format(
            self.codeTutorial)
