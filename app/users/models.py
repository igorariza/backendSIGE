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
    codeUser = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    documentIdUser = models.CharField(validators = [phone_or_id_validate], max_length=10, null = False ,unique=True)
    typeIdeUser = models.CharField(max_length=100, null = False)
    firstNameUser = models.CharField(max_length=100,null = False)
    lastNameUser = models.CharField(max_length=100, null = False)
    emailUser = models.EmailField(max_length=70, blank=True, null= True, unique= True)
    phoneUser = models.CharField(validators = [phone_or_id_validate], max_length=10, null = False, unique=True)
    addressUser = models.CharField(max_length=50, null = False)
    passwordUser = models.CharField(max_length=200,default=[documentIdUser], null = False)
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

# ========== Modelo del Docente que contiene un usuario ========== 
class TeacherUser(models.Model):
    
    """create a user"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    """fields to TeacherUser"""
    codeTeacher = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    degreesTeacher = models.CharField(max_length=100)

# ========== Modelo del Estudiante que contiene un usuario ========== 
class StudentUser(models.Model):
    
    """create a user"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    """fields to TeacherUser"""
    codeStudent = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')


#==========  Modelo del familiar que extiende de usuario basico ========== 
class RelativeUser(models.Model):
    
    """On staff user can be: Parent | Attending"""
    USER_TYPE_CHOICES = (
      (1, 'parent'),
      (2, 'attending'),
    )
    """create a relation with a user"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    """fields to Relative"""
    codeRelative = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    typeRelative = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE)

#==========  Modelo del trabajador que extiende de usuario basico ========== 
class StaffUser(models.Model):
    
    """On staff user can be: Principal | Subprincial | Payer |
       assistantSIMAT | assistant"""
    USER_TYPE_CHOICES = (
      (1, 'principal'),
      (2, 'subprincial'),
      (3, 'payer'),
      (4, 'assistant'),
      (5, 'assistantSIMAT'),
    )
    """create a relation with a user"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    """fields to Staff"""
    codeStaff = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    ocupationStaff = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
