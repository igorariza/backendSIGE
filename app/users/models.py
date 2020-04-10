#modelos para bd
from django.db import models
#modelos de auth
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin, AbstractUser
#Para validar expresiones regulares
from django.core.validators import RegexValidator
#Para manejar la configuracion
from django.conf import settings
#Para manejar el tiempo 
import datetime
#Para hacer la foreign key con las ie
from institutions.models import Headquarters 
# ========== Modelo del usuario base de Django ========== 
class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        """"Create and save a new user"""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, **extra_fields):
        """Create and save a new staffuser"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        user = self.create_user(email, password, **extra_fields)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a new superuser"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        user = self.create_user(email, password, **extra_fields)
        return user
    
# ========== Modelo para el usuario personalizado========== 
class CustomUser(AbstractUser):

    """Established as no necesary by the model the next fields allows a AbstractUser"""
    username = None
    first_name = None
    last_name = None
    
    """Validate than fields phone and id are ok"""
    phone_or_id_validate = RegexValidator(regex=r'^\+?1?\d{7,10}$', message= "Numero incorrecto")
        
    """Fields own of the customuser"""
    #foto = models.ImageField('Foto de perfil', upload_to= 'users/photos/', blank=True, null=True)
    documentIdUser = models.CharField(validators = [phone_or_id_validate], max_length=10, null = False ,unique=True)
    typeIdeUser = models.CharField(max_length=100, null = False)
    firstNameUser = models.CharField(max_length=100,null = False)
    lastNameUser = models.CharField(max_length=100, null = False)
    emailUser = models.EmailField(max_length=70, blank=True, null= True, unique= True)
    phoneUser = models.CharField(validators = [phone_or_id_validate], max_length=10, null = False, unique=True)
    addressUser = models.CharField(max_length=50, null = False)
    passwordUser = models.CharField(max_length=20,default=[documentIdUser], null = False)
    dateOfBirthUser = models.DateField(default=datetime.date.today, null=False)  
    dateLastAccessUser = models.DateField(default=datetime.date.today, null=False)
    genderUser =  models.CharField(max_length=20, null = False)
    rhUser = models.CharField(max_length=20, null = False)  
    codeHeadquartersUser = models.ForeignKey(Headquarters, on_delete=models.CASCADE)
    """Fields to determinate if a user es active o inactive"""
    is_active = models.BooleanField(default=True)
    """Fields by select a superuser and staffuser"""  
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    """Fields requires"""
    USERNAME_FIELD = 'documentIdUser'
    REQUIRED_FIELDS = [ 'firstNameUser','lastNameUser', 'phoneUser']
    
    """"Add a user manager it model"""
    objects = UserManager()

    """functions by identify the model"""
    def get_full_name(self):
        return self.nombres

    def get_id_user(self):
        return self.documentoID
        
    def __str__(self):
        return str(self.correo)
"""
# ========== Modelo del Docente que contiene un usuario ========== 
class Docente(models.Model):
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    interes_mora = models.FloatField()
    #category = models.CharField(max_length=10)
    cycle = models.CharField(max_length=10)
    contrat_number = models.IntegerField(unique=True)
    financial_state = models.CharField(max_length=10)
    billing = models.CharField(max_length=10)

#==========  Modelo del trabajador que extiende de usuario basico ========== 
class Worker(models.Model):
    USER_TYPE_CHOICES = (
      (1, 'admin'),
      (2, 'manager'),
      (3, 'operator'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
"""